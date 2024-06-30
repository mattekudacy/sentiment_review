import os
import streamlit as st
import pandas as pd
from utils.data_utils import load_data, display_data
from utils.plot_utils import create_bar_chart
from utils.analysis_utils import get_sentiment_pipeline, perform_sentiment_analysis, display_wordclouds

# Set the cache directory for Hugging Face models
os.environ["TRANSFORMERS_CACHE"] = "./hf_cache"

@st.cache_data
def get_data(file):
    data = load_data(file)
    return data

@st.cache_data
def analyze_sentiment(text_data):
    sentiment_pipeline = get_sentiment_pipeline()
    sentiments, scores = perform_sentiment_analysis(text_data, sentiment_pipeline)
    return sentiments, scores

def download_csv(analysis_df):
    st.write("### Download Results")
    csv = analysis_df.to_csv(index=False)
    st.download_button(label="Download as CSV", data=csv, file_name='sentiment_analysis.csv', mime='text/csv')

def main():
    st.set_page_config(page_title='Sentiment Review', page_icon='📗')
    st.title('Sentiment Review📗📘')
    st.write('Upload a CSV file to perform sentiment analysis on the text data.')

    file = st.file_uploader('Upload a file', type=['csv'])
    if file is not None:
        data = get_data(file)
        
        options = ["All"] + data.columns.tolist()
        selected_option = st.selectbox('Select columns to display', options)
        
        if selected_option != "All":
            if st.button('Choose this column for sentiment analysis'):
                text_data = data[selected_option].astype(str)
                sentiments, scores = analyze_sentiment(text_data)
                
                analysis_df = pd.DataFrame({
                    selected_option: text_data,
                    'Sentiment': sentiments,
                    'Sentiment Score': scores
                })
                
                display_data(analysis_df, title="# Sentiment Analysis Results")
                create_bar_chart(analysis_df)
                display_wordclouds(analysis_df, selected_option)
                download_csv(analysis_df)

        if selected_option == "All":
            display_data(data, title="All Columns Data")
        else:
            display_data(data[[selected_option]], title=f"Data for Column: {selected_option}")

if __name__ == '__main__':
    main()

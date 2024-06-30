from transformers import pipeline
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import streamlit as st

nltk.download('stopwords')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(f'[{re.escape(string.punctuation)}]', '', text)
    text = re.sub(r'\d+', '', text)
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    text = ' '.join([lemmatizer.lemmatize(word) for word in text.split()])
    return text

@st.cache_resource
def get_sentiment_pipeline():
    return pipeline("sentiment-analysis", model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def perform_sentiment_analysis(text_data, sentiment_pipeline):
    analysis_results = [sentiment_pipeline(text)[0] for text in text_data]
    sentiments = [result['label'] for result in analysis_results]
    scores = [result['score'] for result in analysis_results]
    return sentiments, scores

def generate_wordcloud(text, title):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(text))
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    st.pyplot(plt)

def display_wordclouds(analysis_df, selected_option):
    st.write("### Word Clouds")
    positive_text = analysis_df[analysis_df['Sentiment'] == 'POSITIVE'][selected_option].apply(preprocess_text)
    negative_text = analysis_df[analysis_df['Sentiment'] == 'NEGATIVE'][selected_option].apply(preprocess_text)
    generate_wordcloud(positive_text, "Positive Sentiment Word Cloud")
    generate_wordcloud(negative_text, "Negative Sentiment Word Cloud")

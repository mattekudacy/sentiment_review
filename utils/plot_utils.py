import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

def create_bar_chart(analysis_df):
    st.write("## Positive vs Negative Sentiments")
    overall = analysis_df.size
    positive = analysis_df['Sentiment'].value_counts(normalize=True)['POSITIVE'] * 100
    negative = analysis_df['Sentiment'].value_counts(normalize=True)['NEGATIVE'] * 100
    html_str = f"""
    <style>
        .overall {{
        font-style: bold;
        }}

        .positive {{
        color: green;
        }}

        .negative {{
        color: red;
        }}

    </style>
    <p>There are <span class="a">{overall}</span> records in the dataset. <span class="positive">{positive:.2f}%</span> are positive and <span class="negative">{negative:.2f}%</span> are negative.</p>
"""
    
    st.markdown(html_str, unsafe_allow_html=True)
    plt.figure(figsize=(10, 6))

    # Calculate the percentage of each sentiment
    sentiment_counts = analysis_df['Sentiment'].value_counts()
    sentiment_percentages = (sentiment_counts / sentiment_counts.sum()) * 100

    # Create a DataFrame for the bar plot
    sentiment_df = sentiment_percentages.reset_index()
    sentiment_df.columns = ['Sentiment', 'Percentage']

    # Create a bar plot with custom colors
    ax = sns.barplot(x='Sentiment', y='Percentage', hue='Sentiment', data=sentiment_df,
                     palette={'NEGATIVE': 'red', 'POSITIVE': 'green'}, dodge=False, legend=False)

    # Annotate the bar chart with percentages
    for p in ax.patches:
        percentage = f'{p.get_height():.2f}%'
        ax.annotate(percentage, (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')

    plt.title('Sentiment Analysis Results')
    plt.xlabel('Sentiment')
    plt.ylabel('Percentage')
    st.pyplot(plt)
    

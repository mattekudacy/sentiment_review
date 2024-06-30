# Sentiment Review

Sentiment Review is a Streamlit web application that performs sentiment analysis on text data from a CSV file. It uses the Hugging Face Transformers library for sentiment analysis and provides various features such as data filtering, visualization, and word cloud generation.

## Features

- Upload CSV files containing text data
- Select columns for sentiment analysis
- Display sentiment analysis results with sentiment scores
- Generate annotated bar charts for positive and negative sentiments
- Create word clouds for positive and negative sentiments
- Filter results by sentiment
- Download the analysis results as a CSV file

## Installation

To run the Sentiment Review application, you need to have Docker installed. Follow these steps to set up and run the application:

### Clone the Repository

```bash
git clone https://github.com/yourusername/sentiment_review.git
cd sentiment_review
```

### Build the Docker Image

```bash
docker build -t sentiment_review .
```

### Run the Docker Container
```bash
docker run -p 8501:8501 sentiment_review
```

## Usage

### Upload a CSV File
1. Click on the **Upload a File** button.
2. Select a CSV file containing the text data you want to analyze.

### Select Columns for Analysis
1. Choose a column from the dropdown menu to display its data.
2. Click the button to select the column for sentiment analysis.

### View Analysis Results
- Sentiment Analysis Results: Displays the sentiment and sentiment score for each row in the selected column.
- Annotated Bar Chart: Shows the percentage of positive and negative sentiments.
- Word Clouds: Visualizes the most frequent words in positive and negative sentiments.

### Download Results
- Click the **Download as CSV** button to download the sentiment analysis results.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes.



FROM python:3.9-slim

ENV TRANSFORMERS_CACHE=/app/hf_cache
ENV STREAMLIT_HOME=/app

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

ENTRYPOINT ["streamlit", "run", "Sentiment_Review.py"]

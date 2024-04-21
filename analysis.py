from transformers import pipeline
from io import BytesIO


# Choose a pre-trained model for sentiment analysis
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

# Create a pipeline for sentiment analysis
classifier = pipeline("sentiment-analysis", model=model_name)

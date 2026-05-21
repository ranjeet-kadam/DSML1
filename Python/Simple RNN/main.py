# main.py
import streamlit as st
from pathlib import Path
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
from tensorflow.keras.datasets import imdb # Correct import from Keras datasets

  # Check for model file
MODEL_PATH = "simple_rnn_model.h5"
if not Path(MODEL_PATH).exists():
    st.error(f"⚠️  Model file '{MODEL_PATH}' not found!")
    st.info("Please train your model first using the notebooks")
    st.stop()

# Load pre-trained model
try:
    model = load_model(MODEL_PATH)
    st.success(f"✅ Loaded model from {MODEL_PATH}")
except Exception as e:
  st.error(f"❌ Model loading failed: {str(e)}")
  st.stop()

  # Load word index mapping for text preprocessing
try:
    (_, _), _ = imdb.load_data(num_words=10000)  # Load vocabulary
    word_index = imdb.get_word_index()
    reverse_word_index = {i: word for word, i in word_index.items()}
    max_features = 10000
    max_len = 500
except Exception as e:
  st.warning(f"⚠️  Could not load word index: {str(e)}")
  st.info("Using dummy word index for demonstration")
  word_index = {i: f"UNK-{i}" for i in range(1000)}
  reverse_word_index = {i: f"UNK-{i}" for i in range(1000)}

def preprocess_text(text):
  """Convert text to model-ready sequence"""
  words = text.lower().split()
  encoded_seq = [word_index.get(word, 2)+3 for word in words]  # 2 = unknown token
  padded = sequence.pad_sequences([encoded_seq], maxlen=max_len)
  return padded

def predict_sentiment(text):
  """Make prediction using loaded model"""
  processed = preprocess_text(text)
  prediction = model.predict(processed)[0][0]
  return "Positive" if prediction > 0.5 else "Negative", prediction

def decode_sequence(encoded_seq):
  """Convert model output back to readable text"""
  indices = encoded_seq[0][encoded_seq[0] > 2]  # Remove padding
  return " ".join([reverse_word_index.get(i, "?") for i in indices])

# Streamlit App
st.title("🧠 RNN Text Classifier (Sentiment Analysis)")

 # Input Section
input_text = st.text_area(
  "Enter your text for analysis",
  height=150,
  placeholder="Example: 'This product is amazing!' or 'Terrible experience.'"
)

if st.button("Analyze"):
  if input_text.strip():
     try:
        sentiment, confidence = predict_sentiment(input_text)
        decoded_text = decode_sequence(preprocess_text(input_text))
        st.markdown(f"### 🎯 Prediction: **{sentiment}**")
        st.write(f"Confidence: {confidence:.2f}")
        with st.expander("🔍 Decoded Input"):
            st.write(f"*{decoded_text}*")
            if sentiment == "Positive":
               st.success(f"✨ Confidence: {confidence:.2f}")
            else:
               st.error(f"❌ Confidence: {confidence:.2f}")
     except Exception as e:
        st.error(f"❌ Analysis failed: {str(e)}")
  else:
     st.warning("Please enter some text to analyze")

  # Model Info
with st.expander("ℹ️  Model Details"):
    st.write(f"- Embedding Dimension: 128")
    st.write(f"- RNN Units: 128")
    st.write(f"- Output Layer: Binary Classification")
    st.write(f"- Trained on: IMDB-like dataset (word index: {len(word_index)} words)")

  # Usage Tips
st.sidebar.markdown("### 🔧 Quick Start")
st.sidebar.markdown("1. Enter text in the box above")
st.sidebar.markdown("2. Click 'Analyze' to get prediction")
st.sidebar.markdown("3. View decoded input for transparency")
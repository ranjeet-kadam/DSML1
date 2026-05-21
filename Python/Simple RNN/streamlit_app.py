import streamlit as st
from pathlib import Path
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.datasets import imdb

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "simple_rnn_model.h5"

st.set_page_config(
    page_title="IMDB Sentiment Predictor",
    page_icon="🎥",
    layout="centered",
)

st.title("IMDB Movie Review Sentiment Predictor")
st.write(
    "Type a movie review below and the app will use your trained Simple RNN model to predict whether the sentiment is positive or negative. "
    "This app uses the same preprocessing logic as `prediction.ipynb` and `simple_rnn.ipynb`."
)

@st.cache_resource
def load_trained_model(path: Path):
    return load_model(str(path))

@st.cache_resource
def load_imdb_word_index():
    return imdb.get_word_index()

@st.cache_data
def preprocess_text(text: str, word_index: dict, maxlen: int = 500):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=maxlen)
    return padded_review

def predict_sentiment(model, text: str, word_index: dict):
    data = preprocess_text(text, word_index)
    prediction = model.predict(data, verbose=0)
    score = float(prediction[0][0])
    sentiment = "Positive" if score > 0.5 else "Negative"
    return sentiment, score

with st.sidebar:
    st.header("Instructions")
    st.markdown(
        "1. Enter a movie review in the text box.\n"
        "2. Click **Predict Sentiment**.\n"
        "3. The model returns a sentiment label and confidence score."
    )
    st.markdown("---")
    st.markdown("**Model file:** `simple_rnn_model.h5`")
    st.markdown("**Notebook references:** `prediction.ipynb`, `simple_rnn.ipynb`")

default_review = (
    "One of the best movies I have seen in a long time. The plot was engaging and the acting was superb."
)
review_text = st.text_area("Enter your movie review:", default_review, height=180)
predict_button = st.button("Predict Sentiment")

model = load_trained_model(MODEL_PATH)
word_index = load_imdb_word_index()

if predict_button:
    if not review_text.strip():
        st.warning("Please enter a review before predicting.")
    else:
        with st.spinner("Analyzing review..."):
            sentiment, score = predict_sentiment(model, review_text, word_index)

        st.subheader("Prediction Result")
        st.metric(label="Sentiment", value=sentiment)
        st.info(f"Confidence score: {score:.4f}")

        if sentiment == "Positive":
            st.success("The review appears to be positive.")
        else:
            st.error("The review appears to be negative.")

        st.markdown("---")
        st.markdown("### Review text")
        st.write(review_text)

st.markdown("---")
if st.checkbox("Show model summary"):
    with st.expander("Model architecture"):
        model_summary = []
        model.summary(print_fn=lambda line: model_summary.append(line))
        st.text("\n".join(model_summary))

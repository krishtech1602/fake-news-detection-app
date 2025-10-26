import streamlit as st
import joblib
import re


model=joblib.load("news_model.pkl")
vectorizer=joblib.load("vectorizer.pkl")

def clean_text(text):
    if not text:
        text = ''
    text = re.sub(r'http\S+', '', text)        # Remove URLs
    text = re.sub('[^a-zA-Z]', ' ', text)      # Keep letters only
    text = text.lower()                         # Lowercase
    text = re.sub(r'\s+', ' ', text).strip()   # Remove extra spaces
    return text

st.title("Fake News Detection App")
st.write("Enter a news article below and find out if its **Fake** or **Real**!")

user_input=st.text_area("Enter the news article text here")

if st.button("Predict"):
    if user_input.strip() != "":
        cleaned_text = clean_text(user_input)
        vectorized_text = vectorizer.transform([cleaned_text])
        prediction = model.predict(vectorized_text)[0]
        if prediction == 0:
            st.error("🚨 This news seems **Fake**.")
        else:
            st.success("✅ This news seems **Real**.")

📰 Fake News Detection App
📘 Project Overview

The Fake News Detection App is a machine learning-based project that classifies news articles as Real or Fake using Natural Language Processing (NLP) and Logistic Regression.
It helps users verify the authenticity of news content quickly and interactively through a simple Streamlit web app.

⚙️ Features

✅ Detects whether a news article is Fake or Real

🧹 Preprocesses text data (cleaning, removing URLs & special characters)

🧠 Uses TF-IDF Vectorization and Logistic Regression

💻 Interactive Streamlit web interface for real-time predictions

📦 Modular design – easy to update or retrain with new datasets

🧰 Tools & Libraries Used

Python

Pandas, NumPy – Data handling and preprocessing

Scikit-learn – Model training and evaluation

Joblib – Model serialization

Streamlit – Frontend web application

📊 Project Workflow

Data Collection – Merge and label True.csv and Fake.csv datasets

Preprocessing – Clean text using regex (remove URLs, symbols, extra spaces)

Feature Extraction – Convert text to numerical form using TF-IDF Vectorizer

Model Training – Train Logistic Regression to classify news

Evaluation – Check accuracy, confusion matrix, and classification report

Deployment – Streamlit app for real-time news verification

🏁 Conclusion

This project demonstrates how NLP and Machine Learning can effectively detect misinformation.
The combination of TF-IDF features and Logistic Regression delivers high accuracy and a fast, interpretable model suitable for real-world news verification.

# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1I5HnDuZahmKQL5jgTTP7wvm7UmoogCEt
"""

!pip install streamlit

import streamlit as st
from joblib import load
import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

# Construct the full file paths
model_path = os.path.join(current_directory, 'hate_speech_model(1).pkl')
vectorizer_path = os.path.join(current_directory, 'count_vectorizer(1).pkl')

# Check if the files exist
if os.path.exists(model_path) and os.path.exists(vectorizer_path):
    # Load the model and vectorizer
    clf = load(model_path)
    cv = load(vectorizer_path)

    def hate_speech_detection(tweet):
        data = cv.transform([tweet]).toarray()
        prediction = clf.predict(data)
        return prediction[0]

    st.title("Hate Speech Detection")
    user_input = st.text_area("Enter a Tweet:")

    if user_input:
        prediction = hate_speech_detection(user_input)
        st.write(f"Prediction: {prediction}")
else:
    st.write("Error: Model or vectorizer file not found. Please make sure the files 'hate_speech_model(1).pkl' and 'count_vectorizer(1).pkl' exist in the current directory.")


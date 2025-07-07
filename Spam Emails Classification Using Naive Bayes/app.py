import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# Load trained model and vectorizer
def load_model():
    with open('model/nb_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    return model

def load_vectorizer():
    with open('model/vectorizer.pkl', 'rb') as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    return vectorizer

# Load model
model = load_model()
# Load vectorizer
vectorizer = load_vectorizer()

@app.route('/predict', methods=['POST'])
def predict():
    if 'message' not in request.form:
        return jsonify({'error': 'No message provided'}), 400

    message = request.form['message']
    message_vectorized = vectorizer.transform([message])
    
    # Make prediction
    prediction = model.predict(message_vectorized)
    
    return render_template('index.html', prediction=prediction[0], message=message)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
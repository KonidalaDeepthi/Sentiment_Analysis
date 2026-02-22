# Sentiment_Analysis
Predicts the emotion of a tweet or any sentence. The app classifies text into emotions like positive, negative, or neutral using machine learning algorithms.
# Twitter Sentiment Analysis Web App

## What is this project?

This is a simple web app that can **understand the emotion of a sentence or tweet**.  
It can tell if your text is **positive, negative, or neutral**.  

For example:  
- "I am very happy today!" → Positive  
- "I feel sad about this." → Negative  
- "I am at the park." → Neutral  

---

## How does it work?

1. The app **cleans your text** (removes links, symbols, and extra spaces).  
2. Converts the text into numbers using **TF-IDF**.  
3. Uses a **trained machine learning model** (SVM, Logistic Regression, or Naive Bayes) to predict the sentiment.  
4. Shows the result on the screen.
## Features
- Clean and preprocess text automatically  
- Predict Positive, Negative, or Neutral emotion  
- Works with any sentence you type  
- Interactive web app using **Streamlit**
## Tools and Technologies Used
- **Python 3**  
- **Streamlit** (for the web app)  
- **scikit-learn** (for machine learning models)  
- **Joblib** (for saving and loading the model)  
- **Pandas & NumPy** (for data handling)  
- **TF-IDF** (to convert text into numbers.
## How to Run Locally
1. Clone this repository  
2. Install required libraries:
```bash
pip install -r requirements.txt

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "bf0bc386",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-02-22 22:58:54.663 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.436 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run c:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-02-22 22:59:00.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.442 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.445 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.446 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.448 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.450 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.452 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.456 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.459 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.462 Session state does not function when running a script without `streamlit run`\n",
      "2026-02-22 22:59:00.465 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.474 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-02-22 22:59:00.478 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import joblib\n",
    "import re\n",
    "\n",
    "# Load model and vectorizer\n",
    "model = joblib.load(\"sentiment_model_svm.pkl\")\n",
    "vectorizer = joblib.load(\"tfidf_vectorizer.pkl\")\n",
    "\n",
    "# Cleaning function\n",
    "def clean_text(text):\n",
    "    text = str(text).lower()\n",
    "    text = re.sub(r'http\\S+', '', text)\n",
    "    text = re.sub(r'[^a-zA-Z\\s]', '', text)\n",
    "    text = re.sub(r'\\s+', ' ', text).strip()\n",
    "    return text\n",
    "\n",
    "# Prediction function\n",
    "def predict_emotion(sentence):\n",
    "    sentence = clean_text(sentence)\n",
    "    sentence_vec = vectorizer.transform([sentence])\n",
    "    prediction = model.predict(sentence_vec)\n",
    "    return prediction[0]\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"Twitter Sentiment Analysis\")\n",
    "st.write(\"Type a tweet or sentence below and see the predicted emotion!\")\n",
    "\n",
    "tweet = st.text_input(\"Enter your sentence here:\")\n",
    "\n",
    "if tweet:\n",
    "    emotion = predict_emotion(tweet)\n",
    "    st.write(\"Predicted Emotion:\", emotion)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

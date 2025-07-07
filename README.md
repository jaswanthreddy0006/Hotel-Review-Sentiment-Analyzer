# 🏨 Hotel Review Sentiment Analyzer

![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

> AI-powered hotel review analyzer that performs sentiment classification and keyword extraction with exportable Excel and CSV reports.

---

## 📌 Overview

This project analyzes hotel reviews to understand customer satisfaction, extract service highlights and pain points using natural language processing (NLP). It features a simple Streamlit web interface where users can input reviews and download results.

---

## 🎯 Goals

- 📊 Summarize customer sentiment from hotel reviews  
- 🔍 Identify key service strengths and weaknesses  
- 📥 Export input & output as CSV and Excel (.xlsx)

---

## ✨ Features

### 1. 🤖 AI-Powered Sentiment Analysis & Keyword Extraction

- Uses `distilbert-base-uncased-finetuned-sst-2-english` from Hugging Face
- Classifies sentiment as **Positive**, **Negative**, or **Neutral**
- Extracts clean and **non-repetitive** keywords for each review

### 2. 📥 CSV and Excel Downloads

- Generate and download results in `.csv` or `.xlsx` format
- Excel output created using `xlsxwriter` for neat formatting

### 3. 🌐 Streamlit Web Interface

- Simple form-based UI to input 5 hotel reviews
- Results appear instantly below the form
- Built-in download buttons for both file formats

---

## 🛠️ Tech Stack

| Component      | Technology                                 |
|----------------|---------------------------------------------|
| Language       | Python 3.9+                                 |
| Web Framework  | Streamlit                                   |
| NLP Model      | Hugging Face Transformers                   |
| Sentiment Model| distilbert-base-uncased-finetuned-sst-2-english |
| Data Handling  | Pandas, CSV, XlsxWriter                     |

---

## 🏗️ Architecture

### 📈 Data Flow

1. User submits up to 5 reviews  
2. Model performs sentiment classification  
3. Keywords are extracted with duplication removal  
4. Output is displayed in a table  
5. CSV and Excel files are generated for download  

---

## ▶️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/hotel-review-sentiment.git
cd hotel-review-sentiment

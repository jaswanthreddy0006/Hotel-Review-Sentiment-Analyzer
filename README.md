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



## 🧪 Sample Input

> Enter **5 reviews** (as required input):

The room was clean but the staff was very rude.

Loved the food and ambiance. Everything was perfect.

Poor service and noisy environment. Never coming back.

Excellent hospitality and very comfortable stay.

Not satisfied with room cleanliness and response time.



---

## 📊 Sample Output (on webpage)

| Review | Sentiment | Keywords |
|--------|-----------|----------|
| The room was clean but the staff was very rude. | Negative | room, clean, staff |
| Loved the food and ambiance. Everything was perfect. | Positive | food, ambiance |
| Poor service and noisy environment. Never coming back. | Negative | service, environment |
| Excellent hospitality and very comfortable stay. | Positive | hospitality, stay |
| Not satisfied with room cleanliness and response time. | Negative | room, cleanliness, response |

✅ Downloaded as `output_reviews.xlsx` with both input and output.

---

## ⬇️ Downloadable Files

- 📥 **Input File (auto-generated)**: Contains your entered reviews
- 📥 **Output File (auto-generated)**: Contains sentiment & extracted keywords
- ✅ All files exported in `.xlsx` format using `xlsxwriter`

---



## 🏗️ Project Structure

hotel-review-sentiment/
├── app.py # Main Streamlit application
├── requirements.txt # Python dependencies
├── output_reviews.xlsx # Exported output (created after running)
├── README.md # Full documentation (this file)


---

📁 Files You’ll See
File	Description
app.py	Main Streamlit app file
requirements.txt	List of all required Python packages
output_reviews.xlsx	Excel file with reviews and sentiment results
README.md	This documentation

📌 Future Improvements (Optional Ideas)
Multi-label sentiment (detect multiple emotions)

Admin dashboard for visual analytics

Topic clustering of reviews using LDA

Deploy to cloud (e.g., Streamlit Cloud or Heroku)

📜 License
This project is for educational purposes under the MIT License.

🙌 Credits
Built by [Your Name]
Model by 🤗 Hugging Face Transformers
Web UI using Streamlit

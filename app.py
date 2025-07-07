import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from transformers import pipeline
import pandas as pd
import io

# Set up sentiment pipeline
sentiment_pipeline = pipeline("sentiment-analysis")

# Streamlit UI setup
st.set_page_config(page_title="Hotel Review Sentiment Analyzer", layout="wide")
st.title("🏨 Hotel Review Sentiment Analyzer with CSV Export")
st.markdown("Enter **5 hotel reviews**. The app will analyze sentiment, extract service-related keywords, and let you download the results as a CSV file for Excel.")

# User form
with st.form("review_form"):
    review1 = st.text_area("Review 1", height=100)
    review2 = st.text_area("Review 2", height=100)
    review3 = st.text_area("Review 3", height=100)
    review4 = st.text_area("Review 4", height=100)
    review5 = st.text_area("Review 5", height=100)
    submitted = st.form_submit_button("Analyze Reviews")

# On submit
if submitted:
    reviews = [review1, review2, review3, review4, review5]

    if any(r.strip() == "" for r in reviews):
        st.warning("⚠️ Please fill all 5 reviews.")
    else:
        st.subheader("📊 Sentiment Analysis")
        sentiments = sentiment_pipeline(reviews)

        result_data = []
        for i, (review, sentiment) in enumerate(zip(reviews, sentiments)):
            label = "Positive 😊" if sentiment['label'] == "POSITIVE" else "Negative 😞"
            st.markdown(f"**Review {i+1}:** {label} (Confidence: {sentiment['score']:.2f})")
            result_data.append({
                "Review Number": f"Review {i+1}",
                "Review Text": review,
                "Sentiment": sentiment['label'],
                "Confidence": round(sentiment['score'], 3)
            })

        st.subheader("🔍 Extracted Service Keywords")
        vectorizer = CountVectorizer(ngram_range=(1, 2), stop_words='english')
        X = vectorizer.fit_transform(reviews)
        phrases = vectorizer.get_feature_names_out()

        seen = set()
        unique_phrases = []
        for phrase in phrases:
            cleaned = phrase.lower().strip()
            if cleaned not in seen:
                seen.add(cleaned)
                unique_phrases.append(cleaned)

        top_keywords = unique_phrases[:15]
        if top_keywords:
            st.success("Top Extracted Keywords:")
            for kw in top_keywords:
                st.markdown(f"- {kw}")
        else:
            st.info("No keywords extracted.")

        # Prepare CSV
        df_reviews = pd.DataFrame(result_data)
        df_keywords = pd.DataFrame({"Extracted Keywords": top_keywords})

        st.subheader("📥 Download Results as Excel CSV")

        # Combine both for download
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df_reviews.to_excel(writer, sheet_name='Review Analysis', index=False)
            df_keywords.to_excel(writer, sheet_name='Keywords', index=False)
        output.seek(0)

        st.download_button(
            label="📁 Download Excel File",
            data=output,
            file_name="hotel_review_analysis.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        st.success("✅ Analysis complete and download ready!")

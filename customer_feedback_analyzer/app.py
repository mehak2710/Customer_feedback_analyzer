# customer_feedback_analyzer.py

import streamlit as st
from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Customer Feedback Analyzer", layout="centered")

st.title("🌟 Customer Feedback Analyzer")
st.write("Paste user reviews below and get insights!")

# Text input
reviews_text = st.text_area("Enter reviews (one per line):", height=200)

if reviews_text:
    reviews = reviews_text.split("\n")
    
    # Categorize reviews
    categories = []
    for review in reviews:
        review_lower = review.lower()
        if "feature" in review_lower or "add" in review_lower or "request" in review_lower:
            categories.append("Feature Request")
        else:
            polarity = TextBlob(review).sentiment.polarity
            if polarity > 0:
                categories.append("Positive")
            elif polarity < 0:
                categories.append("Negative")
            else:
                categories.append("Neutral")
    
    # Create dataframe
    df = pd.DataFrame({"Review": reviews, "Category": categories})
    st.subheader("Categorized Reviews")
    st.dataframe(df)
    
    # Count categories
    counts = df["Category"].value_counts()
    
    # Bar chart
    st.subheader("Review Categories")
    fig, ax = plt.subplots()
    counts.plot(kind='bar', color=['#2ecc71','#e74c3c','#f1c40f'], ax=ax)
    plt.ylabel("Number of Reviews")
    plt.xticks(rotation=0)
    st.pyplot(fig)
    
    # Summary
    st.subheader("Summary")
    positive_count = counts.get("Positive", 0)
    negative_count = counts.get("Negative", 0)
    feature_count = counts.get("Feature Request", 0)
    
    summary_text = f"""
    Total Reviews: {len(reviews)}
    - Positive: {positive_count}
    - Negative: {negative_count}
    - Feature Requests: {feature_count}
    """
    st.write(summary_text)


# Customer Feedback Analyzer 🌟

A simple Streamlit web app to analyze customer reviews. Users can **paste reviews**, categorize them automatically, and visualize insights with a bar chart. Ideal for product managers, UX designers, and support teams.

---

## Features

* Paste multiple reviews (one per line).
* Automatic categorization:

  * Positive
  * Negative
  * Feature Request
* Bar chart visualization of category counts.
* Table display of categorized reviews.
* Summary metrics for quick insights.

---

## Demo Screenshot

*(Your dashboard screenshot can go here — shows categorized reviews and bar chart)*

---

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/mehak2710/Customer_feedback_analyzer.git
cd Customer_feedback_analyzer/customer_feedback_analyzer
```

2. **Create a virtual environment (optional)**

```bash
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate       # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
python -m textblob.download_corpora
```

---

## Usage

1. **Run the app**

```bash
streamlit run app.py
```

2. **Paste reviews**

* Enter reviews manually, one per line.

3. **View results**

* Categorized reviews appear in a table.
* Bar chart shows counts per category.
* Summary metrics display total reviews and category counts.

---

## Project Structure

```
customer_feedback_analyzer/
│
├── customer_feedback_analyzer/
│   ├── app.py                # Main Streamlit app
│   ├── requirements.txt      # Python dependencies
│   └── README.md             # This file
```

---

## Dependencies

* Python 3.x
* Streamlit
* TextBlob
* Pandas
* Matplotlib

Install all dependencies:

```bash
pip install -r requirements.txt
```

---


## Future Enhancements

* Support for `.txt` or `.csv` file uploads.
* Interactive charts with drill-down.
* Advanced NLP for recurring themes.
* Exportable reports (PDF/Excel).
* Multi-language support.

---

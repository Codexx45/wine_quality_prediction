# 🍷 Wine Quality Predictor

A Streamlit-based web app that predicts whether a red wine sample is **Good Quality** (quality rating ≥ 7) or **Not Good**, based on its chemical properties.

---

## 🔍 Features

- ✅ Simple, intuitive web interface using Streamlit
- 🧪 Input 11 wine chemical attributes
- 📊 Predicts wine quality using a trained **Random Forest** classifier
- 🔐 Shows a confidence score to support decision-making
- 🎯 Binary classification: "Good" or "Not Good"

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/wine_quality_prediction.git
cd wine_quality_prediction
python -m venv .venv
.\.venv\Scripts\activate       # Windows
# Or: source .venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
streamlit run App.py

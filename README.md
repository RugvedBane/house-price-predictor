# California House Price Predictor 🏠

A production-deployed end-to-end machine learning web application that predicts median house prices in California based on location, housing, and demographic features.

## 🔗 Live Links
- **Frontend (Streamlit)**: https://house-price-predictor-rugved.streamlit.app
- **Backend API (FastAPI)**: https://house-price-predictor-1kl2.onrender.com/docs

> ⚠️ First request may take 30-60 seconds due to Render free tier cold start. Subsequent requests are instant.

---

## 🛠 Tech Stack

| Layer | Technology |
|---|---|
| Model | LightGBM |
| Hyperparameter Tuning | Optuna |
| Backend API | FastAPI + Uvicorn |
| Frontend | Streamlit |
| API Hosting | Render |
| Frontend Hosting | Streamlit Cloud |
| Data Processing | Scikit-learn Pipelines |

---

## ⚙️ Architecture

```
User Input (9 features)
        ↓
Streamlit Frontend
        ↓
FastAPI Backend (Render)
        ↓
Feature Engineering (3 new features created)
        ↓
Preprocessing Pipeline (impute → scale → encode)
        ↓
LightGBM Model
        ↓
Predicted House Price
```

---

## 📊 Model Performance

| Model | R² Score | RMSE |
|---|---|---|
| Random Forest (baseline) | 0.82 | $48,359 |
| LightGBM (Optuna tuned) | 0.86 | $42,772 |

LightGBM with Optuna hyperparameter tuning reduced prediction error by ~$5,600 per house compared to the baseline Random Forest model.

---

## 🔧 Feature Engineering

Three ratio features were engineered from the raw data:

| Feature | Formula |
|---|---|
| `rooms_per_household` | total_rooms / households |
| `bedrooms_per_room` | total_bedrooms / total_rooms |
| `population_per_household` | population / households |

---

## 📥 Input Features

| Feature | Type | Description |
|---|---|---|
| Longitude | float | Geographic coordinate |
| Latitude | float | Geographic coordinate |
| Housing Median Age | float | Median age of houses in block |
| Total Rooms | float | Total rooms in block |
| Total Bedrooms | float | Total bedrooms in block |
| Population | float | Block population |
| Households | float | Number of households |
| Median Income | float | Median income (×$10k) |
| Ocean Proximity | string | Distance category from ocean |

---

## 🚀 How It Works

1. User enters house features on the Streamlit frontend
2. Frontend sends a POST request to the FastAPI backend on Render
3. Backend performs feature engineering and preprocessing
4. LightGBM model returns a predicted house price
5. Prediction is displayed on the frontend

---

## 📁 Project Structure

```
├── api.py              # FastAPI backend
├── app.py              # Streamlit frontend
├── lgbm_model.pkl      # Trained LightGBM model
├── pipeline.pkl        # Preprocessing pipeline
└── requirements.txt    # Dependencies
```

# California House Price Predictor 🏠

A production-deployed machine learning web app that predicts California house prices.

## 🔗 Live Links
- **Frontend**: https://house-price-predictor-rugved.streamlit.app
- **API**: https://house-price-predictor-1kl2.onrender.com/docs

## 🛠 Tech Stack
- **Model**: LightGBM (R² = 0.86, RMSE = ~42,700)
- **Tuning**: Optuna hyperparameter optimization
- **Backend**: FastAPI deployed on Render
- **Frontend**: Streamlit deployed on Streamlit Cloud

## ⚙️ Architecture
User Input → Streamlit Frontend → FastAPI Backend → LightGBM Model → Prediction

## 📊 Model Performance
| Model | R² | RMSE |
|---|---|---|
| Random Forest (baseline) | 0.82 | 48,359 |
| LightGBM (tuned) | 0.86 | 42,772 |

## 🔧 Features
- Stratified train-test split
- Feature engineering (rooms per household, bedrooms per room, population per household)
- Full preprocessing pipeline (imputation, scaling, encoding)
- REST API with Pydantic validation

## ⚠️ Note
First request may take 30-60 seconds due to Render free tier cold start.

# Health Insurance Premium Prediction

This project is a **Health Insurance Premium Prediction** tool built using **Streamlit** and **XGBoost**. It estimates insurance premiums based on user inputs such as age, BMI, smoking status, region, and medical history.

## 📌 Features
- Predicts health insurance premium based on various factors.
- Uses an optimized XGBoost model.
- Streamlit-based interactive UI for easy use.
- Ensures consistent preprocessing between training and prediction.

## 🛠 Installation
### 1. Clone the repository
```sh
git clone https://github.com/TanmayDhamnaskar/insurance-premium-prediction
cd insurance-premium-prediction
```

### 2. Create a virtual environment (recommended)
```sh
python3 -m venv st_env
source st_env/bin/activate  # On Windows: st_env\Scripts\activate
```

### 3. Install dependencies
```sh
pip install -r requirements.txt
```

## 🚀 Running the Streamlit App
```sh
streamlit run app.py
```

## 📂 Project Structure
```
Streamlit_Premium_Prediction/
│── app.py                                             # Main Streamlit app
│── optimized_xgb_pipeline.pkl                         # Initial XGBoost model
│── optimized_xgb_pipeline_fixed.pkl                   # Fixed version of the model
│── requirements.txt                                   # Dependencies
│── InsurancePricePrediction(eda).ipynb                # Statistical Analysis(EDA)
│── InsurancePricePrediction(Model_Pipeline_ML).ipynb  # Hypertuned Model pipeline
└── st_env/                                            # Virtual environment (optional)
```

## 🏗 Model Details
- Model: **XGBoost Regressor**
- Objective: **Predict insurance premium based on user details**
- Features used:
  - Age, Gender, BMI, Smoking Status, Region
  - Medical & Family History, Exercise Frequency, Occupation, Coverage Level
- Log transformation applied for target variable

## 📑 Notes
- Ensure the `optimized_xgb_pipeline.pkl` file is present in the project directory.
- For batch processing, consider modifying the script to accept CSV input.
- Future improvements can include adding more features and enhancing model accuracy.



---
💡 *Built with Streamlit & XGBoost*


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
│── app.py                                     # Main Streamlit app
│── eda_analysis.ipynb                         # Statistical Analysis(EDA)
│── model_pipeline.ipynb                       # Hypertuned Model pipeline 
│── optimized_xgb_pipeline.pkl                 # XGBoost model
│── README.md                                  # Project documentation
│── requirements.txt                           # Dependencies
└── st_env/                                    # Virtual environment (optional)
```

## 🏗 Model Details
- Model: **XGBoost Regressor**
- Objective: **Predict insurance premium based on user details**
- Features used:
  - Age, Gender, BMI, Smoking Status, Region
  - Medical & Family History, Exercise Frequency, Occupation, Coverage Level
- **Log transformation applied to the target variable:** A log transformation is applied to the target variable (insurance premium) to stabilize the variance and improve model performance. After the model makes predictions, the results are converted back to the original scale (i.e., from log-transformed predictions to the actual premium amounts).

## 📑 Notes
- Ensure the `optimized_xgb_pipeline.pkl` file is present in the project directory.
- For batch processing, consider modifying the script to accept CSV input.
- Future improvements can include adding more features and enhancing model accuracy.

## 📘 Alignment with Project Guidelines

- ✅ **Data Source:** Used the `Insurance_Prediction` table from `Database.db`
- ✅ **Record Split:** 
  - 700,000 records used for training
  - 200,000 records used for evaluation
  - 100,000 records considered as live data (via app interface)
- ✅ **Consistent Preprocessing:** The same preprocessing steps are applied during training and prediction using a saved pipeline (`optimized_xgb_pipeline.pkl`)
- ✅ **Model Evaluation Metrics:**
  - RMSE, MAE, and R² evaluated and explained in notebook `model_pipeline.ipynb`
- ✅ **Model Used:** XGBoost Regressor (with hyperparameter tuning)
- ✅ **User Interface:** Streamlit-based real-time prediction app
- ✅ **Deployment Ready:** Can be extended for batch processing or API-based use

> 📬 This project demonstrates end-to-end implementation from data analysis to deployment, meeting all required specifications.



---
💡 *Built with Streamlit & XGBoost*


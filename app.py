
import streamlit as st
import joblib
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.base import BaseEstimator, RegressorMixin

# Define the custom wrapper class
class LogToOriginalXGBRegressor(BaseEstimator, RegressorMixin):
    def __init__(self, base_model=None):
        self.base_model = base_model if base_model else xgb.XGBRegressor(objective="reg:squarederror", random_state=42)

    def fit(self, X, y):
        self.base_model.fit(X, y)
        return self

    def predict(self, X):
        log_preds = self.base_model.predict(X)
        return np.expm1(log_preds)  # Convert back to original scale

# Load the corrected model
try:
    model_pipeline = joblib.load("optimized_xgb_pipeline_fixed.pkl")
    st.success("Model loaded successfully!")
except Exception as e:
    st.error(f"Error loading model: {e}. Make sure 'optimized_xgb_pipeline_fixed.pkl' is in the same directory.")
    st.stop()



# Streamlit UI components follow...


# Streamlit UI
st.title("🏥 Health Insurance Premium Prediction")
st.write("Enter your details to estimate your health insurance premium.")

# Sidebar Input
st.sidebar.header("User Input")

age = st.sidebar.number_input("Age", min_value=18, max_value=65, value=30)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
bmi = st.sidebar.number_input("BMI (Body Mass Index)", min_value=10.0, max_value=50.0, value=25.0)
smoker = st.sidebar.selectbox("Smoker Status", ["Yes", "No"])
region = st.sidebar.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])
medical_history = st.sidebar.selectbox("Medical History", ["Diabetes", "No Disease", "High blood pressure", "Heart disease"])
family_medical_history = st.sidebar.selectbox("Family Medical History", ["No Disease", "High blood pressure", "Diabetes", "Heart disease"])
exercise_frequency = st.sidebar.selectbox("Exercise Frequency", ["Never", "Occasionally", "Rarely", "Frequently"])
occupation = st.sidebar.selectbox("Occupation", ["Blue collar", "White collar", "Student", "Unemployed"])
coverage_level = st.sidebar.selectbox("Coverage Level", ["Basic", "Standard", "Premium"])

# Predict button
if st.sidebar.button("Predict Premium"):
    # Create DataFrame for input
    input_data = pd.DataFrame({
        "age": [age],
        "gender": [gender.lower()],  # Ensure consistency with training data
        "bmi": [bmi],
        "smoker": [smoker.lower()],
        "region": [region.lower()],
        "medical_history": [medical_history],
        "family_medical_history": [family_medical_history],
        "exercise_frequency": [exercise_frequency],
        "occupation": [occupation],
        "coverage_level": [coverage_level]
    })

    # Make Prediction
    try:
        predicted_charges = model_pipeline.predict(input_data)[0]
        st.success(f"💰 Estimated Insurance Premium: **${predicted_charges:,.2f}**")
    except Exception as e:
        st.error(f"Error making prediction: {e}")

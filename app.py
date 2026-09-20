
import streamlit as st
import pandas as pd
import pickle

# Page configuration
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰"
)

# Load the trained model
with open("loan_approval_model.pkl", "rb") as file:
    model = pickle.load(file)

# Application title
st.title("Loan Approval Prediction")
st.subheader("[Decision Tree]")

st.write("Enter applicant details to predict loan approval.")

# Input fields
income = st.number_input(
    "Income",
    min_value=0.0,
    value=50000.0,
    step=1000.0
)

credit_score = st.number_input(
    "Credit Score",
    min_value=0.0,
    max_value=1000.0,
    value=720.0,
    step=1.0
)

# Prediction button
if st.button("Predict Loan Approval"):

    # Prepare input data
    input_data = pd.DataFrame({
        "Income": [income],
        "Credit_Score": [credit_score]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display result
    if str(prediction).strip().lower() in ["1", "yes", "approved", "true"]:
        st.success("LOAN APPROVED")
    else:
        st.error("LOAN NOT APPROVED")

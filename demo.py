import streamlit as st
import pandas as pd
import numpy as np
import joblib  # For loading the model

# Load trained model (ensure you have a trained model saved as 'model.pkl')
def load_model():
    try:
        model = joblib.load('final_models/model.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Define feature columns
FEATURES = [
    "having_IP_Address", "URL_Length", "Shortining_Service", "having_At_Symbol", "double_slash_redirecting", 
    "Prefix_Suffix", "having_Sub_Domain", "SSLfinal_State", "Domain_registeration_length", "Favicon", "port", 
    "HTTPS_token", "Request_URL", "URL_of_Anchor", "Links_in_tags", "SFH", "Submitting_to_email", "Abnormal_URL", 
    "Redirect", "on_mouseover", "RightClick", "popUpWidnow", "Iframe", "age_of_domain", "DNSRecord", "web_traffic", 
    "Page_Rank", "Google_Index", "Links_pointing_to_page", "Statistical_report"
]

# Streamlit UI
def main():
    st.title("Phishing Website Detection")
    st.write("Enter website attributes to predict whether it is legitimate or phishing.")

    # Input fields for features
    input_data = {}
    for feature in FEATURES:
        input_data[feature] = st.number_input(feature, min_value=-1, max_value=1, value=0, step=1)
    
    # Convert input to DataFrame
    input_df = pd.DataFrame([input_data])

    # Load model
    model = load_model()

    if model and st.button("Predict"):
        prediction = model.predict(input_df)
        result = "Phishing Website" if prediction[0] == -1 else "Legitimate Website"
        st.success(f"Prediction: {result}")

if __name__ == "__main__":
    main()

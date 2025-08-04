import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open("area.pkl", "rb"))

# Define the main function
def predict_price():
    st.title("Area land Predictor")

    # Take area input from user
    area = st.number_input("Enter the area in square feet:")

    # Predict button
    if st.button("Predict"):
        prediction = model.predict([[area]])
        st.success(f"The predicted price for the area is: ₹{prediction[0]:,.2f}")

# Call the function to run the app
predict_price()

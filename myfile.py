import pickle
import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# ── Load Model ─────────────────────────────────────────────
model = pickle.load(open("area.pkl", "rb"))

# ── File Path ──────────────────────────────────────────────
file_path = "data.csv"

# ── Default Training Data ──────────────────────────────────
TRAINING_DATA = pd.DataFrame({
    "area": [2600, 3000, 3200, 3600, 4000],
    "price": [550000, 565000, 610000, 680000, 725000]
})

# Create CSV if not exists
if not os.path.exists(file_path):
    TRAINING_DATA.to_csv(file_path, index=False)

# Load data safely
try:
    data = pd.read_csv(file_path)

    # Fix headers if broken
    if "area" not in data.columns or "price" not in data.columns:
        data.columns = ["area", "price"]

except Exception as e:
    st.error(f"Could not load data: {e}")
    data = TRAINING_DATA.copy()

# ── App Config ─────────────────────────────────────────────
st.set_page_config(
    page_title="Land Price Predictor",
    page_icon="🏡",
    layout="centered"
)

# ── Title ──────────────────────────────────────────────────
st.title("🏡 Land Price Predictor")
st.markdown("Predict land price using Machine Learning 📊")
st.markdown("---")

# ── Sidebar ────────────────────────────────────────────────
st.sidebar.header("⚙️ Options")

save_data = st.sidebar.checkbox("Save prediction to dataset")

show_table = st.sidebar.checkbox("Show dataset table")

# ── Quick Stats ────────────────────────────────────────────
if not data.empty:

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "📉 Min Price",
        f"₹{data['price'].min():,.0f}"
    )

    col2.metric(
        "📈 Max Price",
        f"₹{data['price'].max():,.0f}"
    )

    col3.metric(
        "📊 Total Records",
        len(data)
    )

# ── Input Section ──────────────────────────────────────────
st.subheader("🏠 Enter Property Details")

area = st.number_input(
    "Enter Area (sq ft):",
    min_value=100.0,
    step=100.0,
    value=2600.0
)

# ── Prediction Button ──────────────────────────────────────
if st.button("Predict 💰"):

    if area <= 0:
        st.warning("Please enter valid area!")

    else:

        # Predict price
        prediction = model.predict(np.array([[area]]))[0]

        # Display prediction
        st.success(f"Predicted Price: ₹{prediction:,.2f}")

        st.info(f"📊 Price per sq.ft: ₹{prediction / area:.2f}")

        # Save data if checked
        if save_data:

            try:

                new_data = pd.DataFrame({
                    "area": [area],
                    "price": [prediction]
                })

                new_data.to_csv(
                    file_path,
                    mode='a',
                    header=False,
                    index=False
                )

                st.success("✅ Prediction saved successfully!")

                # Reload updated data
                data = pd.read_csv(file_path)

            except Exception as e:
                st.error(f"Error saving data: {e}")

# ── Graph Section ──────────────────────────────────────────
st.subheader("📈 Area vs Price Graph")

if not data.empty and "area" in data.columns:

    fig, ax = plt.subplots(figsize=(8, 5))

    # Scatter Plot
    ax.scatter(
        data["area"],
        data["price"],
        color="blue",
        label="Dataset"
    )

    # Regression Line
    x_range = np.linspace(
        data["area"].min(),
        data["area"].max(),
        100
    )

    y_range = model.predict(x_range.reshape(-1, 1))

    ax.plot(
        x_range,
        y_range,
        color="red",
        linewidth=2,
        label="Regression Line"
    )

    # Current Prediction Point
    if area > 0:

        current_prediction = model.predict(
            np.array([[area]])
        )[0]

        ax.scatter(
            area,
            current_prediction,
            color="green",
            s=150,
            label="Current Prediction"
        )

    # Labels & Styling
    ax.set_xlabel("Area (sq ft)")
    ax.set_ylabel("Price (₹)")
    ax.set_title("Land Price Prediction")

    ax.legend()

    ax.grid(True)

    st.pyplot(fig)

else:
    st.warning("No valid data available!")

# ── Dataset Table ──────────────────────────────────────────
if show_table:

    st.subheader("📋 Dataset Preview")

    st.dataframe(data)

# ── Footer ─────────────────────────────────────────────────
st.markdown("---")

st.caption("Made by Pranjal Srivastava 🚀")

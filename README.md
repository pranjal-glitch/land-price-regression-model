# Land Price Predictor on Area

This is a Streamlit-based machine learning app that predicts land prices based on area using a simple linear regression model.

## 🔧 Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib
- Streamlit

## 🚀 How to Run

1. Clone the repository or download the files
2. Install required libraries:(pip install -r requirements.txt)
3. Run the app:(streamlit run app.py)

 Files Included
- `app.py`: Streamlit app
- `area.pkl`: Trained regression model
- `requirements.txt`: Python dependencies


REGRESSION PLOT PNG
%matplotlib inline
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# Load trained model
with open('area.pkl', 'rb') as f:
    model = pickle.load(f)

# Actual dataset
data = {
    'area': [2600, 3000, 3200, 3600, 4000],
    'price': [550000, 565000, 610000, 680000, 725000]
}
df = pd.DataFrame(data)

# Predict
X = df[['area']]
y_pred = model.predict(X)

# Plot
plt.scatter(df['area'], df['price'], color='blue', label='Actual Data')
plt.plot(df['area'], y_pred, color='red', label='Regression Line')

plt.xlabel("Area (sq.ft)")
plt.ylabel("Price (INR)")
plt.title("Land Area vs Price - Regression Plot")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("regression_plot.png")  # Saves it to your working folder
plt.show()  # Shows it in the notebook




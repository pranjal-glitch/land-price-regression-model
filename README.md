# 🏡 Land Price Predictor using Machine Learning

A Streamlit-based Machine Learning web application that predicts land prices based on area using a **Linear Regression Model**.

---
## 📌 Features

* Predict land price instantly
* Dynamic regression graph visualization
* Interactive Streamlit web interface
* Save predictions to dataset
* Visualize training data and prediction points
---
## 🛠️ Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib
---

## 📂 Project Structure

```bash
land-price-regression-model/
│
├── myfile.py            # Main Streamlit application
├── area.pkl             # Trained Linear Regression model
├── data.csv             # Dataset storage
├── requirements.txt     # Required libraries
├── README.md            # Project documentation
```

---

## 📊 Machine Learning Model

This project uses **Linear Regression** to predict land prices based on land area.

### Training Dataset

| Area (sq ft) | Price (₹) |
| ------------ | --------- |
| 2600         | 550000    |
| 3000         | 565000    |
| 3200         | 610000    |
| 3600         | 680000    |
| 4000         | 725000    |

The model learns the relationship using:

```math
y = mx + b
```

Where:

* `x` = Area
* `y` = Predicted Price
* `m` = Slope
* `b` = Intercept

---

## 🚀 How to Run the Project

### 1️⃣ Clone Repository

```bash
git clone https://github.com/pranjal-glitch/land-price-regression-model.git
```

---

### 2️⃣ Open Project Folder

```bash
cd land-price-regression-model
```

---

### 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Streamlit App

```bash
streamlit run myfile.py
```

---

## 📈 Graph Visualization

The app dynamically displays:

* Dataset points
* Regression line
* Current prediction point

using Matplotlib.

---

## 🧠 Future Improvements

* Add larger datasets
* Improve UI/UX
* Add location-based prediction
* Deploy online using Streamlit Cloud
* Add advanced ML models

---

## 👨‍💻 Author

**Pranjal Srivastava**
B.Tech CSE Student | Data Science Enthusiast | ML Learner 🚀

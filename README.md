<!-- # Lasso-Regression

<img width="1900" height="905" alt="image" src="https://github.com/user-attachments/assets/7dcf124b-88fb-479e-8940-39fc8bbacb1e" /> -->

## Final Grade Predictor – Lasso Regression Model

This project uses Lasso Regression, a linear regression technique with L1 regularization, to predict a student's final academic grade (G3). The project includes a clean, interactive Flask web interface where users can input student characteristics and get real-time predictions.
---

## What is Lasso Regression?

Lasso (Least Absolute Shrinkage and Selection Operator) regression helps in feature selection by shrinking less important feature coefficients to zero, making it ideal for high-dimensional datasets with irrelevant or redundant variables.

---

##  Project Structure
```
Lasso-Regression/
├── app.py                   # Flask application to serve predictions
├── train_model.py           # Model training script using Lasso Regression
├── model.pkl                # Saved Lasso model
├── encoders.pkl             # Encoders for categorical features
├── student_data.csv         # Dataset used for training
│
├── templates/
│   └── index.html           # Web form for user input

```
---

##  Setup Instructions

1. **Clone the repository**

```
git clone https://github.com/Digvijay4252/Lasso-Regression.git
cd Lasso-Regression
```
Install dependencies
```
pip install -r requirements.txt
```
Run the application
```
python app.py
```
Open in browser

Visit: http://localhost:10000

## Screenshots
<img width="1900" height="905" alt="image" src="https://github.com/user-attachments/assets/7dcf124b-88fb-479e-8940-39fc8bbacb1e" />

## Future Improvements
Include prediction confidence or error margin

Add charts (e.g., feature importance, residuals)

Export prediction history

Enable CSV batch uploads


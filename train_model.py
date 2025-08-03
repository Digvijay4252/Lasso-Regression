import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import LabelEncoder
import joblib

# Load dataset
data = pd.read_csv('startup_funding.csv')

# Encode categorical column 'State'
le_state = LabelEncoder()
data['State'] = le_state.fit_transform(data['State'])

# Features and target
X = data[['R&D_Spend', 'Administration', 'Marketing_Spend', 'State']]
y = data['Profit']

# Train Lasso Regression model
model = Lasso(alpha=0.1)
model.fit(X, y)

# Save model and encoder
joblib.dump(model, 'model.pkl')
joblib.dump(le_state, 'state_encoder.pkl')

print("Lasso Regression model and encoder saved.")

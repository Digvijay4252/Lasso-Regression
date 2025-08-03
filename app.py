from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model and label encoder
model = joblib.load('model.pkl')
state_encoder = joblib.load('state_encoder.pkl')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        try:
            rd_spend = float(request.form['rd_spend'])
            admin = float(request.form['administration'])
            marketing = float(request.form['marketing_spend'])
            state = request.form['state']

            # Encode state
            state_encoded = state_encoder.transform([state])[0]

            # Prediction
            features = [[rd_spend, admin, marketing, state_encoded]]
            profit = model.predict(features)[0]
            prediction = f"${profit:,.2f}"

        except Exception as e:
            prediction = f"Error: {e}"

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

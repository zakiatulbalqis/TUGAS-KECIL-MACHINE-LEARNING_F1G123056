from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

# Load model & scaler
scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        lag1       = float(data['lag1'])
        lag2       = float(data['lag2'])
        lag3       = float(data['lag3'])
        ma5        = float(data['ma5'])
        ma10       = float(data['ma10'])
        ma20       = float(data['ma20'])
        std20      = float(data['std20'])
        volatility = float(data['volatility'])

        features = np.array([[lag1, lag2, lag3, ma5, ma10, ma20, std20, volatility]])
        scaled   = scaler.transform(features)
        pred     = model.predict(scaled)[0]

        # Hitung perubahan dari harga kemarin
        change    = pred - lag1
        change_pct = (change / lag1) * 100

        return jsonify({
            'success': True,
            'prediction': round(float(pred), 2),
            'change': round(float(change), 2),
            'change_pct': round(float(change_pct), 4),
        })
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5050))
    app.run(host="0.0.0.0", port=port)
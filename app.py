from flask import Flask, render_template, request
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load your trained model
MODEL_PATH = "rf_ids_modelv1.pkl"
model = joblib.load(MODEL_PATH)

# Define the same feature order as used during training
feature_columns = [
    "dur", "proto", "service", "state",
    "spkts", "dpkts", "sbytes", "dbytes",
    "sttl", "dttl", "sload", "dload", 
    "tcprtt", "synack", "ackdat", "ct_state_ttl"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form values from user input
        form_values = []
        for f in feature_columns:
            val = request.form.get(f, "")
            # Handle categorical input for proto/service/state
            if f in ["proto", "service", "state"]:
                val = hash(val) % 100  # simple hash encoding for categorical
            else:
                val = float(val) if val else 0.0
            form_values.append(val)

        # Convert to numpy array
        data = np.array(form_values).reshape(1, -1)

        # Make prediction
        prediction = model.predict(data)[0]
        result = "🚨 Attack Detected" if prediction == 1 else "✅ Normal Traffic"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)

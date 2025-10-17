# app.py
from flask import Flask, request, jsonify
from features.feature_extractor import extract_features_for_path
from features.logistic_regression import LogisticRegressionGD
import numpy as np
import os

app = Flask(__name__)

# Load trained model parameters
model_data = np.load("models/logreg_demo.npz", allow_pickle=True)
w, b, mu, sigma = model_data["w"], model_data["b"], model_data["mu"], model_data["sigma"]

model = LogisticRegressionGD()
model.w = w
model.b = b

@app.route("/analyze", methods=["POST"])
def analyze_image():
    if "file" not in request.files:
        return jsonify({"error": "No file provided"}), 400
    file = request.files["file"]
    temp_path = "temp_input.png"
    file.save(temp_path)

    feats = extract_features_for_path(temp_path)
    X = (feats - mu) / sigma
    pred = model.predict(X.reshape(1, -1))[0]
    label = "AI-generated" if pred == 1 else "Real"
    os.remove(temp_path)
    return jsonify({"result": label})

if __name__ == "__main__":
    app.run(debug=True)
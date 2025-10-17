from flask import Flask, request, jsonify
from flask_cors import CORS
from features.feature_extractor import extract_features_for_path
from features.logistic_regression import LogisticRegressionGD
import numpy as np
import os

app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/*": {"origins": "*"}})


# Load trained model parameters
model_data = np.load("models/logreg_demo.npz", allow_pickle=True)
w, b, mu, sigma = model_data["w"], model_data["b"], model_data["mu"], model_data["sigma"]

model = LogisticRegressionGD()
model.w = w
model.b = b

@app.route("/predict", methods=["POST", "OPTIONS"])
def analyze_image():
    if request.method == "OPTIONS":
        return '', 204

    try:
        if "image" not in request.files:
            return jsonify({"error": "No image uploaded"}), 400

        file = request.files["image"]
        temp_path = "temp_input.png"
        file.save(temp_path)

        feats = extract_features_for_path(temp_path)
        X = (feats - mu) / sigma
        pred = model.predict(X.reshape(1, -1))[0]
        label = "AI-generated" if pred == 1 else "Real"
        confidence = float(model.sigmoid(np.dot(X, model.w) + model.b))
        top_indices = np.argsort(np.abs(model.w))[-5:][::-1]
        top_features = [{'name': f'Feature {i}', 'weight': float(model.w[i])} for i in top_indices]

        return jsonify({
            "label": label,
            "confidence": float(confidence * 100),
            "top_features": top_features
        })

    except Exception as e:
        return jsonify({"error": "Internal server error"}), 500

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

if __name__ == "__main__":
    app.run(debug=True)
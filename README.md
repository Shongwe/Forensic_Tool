# 🕵️‍♂️ AI Fingerprint Detector

A forensic-grade tool for detecting synthetic media using handcrafted features and interpretable machine learning. Designed for transparency, auditability, and academic integration.

---

## Features

- **Handcrafted Feature Extraction**  
  Extracts 50 forensic descriptors including color moments, noise residuals, DCT statistics, gradient metrics, and LBP histograms.

- **Interpretable Logistic Regression Model**  
  Lightweight model trained with gradient descent, exposing top contributing features per prediction.

- **Confidence & Feature Attribution**  
  Each prediction includes a confidence score and ranked feature weights for forensic traceability.

- **Web Interface**  
  Upload images and receive real-time predictions with visualized feature contributions.

---

## How It Works

1. **Upload an image** via the frontend.
2. **Backend extracts features** using `features/feature_extractor.py`.
3. **Features are normalized** using stored mean and std (`logreg_demo.npz`).
4. **Prediction is made** using a logistic regression model (`logistic_regression.py`).
5. **Top features are returned** with descriptive labels and weights.

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/your-username/ai-fingerprint-detector.git
cd ai-fingerprint-detector

### 2. Set up the backend
```bash
cd Backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python App.py

### 4. Launch the frontend
cd ../Frontend
npm install
npm start

 ## Model Details
• 	Type: Logistic Regression (custom gradient descent)
• 	Input: 50-dimensional feature vector
• 	Training: Normalized features, binary labels (Real vs AI-generated)
• 	Output: Label, confidence, top 5 contributing feature

## Project Structure
├── Backend/
│   ├── App.py
│   ├── models/logreg_demo.npz
│   ├── features/
│   │   ├── feature_extractor.py
│   │   └── logistic_regression.py
│   └── requirements.txt
├── Frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   └── App.js
│   └── package.json






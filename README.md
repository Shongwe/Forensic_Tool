# IT08X27 – Computer Forensics 2025

**AI Fingerprint Detector**
**University of Johannesburg – Academy of Computer Science & Software Engineering**

This repository contains the research, design, and implementation of a forensic tool developed for the IT08X27 Honours module. The project, titled **"Dust for AI Fingerprints"**, investigates the challenge of identifying and attributing AI-generated media in a post-truth digital landscape.

---


## Problem Statement

In an era where synthetic media is indistinguishable from authentic content, forensic investigators face growing difficulty in tracing the origin of manipulated or AI-generated assets. The lack of visible tamper evidence and the sophistication of generative models pose a serious challenge to digital authenticity and legal attribution.

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
```

### 2. Set up the backend
```bash
cd Backend
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python App.py
```
### 4. Launch the frontend
```bash
cd ../Frontend
npm install
npm start
```
 ## Model Details
• 	Type: Logistic Regression (custom gradient descent)
• 	Input: 50-dimensional feature vector
• 	Training: Normalized features, binary labels (Real vs AI-generated)
• 	Output: Label, confidence, top 5 contributing feature

## Project Structure
```bash
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
```

## License
This project is for academic and research purposes only. Unauthorized use or distribution is prohibited.


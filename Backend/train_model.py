import numpy as np
import os
from glob import glob
from features.feature_extractor import extract_features_for_path
from features.logistic_regression import LogisticRegressionGD

# --------------------------------------------------------
# CONFIGURATION
# --------------------------------------------------------
REAL_DIR = "data/real_images"
AI_DIR = "data/ai_generated"
MODEL_PATH = "models/logreg_demo.npz"
os.makedirs("models", exist_ok=True)

# --------------------------------------------------------
# 1. LOAD DATASET
# --------------------------------------------------------
X, y = [], []

def load_images_from_folder(folder, label):
    # Include .jpg, .jpeg, and .png formats
    image_files = glob(os.path.join(folder, "*.jpg")) \
                + glob(os.path.join(folder, "*.jpeg")) \
                + glob(os.path.join(folder, "*.png"))

    for path in image_files:
        try:
            feats = extract_features_for_path(path)
            X.append(feats)
            y.append(label)
        except Exception as e:
            print(f" Skipping {path}: {e}")

print(" Loading images...")
load_images_from_folder(REAL_DIR, 0)  # label 0 = real
load_images_from_folder(AI_DIR, 1)    # label 1 = AI-generated

X = np.array(X)
y = np.array(y)
print(f" Loaded {len(y)} samples: {sum(y==0)} real, {sum(y==1)} AI-generated")

if len(X) == 0:
    raise RuntimeError(" No data found. Please ensure you have images in both folders!")

# --------------------------------------------------------
# 2. NORMALIZE FEATURES
# --------------------------------------------------------
mu = X.mean(axis=0)
sigma = X.std(axis=0) + 1e-9
Xn = (X - mu) / sigma

# --------------------------------------------------------
# 3. SPLIT TRAIN / TEST
# --------------------------------------------------------
np.random.seed(42)
indices = np.arange(len(Xn))
np.random.shuffle(indices)
split = int(0.8 * len(indices))
train_idx, test_idx = indices[:split], indices[split:]
X_train, X_test = Xn[train_idx], Xn[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

# --------------------------------------------------------
# 4. TRAIN MODEL
# --------------------------------------------------------
print("\n Training Logistic Regression Model...")
model = LogisticRegressionGD(lr=0.3, epochs=800)
model.fit(X_train, y_train)

# --------------------------------------------------------
# 5. EVALUATE MODEL
# --------------------------------------------------------
preds = model.predict(X_test)
acc = (preds == y_test).mean() * 100
print(f"\n Accuracy on test set: {acc:.2f}%")

# --------------------------------------------------------
# 6. SAVE MODEL
# --------------------------------------------------------
np.savez(MODEL_PATH, w=model.w, b=model.b, mu=mu, sigma=sigma)
print(f"Model saved at: {MODEL_PATH}")

# logistic_regression.py
import numpy as np

class LogisticRegressionGD:
    def __init__(self, lr=0.5, epochs=1000, l2=1e-4):
        self.lr = lr
        self.epochs = epochs
        self.l2 = l2

    def sigmoid(self, z):
        return 1.0 / (1.0 + np.exp(-z))

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.w = np.zeros(n_features, dtype=np.float32)
        self.b = 0.0
        for epoch in range(self.epochs):
            z = X.dot(self.w) + self.b
            pred = self.sigmoid(z)
            error = pred - y
            grad_w = (X.T.dot(error) / n_samples) + self.l2 * self.w
            grad_b = error.mean()
            self.w -= self.lr * grad_w
            self.b -= self.lr * grad_b
            if epoch % 200 == 0:
                loss = -np.mean(y*np.log(pred+1e-9) + (1-y)*np.log(1-pred+1e-9))
                print(f"Epoch {epoch} | Loss: {loss:.6f}")

    def predict_proba(self, X):
        return self.sigmoid(X.dot(self.w) + self.b)

    def predict(self, X, thresh=0.5):
        return (self.predict_proba(X) >= thresh).astype(int)

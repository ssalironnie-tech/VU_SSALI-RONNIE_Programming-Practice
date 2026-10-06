# ==========================================
# Topic 7: Scikit-learn Supervised Learning
# ==========================================

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# --- Data Generation ---
X, y = make_classification(n_samples=200, n_features=4, random_state=42)

# --- Train-Test Split ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Model Building (Supervised Machine Learning) ---
model = LogisticRegression()
model.fit(X_train, y_train)

# --- Evaluation ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
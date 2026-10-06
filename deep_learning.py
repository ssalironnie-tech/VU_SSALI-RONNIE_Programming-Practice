# ==========================================
# Topic 8: TensorFlow / Neural Network Basics
# ==========================================

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

# --- Synthetic Data Creation ---
# Learning a simple relationship: y = 2x - 1
X_data = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
y_data = np.array([-3.0, -1.0, 1.0, 3.0, 5.0, 7.0], dtype=float)

# --- Building Neural Network Model ---
model = Sequential([
    Dense(units=1, input_shape=[1])
])

model.compile(optimizer='sgd', loss='mean_squared_error')

# --- Training Deep Learning Model ---
print("Training Neural Network...")
model.fit(X_data, y_data, epochs=100, verbose=0)

# --- Prediction ---
prediction = model.predict(np.array([[10.0]]))
print(f"Deep Learning Prediction for X=10 (Expected ~19.0): {prediction[0][0]:.2f}")
# ==========================================
# Topic 6: NumPy, Pandas, Matplotlib & Seaborn
# ==========================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- 1. NumPy Array Operations ---
data_array = np.array([10, 20, 30, 40, 50])
print("NumPy Array Mean:", np.mean(data_array))
print("NumPy Array Standard Deviation:", np.std(data_array))

# --- 2. Pandas Data Manipulation ---
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [85, 92, 78, 88],
    'Passed': [True, True, True, True]
}
df = pd.DataFrame(data)
print("\n--- Pandas DataFrame ---")
print(df)

# --- 3. Visualization ---
plt.figure(figsize=(6, 4))
sns.barplot(x='Student', y='Score', data=df, palette='Blues_d')
plt.title('Student Scores Overview')
plt.xlabel('Student Name')
plt.ylabel('Score')
plt.tight_layout()

# Save plot to disk
plt.savefig('scores_visualization.png')
print("\nVisualization plot saved as 'scores_visualization.png'")
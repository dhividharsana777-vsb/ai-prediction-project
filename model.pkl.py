import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# Sample dataset (you can change values)
# Features: [Study Hours, Sleep Hours, Attendance]
X = np.array([
    [2, 6, 60],
    [3, 7, 65],
    [4, 6, 70],
    [5, 7, 75],
    [6, 8, 80],
    [7, 7, 85],
    [8, 8, 90]
])

# Target (Marks / Performance)
y = np.array([40, 50, 55, 65, 70, 80, 90])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
pickle.dump(model, open('model.pkl', 'wb'))

print("Model trained and saved as model.pkl ✅")

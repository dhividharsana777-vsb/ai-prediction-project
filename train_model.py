import numpy as np
from sklearn.linear_model import LinearRegression
import pickle

# sample data
X = np.array([[1,2,3],[2,3,4],[3,4,5]])
y = np.array([6,9,12])

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open('model.pkl', 'wb'))

print("Model created!")
import numpy as np
import matplotlib.pyplot as plt

# Generate sample data (simulating y = 3x + 5 with some noise)
np.random.seed(42)
X = np.random.rand(100, 1) * 10  # Random values between 0 and 10
y = 3 * X + 5 + np.random.randn(100, 1) * 2  # y = 3x + 5 + noise

# Initialize parameters
m = 0  # Slope (weight)
b = 0  # Intercept (bias)
learning_rate = 0.01
epochs = 1000  # Number of iterations

n = len(X)  # Number of samples

# Gradient Descent Algorithm
for _ in range(epochs):
    y_pred = m * X + b  # Predictions
    loss = np.mean((y_pred - y) ** 2)  # Mean Squared Error (MSE)

    # Compute gradients
    dm = -(2/n) * np.sum(X * (y - y_pred))  # Derivative w.r.t. m
    db = -(2/n) * np.sum(y - y_pred)  # Derivative w.r.t. b

    # Update parameters
    m -= learning_rate * dm
    b -= learning_rate * db

# Print final learned parameters
print(f"Final equation: y = {m:.2f}x + {b:.2f}")

# Plot data and regression line
plt.scatter(X, y, color="blue", label="Data points")
plt.plot(X, m * X + b, color="red", label="Regression line")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

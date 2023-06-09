from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

import numpy as np
import matplotlib.pyplot as plt

def linear_least_squares(x, y):
    n = len(x)
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_x_squared = np.sum(x**2)
    sum_xy = np.sum(x * y)

    # Calculate the slope (m) and intercept (c) of the linear equation
    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept

# Example usage:
x = np.array([1, 2, 3, 4, 5])  # Data points x-coordinates
y = np.array([3, 5, 7, 9, 11])  # Data points y-coordinates

# Calculate x squared and xy
x_squared = x**2
xy = x * y

# Calculate the sums
sum_x = np.sum(x)
sum_y = np.sum(y)
sum_x_squared = np.sum(x_squared)
sum_xy = np.sum(xy)

# Print the table
print("Data Points:")
print(" x   |   y   | x^2  |  xy  ")
print("-----------------------------")
for i in range(len(x)):
    print(f"{x[i]:.2f} | {y[i]:.2f} | {x_squared[i]:.2f} | {xy[i]:.2f}")
print("-----------------------------")
print(f"Sum  | {sum_x:.2f} | {sum_y:.2f} | {sum_x_squared:.2f} | {sum_xy:.2f}")
print()

# Perform linear least squares fitting
slope, intercept = linear_least_squares(x, y)

# Print the linear fitted equation
print(f"Linear Fitted Equation: y = {slope:.2f}x + {intercept:.2f}")

# Generate the fitted line points
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = slope * x_fit + intercept

# Plot the data points and the fitted line
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_fit, y_fit, color='red', label='Fitted Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Least Squares Fitting')
plt.legend()
plt.grid(True)
plt.show()



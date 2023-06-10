import numpy as np
import matplotlib.pyplot as plt

def power_law_fit(x, y):
    log_x = np.log(x)
    log_y = np.log(y)

    slope, intercept = np.polyfit(log_x, log_y, 1)

    return slope, intercept

def exponential_fit(x, y):
    fit_params = np.polyfit(x, np.log(y), 1)
    slope = fit_params[0]
    intercept = np.exp(fit_params[1])

    return slope, intercept

# Example usage:
x = np.array([1, 2, 3, 4, 5])  # Data points x-coordinates
y = np.array([2, 4, 8, 16, 32])  # Data points y-coordinates

# Get user input for fitting method
fitting_method = input("Choose fitting method (power/exponential): ")

if fitting_method.lower() == "power":
    slope, intercept = power_law_fit(x, y)
    fitted_curve = lambda x: intercept * x ** slope
    fitted_curve_equation = f"y = {intercept:.2f} * x^{slope:.2f}"
elif fitting_method.lower() == "exponential":
    slope, intercept = exponential_fit(x, y)
    fitted_curve = lambda x: intercept * np.exp(slope * x)
    fitted_curve_equation = f"y = {intercept:.2f} * exp({slope:.2f} * x)"
else:
    print("Invalid fitting method chosen.")
    exit()

# Generate the fitted curve points
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = fitted_curve(x_fit)

# Print the fitted curve equation
print(f"Fitted Curve Equation: {fitted_curve_equation}")

# Plot the data points and the fitted curve
plt.scatter(x, y, color='blue', label='Data Points')
plt.plot(x_fit, y_fit, color='red', label='Fitted Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.title(f"{fitting_method.capitalize()} Law Fitting")
plt.legend()
plt.grid(True)
plt.show()

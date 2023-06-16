import math
import matplotlib.pyplot as plt
import numpy as np

def calculate_factorial(n):
    """
    Calculates the factorial of a given number n.
    """
    if n == 0:
        return 1
    return n * calculate_factorial(n - 1)

def taylor_approximation(function, x, num_terms):
    """
    Calculates the Taylor series approximation of the given function at a given point x
    using the specified number of terms.
    """
    result = 0.0
    for n in range(num_terms):
        numerator = function(x, n)
        denominator = calculate_factorial(n)
        result += numerator / denominator
    return result

def calculate_exp(x, n):
    """
    Calculates the nth term of the Taylor series expansion for e^x.
    """
    return x ** n

def calculate_sin(x, n):
    """
    Calculates the nth term of the Taylor series expansion for sin(x).
    """
    sign = (-1) ** n
    numerator = x ** (2 * n + 1)
    denominator = calculate_factorial(2 * n + 1)
    return sign * numerator / denominator

def calculate_cos(x, n):
    """
    Calculates the nth term of the Taylor series expansion for cos(x).
    """
    sign = (-1) ** n
    numerator = x ** (2 * n)
    denominator = calculate_factorial(2 * n)
    return sign * numerator / denominator

def calculate_ln(x, n):
    """
    Calculates the nth term of the Taylor series expansion for ln(1 + x).
    """
    if n % 2 == 0:
        sign = 1
    else:
        sign = -1
    numerator = x ** (n + 1)
    denominator = (n + 1)
    return sign * numerator / denominator

def compare_to_exact_value(approximation, exact_value):
    """
    Compares the approximation with the exact value and calculates the truncation error.
    """
    error = abs(approximation - exact_value)
    relative_error = error / abs(exact_value) * 100
    print(f"Approximation: {approximation}")
    print(f"Exact value: {exact_value}")
    print(f"Truncation error: {error}")
    print(f"Relative error: {relative_error}%")

# Function dictionary mapping
functions = {
    'exp': (calculate_exp, math.exp),
    'sin': (calculate_sin, math.sin),
    'cos': (calculate_cos, math.cos),
    'ln': (calculate_ln, math.log1p),
}

# Get user input for function choice, x, and num_terms
function_choice = input("Choose a function (exp, sin, cos, ln): ")
x = float(input("Enter the value for x: "))
num_terms = int(input("Enter the number of terms: "))

# Check if the chosen function is valid
if function_choice not in functions:
    print("Invalid function choice!")
else:
    # Retrieve the corresponding function and exact function from the dictionary
    function, exact_function = functions[function_choice]

    # Perform the Taylor series approximation
    approximation = taylor_approximation(function, x, num_terms)
    exact_value = exact_function(x)

    # Compare the results
    print("Approximation using Taylor series:")
    compare_to_exact_value(approximation, exact_value)
    print()

    # Plotting
    x_values = np.linspace(-2 * math.pi, 2 * math.pi, 200)
    y_approx = np.vectorize(lambda x: taylor_approximation(function, x, num_terms))(x_values)
    y_exact = np.vectorize(exact_function)(x_values)

    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_approx, label='Approximation')
    plt.plot(x_values, y_exact, label='Exact')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{function_choice}(x) Approximation')
    plt.legend()
    plt.grid(True)
    plt.show()

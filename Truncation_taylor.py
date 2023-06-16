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

# Function dictionary mapping
functions = {
    'exp': (calculate_exp, math.exp),
    'sin': (calculate_sin, math.sin),
    'cos': (calculate_cos, math.cos),
    'ln': (calculate_ln, math.log1p),
}

# Get user input for function choice and x
function_choice = input("Choose a function (exp, sin, cos, ln): ")
x = float(input("Enter the value for x: "))

# Check if the chosen function is valid
if function_choice not in functions:
    print("Invalid function choice!")
else:
    # Retrieve the corresponding function and exact function from the dictionary
    function, exact_function = functions[function_choice]

    # Plotting
    num_terms_range = range(1, 11)
    x_values = np.linspace(-2 * math.pi, 2 * math.pi, 200)

    plt.figure(figsize=(10, 6))

    # Plot the exact function
    y_exact = np.vectorize(exact_function)(x_values)
    plt.plot(x_values, y_exact, label='Exact')

    # Plot the Taylor series approximations with different numbers of terms
    for num_terms in num_terms_range:
        y_approx = np.vectorize(lambda x: taylor_approximation(function, x, num_terms))(x_values)
        plt.plot(x_values, y_approx, label=f'{num_terms} terms')

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{function_choice}(x) Approximation Convergence')
    plt.legend()
    plt.grid(True)
    plt.show()

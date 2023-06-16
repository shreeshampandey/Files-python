'''
import numpy as np
import matplotlib.pyplot as plt

def sine_taylor(x, n):
    result = 0.0
    sign = 1

    for i in range(1, n+1):
        term = sign * (x**(2*i - 1)) / np.math.factorial(2*i - 1)
        result += term
        sign *= -1

    return result

def cosine_taylor(x, n):
    result = 0.0
    sign = 1

    for i in range(n):
        term = sign * (x**(2*i)) / np.math.factorial(2*i)
        result += term
        sign *= -1

    return result

def main():
    x_degrees = float(input("Enter the value of x in degrees: "))
    x_radians = np.deg2rad(x_degrees)

    n = int(input("Enter the number of terms to use in Taylor series expansion: "))

    function_choice = input("Choose a function (sin/cos): ")

    if function_choice.lower() == "sin":
        approx_value = sine_taylor(x_radians, n)
        actual_value = np.sin(x_radians)
    elif function_choice.lower() == "cos":
        approx_value = cosine_taylor(x_radians, n)
        actual_value = np.cos(x_radians)
    else:
        print("Invalid function choice.")
        return

    error = np.abs(actual_value - approx_value)

    print(f"Approximated value: {approx_value:.6f}")
    print(f"Actual value: {actual_value:.6f}")
    print(f"Error: {error:.6f}")

    x_values = np.linspace(0, 2 * np.pi, 100)
    actual_values = np.sin(x_values)
    approximated_values = sine_taylor(x_values, n)

    plt.plot(x_values, actual_values, label='Actual')
    plt.plot(x_values, approximated_values, label='Approximated')
    plt.xlabel('x')
    plt.ylabel('Value')
    plt.title(f'Taylor Series Approximation - {function_choice.capitalize()}')
    plt.legend()
    plt.grid(True)
    plt.show()

    if n > 1:
        convergence_ratio = np.abs(approximated_values[-1] - approximated_values[-2]) / np.abs(approximated_values[-2] - approximated_values[-3])
        print(f"Convergence ratio: {convergence_ratio:.6f}")

if __name__ == '__main__':
    main()

'''

import numpy as np
import matplotlib.pyplot as plt

def sine_taylor(x, n):
    result = 0.0
    sign = 1

    for i in range(1, n+1):
        term = sign * (x**(2*i - 1)) / np.math.factorial(2*i - 1)
        result += term
        sign *= -1

    return result

def cosine_taylor(x, n):
    result = 0.0
    sign = 1

    for i in range(n):
        term = sign * (x**(2*i)) / np.math.factorial(2*i)
        result += term
        sign *= -1

    return result

def main():
    x_degrees = float(input("Enter the value of x in degrees: "))
    x_radians = np.deg2rad(x_degrees)

    n = int(input("Enter the number of terms to use in Taylor series expansion: "))

    function_choice = input("Choose a function (sin/cos): ")

    if function_choice.lower() == "sin":
        actual_value = np.sin(x_radians)
        approx_value = sine_taylor(x_radians, n)
        function_name = "Sine"
    elif function_choice.lower() == "cos":
        actual_value = np.cos(x_radians)
        approx_value = cosine_taylor(x_radians, n)
        function_name = "Cosine"
    else:
        print("Invalid function choice.")
        return

    error = np.abs(actual_value - approx_value)

    print(f"Actual value: {actual_value:.6f}")
    print(f"Approximated value: {approx_value:.6f}")
    print(f"Error: {error:.6f}")

    x_plot = np.linspace(0, n, n+1)
    actual_values = np.full_like(x_plot, actual_value)

    plt.plot(x_plot, actual_values, label="Actual")
    plt.plot(x_plot, approx_value, label="Approximated")
    plt.xlabel("Number of Terms (n)")
    plt.ylabel(f"{function_name} Value")
    plt.title(f"{function_name} Taylor Series Approximation")
    plt.legend()
    plt.grid(True)
    plt.show()

    convergence = np.abs(approx_value[1:] - approx_value[:-1])
    convergence_plot = np.arange(1, n+1)

    plt.plot(convergence_plot, convergence)
    plt.xlabel("Number of Terms (n)")
    plt.ylabel("Convergence")
    plt.title(f"{function_name} Taylor Series Convergence")
    plt.grid(True)
    plt.show()

if __name__ == '__main__':
    main()



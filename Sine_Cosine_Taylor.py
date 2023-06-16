import numpy as np

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
    elif function_choice.lower() == "cos":
        approx_value = cosine_taylor(x_radians, n)
    else:
        print("Invalid function choice.")
        return

    print(f"Approximated value: {approx_value:.6f}")

if __name__ == '__main__':
    main()


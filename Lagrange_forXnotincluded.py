import numpy as np
import matplotlib.pyplot as plt

def lagrange_interpolation(x_data, y_data, x):
    n = len(x_data)
    y = 0

    for i in range(n):
        numerator = 1
        denominator = 1

        for j in range(n):
            if j != i:
                numerator *= (x - x_data[j])
                denominator *= (x_data[i] - x_data[j])

        y += y_data[i] * (numerator / denominator)

    return y


x_data = [1, 2, 3, 4]
y_data = [4, 2, 1, 3]


x_test = 5


y_test = lagrange_interpolation(x_data, y_data, x_test)


print(f"y({x_test}) = {y_test}")


plt.scatter(x_data, y_data, color='red', label='Data Points')
x = np.linspace(min(x_data), x_test, 100)
y = lagrange_interpolation(x_data, y_data, x)
plt.plot(x, y, color='blue', label='Interpolated Curve')
plt.scatter(x_test, y_test, color='green', label=f'y({x_test})')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Lagrange Interpolation')
plt.grid(True)
plt.show()

import random
import math

def f(x):
    return x**2

def acceptance_rejection_method(f, a, b, N):
    c = max(f(a), f(b))
    count = 0
    for i in range(N):
        x = random.uniform(a, b)
        y = random.uniform(0, c)
        if y <= f(x):
            count += 1
    return count / N * c * (b - a)

if __name__ == '__main__':
    # Estimate the value of π
    N = 100000
    count = 0
    for i in range(N):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            count += 1
    print('Value of π:', 4 * count / N)

    # Integrate the function f(x) = x**2
    a = 0
    b = 1
    N = 100000
    result = acceptance_rejection_method(f, a, b, N)
    print('Integration result:', result)

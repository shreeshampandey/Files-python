import numpy as np
import matplotlib.pyplot as plt


def generate_random_numbers(distribution, N):
    if distribution == 'uniform':
        return np.random.uniform(0, 1, N)
    elif distribution == 'binomial':
        return np.random.binomial(1, 0.5, N)
    elif distribution == 'poisson':
        return np.random.poisson(1, N)
    elif distribution == 'gaussian':
        return np.random.normal(0, 1, N)
    else:
        return None


def plot_distribution(distribution, N):
    numbers = generate_random_numbers(distribution, N)
    plt.hist(numbers, bins=30)
    plt.title('{} Distribution with N = {}'.format(distribution.capitalize(), N))
    plt.show()


def verify_central_limit_theorem(distribution, N):
    numbers = generate_random_numbers(distribution, N)
    mean = np.mean(numbers)
    std = np.std(numbers)
    print('Mean: {:.2f}, Standard Deviation: {:.2f}'.format(mean, std))


if __name__ == '__main__':
    distribution = 'gaussian'
    N = 1000
    plot_distribution(distribution, N)
    verify_central_limit_theorem(distribution, N)

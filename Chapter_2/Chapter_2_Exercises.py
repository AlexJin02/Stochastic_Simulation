# Exercise 2.1
import numpy as np
import matplotlib.pyplot as plt

r = 4.0
N = 100000
x = np.zeros(N)

def p_star(x):
    return 1 / (np.pi * np.sqrt(x * (1 - x)))


x[0] = np.random.rand()

for i in range(1, N):
    x[i] = r * x[i-1] * (1 - x[i-1])

plt.hist(x, bins=100, density=True, alpha=0.5, label='Histogram of samples')

x_vals = np.linspace(0.001, 0.999, 1000)
plt.plot(x_vals, p_star(x_vals), 'r-', label='Arcsine distribution density')
plt.xlabel('x')
plt.ylabel('Density')
plt.title('Histogram of Logistic Map Samples vs Arcsine Distribution')
plt.legend()
plt.show()

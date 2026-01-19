import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 4, 7]
y = [3, 6, 24, 48]

n = len(x)

coef = y.copy()

for j in range(1, n):
    for i in range(n-1, j-1, -1):
        coef[i] = (coef[i] - coef[i-1]) / (x[i] - x[i-j])

def newton_dd(x_val):
    result = coef[0]
    product = 1
    for i in range(1, n):
        product *= (x_val - x[i-1])
        result += coef[i] * product
    return result

x_val = 3
print("Interpolated value at x =", x_val, "is", newton_dd(x_val))


x_plot = np.linspace(min(x), max(x), 100)
y_plot = [newton_dd(xi) for xi in x_plot]

plt.plot(x_plot, y_plot, label="Newton Divided Difference")
plt.scatter(x, y, color='red', label="Data Points")
plt.legend()
plt.grid(True)
plt.show()

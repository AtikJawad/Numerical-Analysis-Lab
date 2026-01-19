import matplotlib.pyplot as plt
import numpy as np

x_data = [0, 1, 2, 3]
y_data = [1, 3, 2, 5]

def lagrange(x, x_data, y_data):
    total = 0
    n = len(x_data)

    for i in range(n):
        term = y_data[i]
        for j in range(n):
            if i != j:
                term *= (x - x_data[j]) / (x_data[i] - x_data[j])
        total += term

    return total

x_val = 1.5
print("Interpolated value at x =", x_val, "is", lagrange(x_val, x_data, y_data))

x_plot = np.linspace(min(x_data), max(x_data), 100)
y_plot = [lagrange(x, x_data, y_data) for x in x_plot]

plt.plot(x_plot, y_plot, label="Lagrange Polynomial")
plt.scatter(x_data, y_data, color='red', label="Data Points")
plt.legend()
plt.grid(True)
plt.show()

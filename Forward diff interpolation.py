import matplotlib.pyplot as plt
import numpy as np

x = [0, 1, 2, 3]
y = [1, 3, 7, 13]

h = x[1] - x[0]
n = len(y)

diff = [y.copy()]

for i in range(1, n):
    temp = []
    for j in range(n - i):
        temp.append(diff[i-1][j+1] - diff[i-1][j])
    diff.append(temp)

def newton_forward(x_val):
    p = (x_val - x[0]) / h
    result = y[0]
    fact = 1
    p_term = 1

    for i in range(1, n):
        p_term *= (p - (i - 1))
        fact *= i
        result += (p_term * diff[i][0]) / fact

    return result

x_val = 0.5
print("Interpolated value at x =", x_val, "is", newton_forward(x_val))

# Plot
x_plot = np.linspace(min(x), max(x), 100)
y_plot = [newton_forward(xi) for xi in x_plot]

plt.plot(x_plot, y_plot, label="Newton Forward")
plt.scatter(x, y, color='red', label="Data Points")
plt.legend()
plt.grid(True)
plt.show()

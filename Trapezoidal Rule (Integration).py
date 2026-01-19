import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 1   # example function

def trapezoidal(a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        result += 2 * f(a + i*h)

    return (h / 2) * result

a = 0
b = 2
n = 4

ans = trapezoidal(a, b, n)
print("Trapezoidal Rule Result =", ans)

# Plot
x = np.linspace(a, b, 100)
plt.plot(x, f(x),'r--')
plt.title("Trapezoidal Rule")
plt.grid(True)
plt.show()

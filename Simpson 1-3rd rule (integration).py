import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 1

def simpson_one_third(a, b, n):
    if n % 2 != 0:
        print("n must be even!")
        return None

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        if i % 2 == 0:
            result += 2 * f(a + i*h)
        else:
            result += 4 * f(a + i*h)

    return (h / 3) * result

a = 0
b = 2
n = 4

ans = simpson_one_third(a, b, n)
print("Simpson 1/3 Rule Result =", ans)

# Plot
x = np.linspace(a, b, 100)
plt.plot(x, f(x))
plt.title("Simpson's 1/3 Rule")
plt.grid(True)
plt.show()

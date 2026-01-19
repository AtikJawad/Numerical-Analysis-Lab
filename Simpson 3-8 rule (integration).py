import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 1

def simpson_three_eight(a, b, n):
    if n % 3 != 0:
        print("n must be multiple of 3!")
        return None

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        if i % 3 == 0:
            result += 2 * f(a + i*h)
        else:
            result += 3 * f(a + i*h)

    return (3 * h / 8) * result

a = 0
b = 3
n = 6

ans = simpson_three_eight(a, b, n)
print("Simpson 3/8 Rule Result =", ans)

x = np.linspace(a, b, 100)
plt.plot(x, f(x))
plt.title("Simpson's 3/8 Rule")
plt.grid(True)
plt.show()
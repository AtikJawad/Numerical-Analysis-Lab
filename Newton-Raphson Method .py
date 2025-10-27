# Newton-Raphson Method
import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return math.sin(x) - 1 + x  # Example function math.sin(x) - 1 + x

def df(x):
    return math.cos(x) + 1  # Derivative of f(x) math.cos(x) + 1

def newton_raphson(a, b, tol):

    if f(a)*f(b)>=0 :
        print("Wrong interval! f(a) and f(b) must have opposite signs.")
        return None
    x0 = a # x0=b also valid
    while True:
        x1 = x0 - (f(x0) / df(x0))
        if abs(x1 - x0) < tol:
            break
        x0 = x1

    return x1


a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
tol = float(input("Enter tolerance (e.g. 0.001): "))   # e.g. 0.001

root = newton_raphson(a, b, tol)
print(f"Approximate root = {root:.6f}")
# ---- Plot the function and root ----

x = np.linspace(-5, 5, 100)
y = np.sin(x) - 1 + x

plt.plot(x, y)                   # plot the function
plt.axhline(0, color='black')    # x-axis
plt.axvline(0, color='black')
plt.scatter(root, 0, color='red')  # mark the root
plt.title("f(x) = sin(x) - 1 + x")
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()

# Fixed Point Iteration Method in Python
import numpy as np
import matplotlib.pyplot as plt

def fixed_point(func, x0, tol):
    def g(x):
        return eval(func)

    while True:
        x1 = g(x0)
        if abs(x1 - x0) < tol:
            break
        x0 = x1

    return x1

func= input("Enter x=g(x) e.g. ( the x derived from f(x)=0 => 1/((x+1)**(1/2))) : ")
x0 = float(input("Enter initial guess (e.g 3.2 for trigonos and logs & 0.5 for exponentials : "))
tol = float(input("Enter tolerance (e.g. 0.001): "))

root = fixed_point(func, x0, tol)
print(f"Approximate root = {root:.6f}")
# plotting

x = np.linspace(-5, 5, 100)
y = eval(func)  # original f(x)

plt.plot(x, y)
plt.axhline(0, color='black')
plt.axvline(0, color='black')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.scatter(root, 0, color='red')  # root
plt.title(f"Fixed Point Iteration: g(x) = {func}")
plt.show()

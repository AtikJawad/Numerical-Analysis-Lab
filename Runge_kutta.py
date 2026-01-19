import matplotlib.pyplot as plt
import math

# dy/dx = y - x^2 + 1
def f(x, y):
    return y - x**2 + 1

def runge_kutta_4(x0, y0, xn, h):
    x_values = [x0]
    y_values = [y0]
    step = 0

    print("\nStep\t  x\t\t  y (approx)")
    print("--------------------------------------")

    while x0 < xn:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)

        y1 = y0 + (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 = round(x0 + h, 4)
        step += 1

        print(f"{step}\t  {x0:.4f}\t  {y1:.6f}")

        x_values.append(x0)
        y_values.append(y1)
        y0 = y1

    return x_values, y_values


# GIVEN INPUTS FROM QUESTION
x0 = 0
y0 = 0.5
xn = 2
h = 0.2

x_vals, y_vals = runge_kutta_4(x0, y0, xn, h)

print("\nComparison with Exact Solution:")
print("x\t  RK4 y\t\t  Exact y\t  Error")
print("--------------------------------------------------")

exact_values = []
for i in range(len(x_vals)):
    exact = (x_vals[i] + 1)**2 - 0.5 * math.exp(x_vals[i])
    exact_values.append(exact)
    error = abs(exact - y_vals[i])
    print(f"{x_vals[i]:.1f}\t  {y_vals[i]:.6f}\t  {exact:.6f}\t  {error:.6f}")

# PLOTTING BOTH CURVES
plt.plot(x_vals, y_vals, 'r-o', label="Runge-Kutta 4th Order")
plt.plot(x_vals, exact_values, 'b-', label="Exact Solution")
plt.title("Comparison: RK4 vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
import matplotlib.pyplot as plt
import math

# dy/dx = y - x^2 + 1
def f(x, y):
    return y - x**2 + 1

# Formula for 2nd-order Taylor:
# y'' = f_x + f_y * f(x, y)
def f_prime(x, y):
    f_x = -2*x       # derivative wrt x
    f_y = 1          # derivative wrt y
    return f_x + f_y * f(x, y)

def taylor_method(x0, y0, xn, h):
    x_values = [x0]
    y_values = [y0]
    step = 0

    print("\nStep\t  x\t\t  y (approx)\t  f(x,y)")
    print("--------------------------------------------------")

    while x0 < xn :
        fxy = f(x0, y0)
        y1 = y0 + h*fxy + (h**2/2)*f_prime(x0, y0)
        x0 = round(x0 + h, 4)
        step += 1
        print(f"{step}\t  {x0:.4f}\t  {y1:.6f}\t  {fxy:.6f}")
        x_values.append(x0)
        y_values.append(y1)
        y0 = y1

    return x_values, y_values

# GIVEN INPUTS FROM QUESTION
x0 = 0
y0 = 0.5
xn = 2
h = 0.2

# RUN THE METHOD
x_vals, y_vals = taylor_method(x0, y0, xn, h)

print("\nComparison with Exact Solution:")
print("x\t  Taylor y\t  Exact y\t  Error")
print("--------------------------------------------------")

exact_values = []
for i in range(len(x_vals)):
    exact = (x_vals[i] + 1)**2 - 0.5*math.exp(x_vals[i])
    exact_values.append(exact)
    error = abs(exact - y_vals[i])
    print(f"{x_vals[i]:.1f}\t  {y_vals[i]:.6f}\t  {exact:.6f}\t  {error:.6f}")

# PLOTTING BOTH CURVES
plt.plot(x_vals, y_vals, 'r-o', label="Taylor 2nd Order (Approx)")
plt.plot(x_vals, exact_values, 'b-', label="Exact Solution")
plt.title("Comparison: Taylor 2nd Order vs Exact Solution")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
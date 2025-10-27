import numpy as np
import matplotlib.pyplot as plt

def false_position(func_str, a, b, tol):
    def f(x):
        return eval(func_str)

    if f(a) * f(b) >= 0:
        print("Wrong interval! f(a) and f(b) must have opposite signs.")
        return None

    while True:
        # Formula for false position
        c = ((a * f(b) - b * f(a))/ (f(b)- f(a)))

        # Check if root is found or close enough
        if abs(f(c)) < tol:
            break

        # Update interval based on sign change
        if f(a) * f(c) > 0:  # same as Bisection
            a = c
        else:
            b = c

    return c


func= input("Enter any equation using variable 'x' only e.g. ( x**3-3*x+1 ) : ")
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
tol = float(input("Enter tolerance (e.g. 0.0001): "))

root = false_position(func, a, b, tol)
print(f" Root = {root:.6f} [Approx...]")

# plotting
x= np.linspace(-5,5,100)
y= eval(func)

plt.plot(x,y)

plt.axhline(0,color= 'black')
plt.axvline(0,color='black')
plt.scatter(root,0, color='blue') # mark the root

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title(f" False Position Method: {func}")

plt.show()

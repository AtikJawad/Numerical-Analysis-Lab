import numpy as np
import matplotlib.pyplot as plt

def bisection(func_str,a,b,tol):
    """
      Find the root of a function using the Bisection Method.

      Parameters:
      - func_str: A string expression like "x**3 - x - 2"
      - a: Lower bound of the root
      - b: Upper bound of the root
      - tolerance: How close a and b must be to stop (e.g., 0.001)

      Returns:
      - Approximate root of the function
      """

    def f(x):
        return eval(func_str)

    if f(a)*f(b)>=0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    while abs(b-a) > tol:

        c = (a+b)/2 #midpooint

        if f(c) == 0:
            return c #exact Root
        if f(a)*f(c) > 0:
            a=c       # if f(c) and f(a) are both same sign , replace a with c
        else:
            b=c       # else f(c) and f(b) are both same sign , replace b with c

    return (a+b)/2      # Midpoint is the best approximation

func= input("Enter any equation using variable 'x' only e.g. ( x**3-3*x+1 ) : ")
a = float(input("Enter lower limit a: "))
b = float(input("Enter upper limit b: "))
tolerance=float(input("Enter Tolerance (desired_accuracy) e.g (0.00001): "))

root = bisection(func,a,b,tolerance)

print(f"Root = {root:.5f} [Approx...]")

#plotting
x= np.linspace(-5,5,100)
y= eval(func)

plt.plot(x,y)

plt.axvline(0,color ='black')
plt.axhline(0,color = 'black')
plt.scatter(root,0,color= 'red') # mark the root

plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.title(f"Bisection Method:{func}")

plt.show()


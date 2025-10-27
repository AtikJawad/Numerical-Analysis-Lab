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
        return eval(func_str)  # eval() is a built-in Python function that takes a string and executes it as Python code

    if f(a)*f(b)>=0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    while abs(b-a) > tol:
        mid = (a+b)/2 #midpooint

        if f(mid) == 0:
            return mid #exact Root
        if f(a)*f(mid) > 0:
            a=mid       # if f(mid) and f(a) are both same sign , replace a with mid
        else:
            b=mid       # else f(mid) and f(b) are both same sign , replace b with mid

    return (a+b)/2      # Midpoint is the best approximation

func= input("Enter any equation using variable 'x' only e.g. ( x**3-3*x+1 ) : ")
a= float(input("Enter lower bound: "))
b=float(input("Enter upper bound: "))
tolerance=float(input("Enter Tolerance (desired_accuracy) e.g (0.00001): "))

root = bisection(func,a,b,tolerance)

print(f"Root = {root:.5f}")

#plotting
x= np.linspace(-5,5,100)
y= eval(func)

plt.plot(x,y)
plt.axvline(0,color ='black')
plt.axhline(0,color = 'black')
plt.scatter(root,0,color= 'red') # mark the root
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title(f"Bisection Method:{func}")
plt.show()

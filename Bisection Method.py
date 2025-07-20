def bisection_method(func_str, a, b, tolerance):
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
    
    # Check if f(a) and f(b) have opposite signs
    if f(a) * f(b) >= 0:
        print("Error: f(a) and f(b) must have opposite signs.")
        return None

    while abs(b - a) > tolerance:
        c = (a + b) / 2  # Midpoint

        if f(c) == 0:
            return c  # Found exact root

        if f(a) * f(c) > 0:
            a = c
        else:
            b = c

    # Midpoint is our best approximation
    return (a + b) / 2


func= input("Enter any equation using variable 'x' only e.g.(x**3 - x - 2)")
interval=

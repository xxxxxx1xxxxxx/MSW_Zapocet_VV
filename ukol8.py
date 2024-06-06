import numpy as np

def func(x):
    return x**2

def static_numerical_derivative(func, x, h=1e-5):
    return (func(x + h) - func(x - h)) / (2 * h)

def adaptive_numerical_derivative(func, x, h=1e-5, tol=1e-3):
    deriv = (func(x + h) - func(x - h)) / (2 * h)
    h_new = h * 0.9 # initial value of new step size
    while True:
        deriv_new = (func(x + h_new) - func(x - h_new)) / (2 * h_new)
        error = abs(deriv_new - deriv)
        if error < tol:
            return deriv_new, h_new
        else:
            deriv = deriv_new
            h_new *= 0.9

x = 2 # Point at which to evaluate the derivative

# Static numerical derivative
static_derivative = static_numerical_derivative(func, x)

# Adaptive numerical derivative
adaptive_derivative, step_size = adaptive_numerical_derivative(func, x)

# Analytic derivative
analytic_derivative = 2 * x

print("Statická numerická derivace v bodě x =", x, "je", static_derivative)
print("Adaptivní numerická derivace v bodě x =", x, "je", adaptive_derivative, "s krokem velikosti", step_size)
print("Analytická derivace v bodě x =", x, "je", analytic_derivative)



#Statická numerická derivace v bodě x = 2 je 4.000000000026205
#Adaptivní numerická derivace v bodě x = 2 je 3.9999999999669926 s krokem velikosti 9e-06
#Analytická derivace v bodě x = 2 je 4

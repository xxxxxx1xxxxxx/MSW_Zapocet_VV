import timeit
# 1. Skalární součin dvou vektorů

# Standardní Python
def dot_product_standard(a, b):
    return sum(x * y for x, y in zip(a, b))

# Generování dvou vektorů
a = list(range(1000))
b = list(range(1000))

# Měření času
time_standard = timeit.timeit('dot_product_standard(a, b)', globals=globals(), number=1000)
print(f'Standardní Python skalární součin: {time_standard} sekund')
#Standardní Python: 0.1350341999786906 sekund

#NumPy
import numpy as np

a_np = np.array(a)
b_np = np.array(b)

# Měření času
time_numpy = timeit.timeit('np.dot(a_np, b_np)', globals=globals(), number=1000)
print(f'NumPy skalarní součin: {time_numpy} sekund')
#NumPy: 0.0037320000119507313 sekund








#2. Určitý integrál funkce

#Standardní Python

def f(x):
    return x**2

def integrate_standard(f, a, b, n=1000):
    h = (b - a) / n
    result = sum(f(a + i * h) for i in range(n)) * h
    return result

# Měření času
time_standard = timeit.timeit('integrate_standard(f, 0, 1)', globals=globals(), number=1000)
print(f'Standardní Python integrál: {time_standard} sekund')
#Standardní Python integrál: 0.47627429995918646 sekund

#SciPy
import scipy.integrate as spi

# Měření času
time_scipy = timeit.timeit('spi.quad(f, 0, 1)', globals=globals(), number=1000)
print(f'SciPy integral: {time_scipy} sekund')
#SciPy integral: 0.012221199984196573 sekund











#3. Výpočet determinantu matice

#Standardní Python:
def determinant_standard(matrix):
    # Implementace výpočtu determinantu (např. Gaussova eliminace)
    pass

matrix = [[1, 2], [3, 4]]

# Měření času
time_standard = timeit.timeit('determinant_standard(matrix)', globals=globals(), number=1000)
print(f'Standardní Python determinant matice: {time_standard} sekund')


#NumPy
import numpy as np
matrix_np = np.array(matrix)

# Měření času
time_numpy = timeit.timeit('np.linalg.det(matrix_np)', globals=globals(), number=1000)
print(f'NumPy determinant matice: {time_numpy} sekund')









#4. Výpočet Fibonacciho čísla

#Standardní Python 
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Měření času pro n=20
time_standard = timeit.timeit('fibonacci_recursive(20)', globals=globals(), number=100)
print(f'Standardní Python fibonacciho číslo (rekurzivní): {time_standard} sekund')
#Standardní Python fibonacciho číslo (rekurzivní): 0.20546210004249588 sekund


#Numba
import numba
from numba import jit

@jit(nopython=True)
def fibonacci_numba(n):
    if n <= 1:
        return n
    else:
        return fibonacci_numba(n-1) + fibonacci_numba(n-2)

# Měření času pro n=35
time_numba = timeit.timeit('fibonacci_numba(35)', globals=globals(), number=100)
print(f'Numba fibonacciho číslo: {time_numba} sekund')
#Numba fibonacciho číslo: 0.3698045000201091 sekund










#5. Řešení soustavy lineárních rovnic

#Standardní Python
def solve_linear_system_standard(a, b):
    # Implementace Gaussovy eliminace nebo jiné metody
    pass

A = [[3, 2], [1, 4]]
B = [1, 2]

# Měření času
time_standard = timeit.timeit('solve_linear_system_standard(A, B)', globals=globals(), number=1000)
print(f'Standardní Python linearni rovnice: {time_standard} sekund')



#NumPy
import numpy as np

A_np = np.array(A)
B_np = np.array(B)

# Měření času
time_numpy = timeit.timeit('np.linalg.solve(A_np, B_np)', globals=globals(), number=1000)
print(f'NumPy linearni rovnice: {time_numpy} sekund')

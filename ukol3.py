import numpy as np
import scipy.linalg as la
import scipy.sparse.linalg as spla
import matplotlib.pyplot as plt
import time

def measure_time(matrix_size, method):
    # Generování symetrické pozitivně definitní matice
    A = np.random.rand(matrix_size, matrix_size)
    A = np.dot(A, A.transpose())  # Zajistí symetrickou pozitivně definitní matici
    b = np.random.rand(matrix_size)
    
    start_time = time.time()
    if method == 'direct':
        try:
            la.solve(A, b)
        except la.LinAlgError:
            return float('inf')  # Pokud nelze vyřešit, vrátí nekonečno
    elif method == 'iterative':
        try:
            spla.cg(A, b)
        except spla.ArpackNoConvergence:
            return float('inf')  # Pokud nelze vyřešit, vrátí nekonečno
    end_time = time.time()
    
    return end_time - start_time

matrix_sizes = range(50, 501, 50)
direct_times = []
iterative_times = []

for size in matrix_sizes:
    direct_time = np.mean([measure_time(size, 'direct') for _ in range(10)])
    iterative_time = np.mean([measure_time(size, 'iterative') for _ in range(10)])
    direct_times.append(direct_time)
    iterative_times.append(iterative_time)

plt.figure(figsize=(10, 6))
plt.plot(matrix_sizes, direct_times, label='Přímá metoda', marker='o')
plt.plot(matrix_sizes, iterative_times, label='Iterační metoda', marker='o')
plt.xlabel('Velikost matice')
plt.ylabel('Průměrný čas (v sekundách)')
plt.title('PŘÍMÁ VS ITERAČNÍ METODA')
plt.legend()
plt.grid(True)
plt.show()




#Import knihoven: Načteme potřebné knihovny (NumPy, SciPy, Matplotlib, time).
#Funkce measure_time: Tato funkce generuje náhodnou matici a vektor, poté měří čas potřebný k vyřešení soustavy lineárních rovnic buď přímou metodou (LU rozklad) nebo iterační metodou (Conjugate Gradient).
#Seznam velikostí matic matrix_sizes: Určujeme různé velikosti matic, které budeme testovat.
#Sběr dat: Pro každou velikost matice řešíme soustavu rovnic 10krát pro každou metodu a průměrný čas ukládáme.
#Vykreslení grafu: Pomocí Matplotlib vykreslíme výsledky do grafu.

import numpy as np
import time

# Definování funkcí
def f1(x):
    return x**3 - 6*x**2 + 11*x - 6

def f2(x):
    return np.exp(x) - 3*x

def f3(x):
    return np.sin(x) - 0.5

# Derivace funkcí pro Newtonovu metodu
def df1(x):
    return 3*x**2 - 12*x + 11

def df2(x):
    return np.exp(x) - 3

def df3(x):
    return np.cos(x)

# Uzavřená metoda: metoda bisekce
def bisekce(f, a, b, tol=1e-10, max_iterations=1000):
    for _ in range(max_iterations):
        c = (a + b) / 2
        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if np.sign(f(c)) == np.sign(f(a)):
            a = c
        else:
            b = c
    return c

# Otevřená metoda: Newtonova metoda
def newton(f, df, x0, tol=1e-10, max_iterations=1000):
    x = x0
    for _ in range(max_iterations):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x

# Testování funkcí a měření časové náročnosti a přesnosti

funkce = [(f1, df1, (1, 3), 2.0), (f2, df2, (0, 1), 0.5), (f3, df3, (0, 2), 1.0)]
vysledky = []
pocet_opakovani = 100

for f, df, interval, x0 in funkce:
    # Metoda bisekce
    casy_bisekce = []
    for _ in range(pocet_opakovani):
        start_time = time.time()
        koren_bisekce = bisekce(f, interval[0], interval[1])
        end_time = time.time()
        casy_bisekce.append(end_time - start_time)
    prumerny_cas_bisekce = np.mean(casy_bisekce)
    chyba_bisekce = abs(f(koren_bisekce))
    
    # Newtonova metoda
    casy_newton = []
    for _ in range(pocet_opakovani):
        start_time = time.time()
        koren_newton = newton(f, df, x0)
        end_time = time.time()
        casy_newton.append(end_time - start_time)
    prumerny_cas_newton = np.mean(casy_newton)
    chyba_newton = abs(f(koren_newton))
    
    vysledky.append({
        'funkce': f.__name__,
        'koren_bisekce': koren_bisekce,
        'prumerny_cas_bisekce': prumerny_cas_bisekce,
        'chyba_bisekce': chyba_bisekce,
        'koren_newton': koren_newton,
        'prumerny_cas_newton': prumerny_cas_newton,
        'chyba_newton': chyba_newton
    })

# Výpis výsledků
for vysledek in vysledky:
    print(f"Funkce: {vysledek['funkce']}")
    print(f"  Metoda bisekce: kořen = {vysledek['koren_bisekce']:.10f}, průměrný čas = {vysledek['prumerny_cas_bisekce']:.10f}s, chyba = {vysledek['chyba_bisekce']:.10e}")
    print(f"  Newtonova metoda: kořen = {vysledek['koren_newton']:.10f}, průměrný čas = {vysledek['prumerny_cas_newton']:.10f}s, chyba = {vysledek['chyba_newton']:.10e}")
    print()

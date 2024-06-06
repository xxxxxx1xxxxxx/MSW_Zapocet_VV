import numpy as np

# Definice funkcí
def polynom(x):
    return 4*x**3 - 2*x**2 + 5*x - 7

def harmonicka(x):
    return np.sin(2*x)

def exponenciala(x):
    return np.exp(2*x)

# Metoda Monte Carlo pro výpočet integrálu
def monte_carlo_integration(func, a, b, n):
    x = np.random.uniform(a, b, n)
    y = func(x)
    mean_y = np.mean(y)
    area = (b - a) * mean_y
    return area

# Metoda adaptivního Simpsonova pravidla pro výpočet integrálu
def adaptive_simpson_rule(func, a, b, tol=1e-6):
    def simpson_rule(func, a, b):
        return (b - a) / 6 * (func(a) + 4 * func((a + b) / 2) + func(b))

    def recursive_simpson_rule(func, a, b, tol, whole_area):
        c = (a + b) / 2
        left_area = simpson_rule(func, a, c)
        right_area = simpson_rule(func, c, b)
        total_area = left_area + right_area

        if abs(total_area - whole_area) <= 15 * tol:
            return total_area
        else:
            return (recursive_simpson_rule(func, a, c, tol/2, left_area) +
                    recursive_simpson_rule(func, c, b, tol/2, right_area))

    return recursive_simpson_rule(func, a, b, tol, simpson_rule(func, a, b))

# Intervaly pro integraci
interval_polynom = (0, 3)
interval_harmonicka = (0, np.pi)
interval_exponenciala = (0, 2)

# Počet náhodných bodů pro Monte Carlo integraci
n = 10000

# Výpočet integrálů pomocí metody Monte Carlo
integral_polynom_mc = monte_carlo_integration(polynom, *interval_polynom, n)
integral_harmonicka_mc = monte_carlo_integration(harmonicka, *interval_harmonicka, n)
integral_exponenciala_mc = monte_carlo_integration(exponenciala, *interval_exponenciala, n)

# Výpočet integrálů pomocí metody adaptivního Simpsonova pravidla
integral_polynom_asr = adaptive_simpson_rule(polynom, *interval_polynom)
integral_harmonicka_asr = adaptive_simpson_rule(harmonicka, *interval_harmonicka)
integral_exponenciala_asr = adaptive_simpson_rule(exponenciala, *interval_exponenciala)

# Výsledky
print("Monte Carlo integrál pro polynom:", integral_polynom_mc)
print("Monte Carlo integrál pro harmonickou funkci:", integral_harmonicka_mc)
print("Monte Carlo integrál pro exponenciální funkci:", integral_exponenciala_mc)
print()
print("Adaptivní Simpsonovo pravidlo pro polynom:", integral_polynom_asr)
print("Adaptivní Simpsonovo pravidlo pro harmonickou funkci:", integral_harmonicka_asr)
print("Adaptivní Simpsonovo pravidlo pro exponenciální funkci:", integral_exponenciala_asr)

#VYSLEDKY
#Monte Carlo integrál pro polynom: 63.93472344159338
#Monte Carlo integrál pro harmonickou funkci: -0.010525823373677134       
#Monte Carlo integrál pro exponenciální funkci: 26.970766031621338        

#Adaptivní Simpsonovo pravidlo pro polynom: 64.5
#Adaptivní Simpsonovo pravidlo pro harmonickou funkci: 0.0
#Adaptivní Simpsonovo pravidlo pro exponenciální funkci: 26.79907534738094

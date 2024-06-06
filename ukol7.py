import yfinance as yf
import numpy as np

# Získání historických dat Bitcoinu z Yahoo Finance
bitcoin_data = yf.download('BTC-USD', start='2020-01-01', end='2021-01-01')

# Vybrání sloupce 'Close' (uzavírací ceny) pro další analýzu
bitcoin_prices = bitcoin_data['Close']

# Výpočet denních procentuálních změn cen Bitcoinu
daily_returns = bitcoin_prices.pct_change().dropna()

# Počet simulací
num_simulations = 1000

# Počet dní pro simulaci
days = 365

# Počáteční cena Bitcoinu
initial_price = bitcoin_prices.iloc[-1]

# Generování náhodných změn cen pomocí Monte Carlo
simulated_prices = []
for i in range(num_simulations):
    daily_returns_simulated = np.random.choice(daily_returns, days)
    price = initial_price * np.prod(1 + daily_returns_simulated)
    simulated_prices.append(price)

# Definice cílového kurzu
target_price = 180000

# Výpočet pravděpodobnosti dosažení cílového kurzu
probability = sum(price >= target_price for price in simulated_prices) / num_simulations

print(f'Pravděpodobnost dosažení cílového kurzu {target_price}: {probability}')


#Pravděpodobnost dosažení cílového kurzu 180000: 0.297
#To znamená, že podle simulace Monte Carlo založené na historických datech je pravděpodobnost, že cena Bitcoinu dosáhne nebo překročí 180 000 USD, přibližně 29,7 %.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Adresář obsahující CSV soubory
data_dir = 'C:\\Users\\valih\\OneDrive\\Plocha\\archive'

# Seznam všech souborů v adresáři
files = os.listdir(data_dir)

# Načtení datových sad pro jednotlivé kryptoměny
crypto_data = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        coin_data = pd.read_csv(os.path.join(data_dir, file))
        crypto_data = pd.concat([crypto_data, coin_data])

# Přejmenování sloupce 'Date' na 'date'
crypto_data.rename(columns={'Date': 'date'}, inplace=True)

# Zobrazíme si prvních několik řádků spojené datové sady
print(crypto_data.head())

# Převedeme sloupec 'date' na typ datetime
crypto_data['date'] = pd.to_datetime(crypto_data['date'])

# Vytvoříme nový sloupec s rokem
crypto_data['year'] = crypto_data['date'].dt.year

# Zjistíme počet unikátních kryptoměn v datové sadě
num_unique_coins = crypto_data['Symbol'].nunique()
print("Počet unikátních kryptoměn:", num_unique_coins)

# Funkce pro vytvoření grafu vývoje ceny vybrané kryptoměny v čase
def plot_price_trend(data, symbol):
    coin_data = data[data['Symbol'] == symbol]
    plt.figure(figsize=(10, 6))
    plt.plot(coin_data['date'], coin_data['Close'], color='blue')
    plt.title('Vývoj ceny ' + symbol + ' v čase')
    plt.xlabel('Datum')
    plt.ylabel('Cena (USD)')
    plt.grid(True)
    plt.show()
    plt.close()

# Histogram cen
def plot_price_histogram(data, symbol):
    coin_data = data[data['Symbol'] == symbol]
    plt.figure(figsize=(10, 6))
    sns.histplot(coin_data['Close'], kde=True, color='blue')
    plt.title('Histogram cen ' + symbol)
    plt.xlabel('Cena (USD)')
    plt.ylabel('Počet obchodů')
    plt.grid(True)
    plt.show()
    plt.close()

# Boxploty cen
def plot_price_boxplot(data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Symbol', y='Close', data=data, palette='Set2', hue='Symbol', legend=False)
    plt.title('Boxploty cen kryptoměn')
    plt.xlabel('Kryptoměna')
    plt.ylabel('Cena (USD)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.show()
    plt.close()

# Korelační grafy
def plot_correlation(data):
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(10, 6))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Korelační matice cen kryptoměn')
    plt.xlabel('Kryptoměna 1')
    plt.ylabel('Kryptoměna 2')
    plt.show()
    plt.close()

# Zobrazíme vývoj ceny vybraných kryptoměn v čase
plot_price_trend(crypto_data, 'BTC')
plot_price_trend(crypto_data, 'ETH')
plot_price_trend(crypto_data, 'XRP')

# Zobrazíme histogram cen pro vybrané kryptoměny
plot_price_histogram(crypto_data, 'BTC')
plot_price_histogram(crypto_data, 'ETH')

# Zobrazíme boxploty cen pro všechny kryptoměny
plot_price_boxplot(crypto_data)

# Zobrazíme korelační grafy
plot_correlation(crypto_data)



#1. Graf vývoje ceny kryptoměn v čase:
#Z liniových grafů vývoje cen kryptoměn v čase vyplývá, že cena Bitcoinu má tendenci k výraznějším kolísáním než Ethereum a Ripple. Tento rozdíl může být důsledkem různých faktorů, jako je tržní kapitalizace, technické vlastnosti a investiční zájem.

#2. Histogram cen:
#Histogramy cen kryptoměn naznačují, že většina obchodů se uskutečňuje v určitém cenovém rozsahu. Například Bitcoin má tendenci k obchodování v rozmezí od několika tisíc dolarů do několika desítek tisíc dolarů, zatímco Ethereum a Ripple mají rozsah obchodů výraznější.

#3. Boxploty cen:
#Boxploty cen kryptoměn nám ukazují rozložení cen mezi různými kryptoměnami. Například Bitcoin má vyšší maximální ceny než Ethereum a Ripple, což naznačuje větší volatilitu a spekulativní aktivitu v obchodování s Bitcoinem.

#4. Korelační matice cen kryptoměn:
#Korelační matice nám poskytuje informace o vztazích mezi cenami různých kryptoměn. Vysoké korelace mezi cenami mohou naznačovat, že tyto kryptoměny mají tendenci se pohybovat ve stejném směru, což může být užitečné pro investiční strategie diverzifikace portfolia.

#%%
# imports
import requests
import json
import pandas
# %%
url = 'https://economia.awesomeapi.com.br/last/USD-BRL'
ret = requests.get(url)
# %%
if ret:
    print(ret)
else:
    print('Falhou')
# %%
dolar = json.loads(ret.text)['USDBRL']
# %%
print(f"20 Dólares hoje custam {float(dolar['bid']) * 20:.2f} reais")
# %%
def cotacao(valor, moeda):
    url = f'https://economia.awesomeapi.com.br/last/{moeda}'
    ret = requests.get(url)
    dolar = json.loads(ret.text)[moeda.replace('-','')]
    print(f"{valor} {moeda[:3]} hoje custam {float(dolar['bid']) * valor:.2f} {moeda[-3:]}")

#%%
cotacao(20, 'USD-BRL')
# %%
cotacao(20, 'JPY-BRL')
# %%
lst_money = [
        "USD-BRL",
        "EUR-BRL",
        "BTC-BRL",
        "JPY-BRL",
        "RPL-BRL"
    ]
# %%

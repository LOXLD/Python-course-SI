import requests
import pandas as pd
import time
from numpy import mean, round
from cs50 import get_int

def portmonetka_scv():
    file = pd.read_csv('resources.csv')
    return file


def staty():
    url = "https://api.bitbay.net/rest/trading/stats/BTC-USD"

    response = requests.request("GET", url)
    sell_list = response.json()['stats']

    for i in sell_list:
        if i == 'm':
            print('Kod rynku..................................', sell_list[i])
        elif i == 'h':
            print('Najwyższy kurs z ostatnich 24 godzin.......', sell_list[i])
        elif i == 'l':
            print('Najniższy kurs z ostatnich 24 godzin.......', sell_list[i])
        elif i == 'v':
            print('Wolumen z ostatnich 24 godzin..............', sell_list[i])
        elif i == 'r24h':
            print('Średni kurs z ostatnich 24 godzin..........', sell_list[i])


user_choice = get_int('Insert a timestamp (in hours) to count a difference for Bitcoin: ')
now_time = time.time()-user_choice*3600


def info(timerange):
    url2 = f"https://api.bitbay.net/rest/trading/transactions/BTC-USD?fromtime={str(timerange)}"
    headers={'fromtime':str(timerange)}
    response2 = requests.request("GET", url2, headers=headers)

    suma=[]
    for i in response2.json()['items']:
        suma.append(float(i['r']))
    return mean(suma)


def my_wallet():
    print('\nWartość twoich BitCoinow to')
    print(round(float(portmonetka_scv()['Ilosc'][0])*info(now_time),4), 'USD')



def main():
    print('-' * 50)
    print('## Portmonetka ##\n')
    print(portmonetka_scv(),'\n')
    print('-'*50)
    print('#### Statystkiki z ostatnich 24 godzin ####\n')
    staty()
    print('-' * 50)
    my_wallet()

main()

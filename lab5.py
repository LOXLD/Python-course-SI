import requests
import time


def request():
    BTC = requests.get("https://bitbay.net/API/Public/BTCUSD/ticker.json")
    ETH = requests.get("https://bitbay.net/API/Public/ETHUSD/ticker.json")
    DASH = requests.get("https://bitbay.net/API/Public/DASHUSD/ticker.json")
    LTC = requests.get("https://bitbay.net/API/Public/LTCUSD/ticker.json")
    NEU = requests.get("https://bitbay.net/API/Public/NEUUSD/ticker.json")

    return BTC.json(), ETH.json(), DASH.json(), LTC.json(), NEU.json()


def difference(min, max):
    value = float(((max - min) * 100 / min))
    return round(value, 2)


def main():
    while True:
        BTC, ETH, DASH, LTC, NEU = request()

        BTC_max = float(BTC["max"])
        BTC_min = float(BTC["min"])

        ETH_max = float(ETH["max"])
        ETH_min = float(ETH["min"])

        DASH_max = float(DASH["max"])
        DASH_min = float(DASH["min"])

        LTC_max = float(LTC["max"])
        LTC_min = float(LTC["min"])

        NEU_max = float(NEU["max"])
        NEU_min = float(NEU["min"])

        difs = [float(difference(BTC_min, BTC_max)), float(difference(ETH_min, ETH_max)),
                float(difference(DASH_min, DASH_max)),
                float(difference(LTC_min, LTC_max)), float(difference(NEU_min, NEU_max))]
        names = ['Bitcoin', 'Ethereum', 'Dash', 'Litecoin', 'Lisk']

        for i in range(len(difs) - 1, 0, -1):
            for j in range(i):
                if difs[j] < difs[j + 1]:
                    difs[j], difs[j + 1] = difs[j + 1], difs[j]
                    names[j], names[j + 1] = names[j + 1], names[j]

        def data_presentation():
            print('+-' * 20)
            print(time.asctime(), '\n')
            for value in range(len(difs)):
                print(names[value], difs[value], '%')

        data_presentation()
        time.sleep(300)


main()

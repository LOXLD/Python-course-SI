import requests
import time
balance = 0 #USD
buy_list = [
float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['ask']),
float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Ask']),
float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/buy').json()['data']['amount']),
float(requests.get('https://www.bitstamp.net/api/ticker').json()['ask'])]
name_list = ['Bitbay', 'Bittrex', 'Coinbase', 'Bitstamp']
fees = [0.001, 0.002, 0.0025, 0.005]

sell_list = [
float(requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json').json()['bid']),
float(requests.get('https://api.bittrex.com/api/v1.1/public/getticker?market=USD-BTC').json()['result']['Bid']),
float(requests.get('https://api.coinbase.com/v2/prices/BTC-USD/sell').json()['data']['amount']),
float(requests.get('https://www.bitstamp.net/api/ticker').json()['bid'])]

amount_of_BTC_to_buy = 0.1

while True:
    arbitrage = 0
    arbitrage += amount_of_BTC_to_buy * (max(sell_list) - min(buy_list) - max(sell_list)  * fees[buy_list.index(min(buy_list))])
    print('-'*50)
    if arbitrage > 0:
        balance += arbitrage
        print('Bought',amount_of_BTC_to_buy, 'BTC from ', name_list[buy_list.index(min(buy_list))], "and sold on ", name_list[buy_list.index(max(sell_list))], '.Gained',arbitrage,' USD\n')
        print('your balance is equel ',balance)
    else:
        print("can't gain any money when arbitrage is negative. arbitrage =",arbitrage)
    time.sleep(3)
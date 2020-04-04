import requests


def bitbay_ticker():
    response = requests.get('https://bitbay.net/API/Public/LTCUSD/trades.json')
    buy = []
    sell = []
    for i in response.json():
        if i['type'] == 'buy':
            buy.append(i)
        else:
            sell.append(i)
    print('buy offers:')
    for i in buy:
        print('amount', i['amount'], 'in price', i['price'], )

    print('\n')

    print('sell offers: ')
    for i in sell:
        print('amount', i['amount'], 'in price', i['price'], )


def bitbay_vs_bitstamp():
    bb_request = requests.get('https://bitbay.net/API/Public/BTCUSD/ticker.json')
    bb_buy = float(bb_request.json()['ask'])
    bb_sell = float(bb_request.json()['bid'])
    bs_request = requests.get('https://www.bitstamp.net/api/ticker/')
    bs_buy = float(bs_request.json()['high'])
    bs_sell = float(bs_request.json()['low'])

    if bb_sell < bs_sell:
        print('We recommend you to sell BTC on BitBay.')
    else:
        print('We recommend you to sell BTC on BitStamp.')

    if bb_buy > bs_buy:
        print('We recommend you to buy BTC on BitBay.')
    else:
        print('We recommend you to buy BTC on BitStamp')


bitbay_ticker()
print('\n')
bitbay_vs_bitstamp()

import requests
import time
from random import gauss
from numpy import arange
from scipy.stats import norm
from statistics import median
from matplotlib.pyplot import bar, show, grid, xlabel, ylabel, title, legend, savefig, gca


future = []
volume = []
change = []


def request(market, days):
    timestamp = str(int(time.time()) - 86400 * days)
    url = f"https://www.bitstamp.net/api/v2/ohlc/{market}usd?step=86400&limit=100&start={timestamp}"
    answer = requests.get(url).json()['data']['ohlc']
    for index in range(0, len(answer) - 1):
        volume.append(float(answer[index]['volume']))
        change.append(absolute((volume[index] - volume[index - 1]) / volume[index]))
    return change, volume


def absolute(value):
    if value > 1:
        return value - 1
    if value < -1:
        return value + 1
    return value


def plotsy(data, volumens):
    avg, std = norm.fit(data)
    predict = absolute(gauss(avg, std))
    future.append(predict * volumens[-1] + volumens[-1])
    grid(color='gray', which='major',alpha=0.5, linestyle='dashed', axis='y')
    bar(arange(0, len(volumens)), volumens, color='#005c99')
    bar(arange(len(volumens), len(future) + len(volumens)), future, color='#33adff')
    ylabel("amount of Volume")
    legend(['Historical data','Predicted data'])
    ax = gca()
    ax.set_facecolor('#ebebe0')


def main(market, days):
    change, volume = request(market, days)
    for i in range(days):
        plotsy(change, volume)
    title(f"Prediction of volume {market.upper()} for next {days} days",fontdict={'fontsize':15})
    xlabel(f"last {days} days                               next {days} days")
    savefig('chart')
    show()


main('btc', 30)

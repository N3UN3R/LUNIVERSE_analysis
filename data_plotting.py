from matplotlib import pyplot as plt

def plot_market_price_data(market_prices):

    market_prices['market price 2019'].plot(figsize=(15,5),linewidth = 0.8)
    market_prices['market price 2020'].plot(figsize=(15,5),linewidth = 0.8)
    plt.legend(loc='best')
    #market_prices['market price 2021'].plot(figsize=(15,5),linewidth = 0.8)
    #market_prices['market price 2022'].plot(figsize=(15,5),linewidth = 0.8)
    plt.savefig('preise.png')


    return None

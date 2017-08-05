import bittrex

Rex = bittrex.Bittrex(api_key="", api_secret="")


def get_market_symbols():
    res = Rex.get_markets()
    coins = res.get('result')
    coin_names = []

    for coin in coins:
        base = coin.get('BaseCurrency')
        isActive = coin.get('IsActive')
        if isActive:
            if base == "BTC":
                name = coin.get('MarketCurrency')
                coin_names.append(name)

    return coin_names

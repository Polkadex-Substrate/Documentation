import shrimpy
import time

# Provide the name of the exchange that you need to get trades per second ( it should be
# supported by Shrimpy)
exchange = 'Binance'

# If you have a paid token of Shrimpy include it here.
api_client = shrimpy.ShrimpyApiClient("", "")

trading_pairs = api_client.get_trading_pairs(exchange)
max_bids = 0
max_asks = 0
for pair in trading_pairs:
    orderbooks = api_client.get_orderbooks(
        exchange,  # exchange
        pair['baseTradingSymbol'],  # base_symbol
        pair['quoteTradingSymbol'],  # quote_symbol
        10000  # limit
    )
    print(pair['quoteTradingSymbol']+"/"+pair['baseTradingSymbol'])
    print("Asks Depth: ", len(orderbooks[0]['orderBooks'][0]['orderBook']['asks']))
    print("Bids Depth: ", len(orderbooks[0]['orderBooks'][0]['orderBook']['bids']))

    max_asks = max(max_asks,len(orderbooks[0]['orderBooks'][0]['orderBook']['asks']))
    max_bids = max(max_bids,len(orderbooks[0]['orderBooks'][0]['orderBook']['bids']))
    time.sleep(6)

print(" The maximum bids depth: ",max_bids)
print(" The maximum asks depth: ",max_asks)

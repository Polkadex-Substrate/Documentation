import shrimpy
import time

# Provide the name of the exchange that you need to get trades per second ( it should be
# supported by Shrimpy)
exchange = 'binance'
# Provide the start and end dates
start_date = "2020-07-01"
end_date = "2020-08-01"
# If you have a paid token of Shrimpy include it here.
api_client = shrimpy.ShrimpyApiClient("", "")

# Here we are getting all the trading pairs of the given exchange and getting it's trade count.
trading_pairs = api_client.get_trading_pairs(exchange)
total_count = 0
for i in range(len(trading_pairs)):
    count = api_client.get_historical_count(
        'trade',
        exchange,
        trading_pairs[i]["baseTradingSymbol"],
        trading_pairs[i]["quoteTradingSymbol"],
        start_date + 'T01:00:00.000Z',
        end_date + 'T02:00:00.000Z')
    print("Progress: ", i + 1,
          "/" + str(len(trading_pairs)) + " Trade Pair Count: " + str(count['count']) + " - " + trading_pairs[i][
              "baseTradingSymbol"] + "/" +
          trading_pairs[i]["quoteTradingSymbol"] + " Total Trades: ", total_count)
    total_count = total_count + count['count']
    time.sleep(7) # Remove this sleep if you have paid token from Shrimpy
print("Total Trades in one month: {}", total_count)
print("Average Trades per second: {}", float(total_count) / float((30 * 24 * 60 * 60)))

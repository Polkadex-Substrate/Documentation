# Polkadex Market Analysis :monocle_face:

We have provided a python script to get the current trades per second at centralized exchanges. It uses [Shrimpy API](https://developers.shrimpy.io/) to get the analytics.

## Installing Shrimpy 
```python
pip install shrimpy-python
```

## Run
Shrimpy has rate limiting of 1 request per 7 secs when used without paid token. If you have a paid for Shrimpy then use the the public key and private key as shown in the get-transactions-per-second-of-exchanges.py . We have include sleep of 7 seconds to use the script without a paid token, but it will take about 90 mins to complete.
'''python
python get-transactions-per-second-of-exchanges.py
'''

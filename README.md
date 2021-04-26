# binance-bot

## Prerequisites:
Python3 (with binance libarary.)

# preparation
obtain your binance API from www.binance.com and save in config.py file


## check balance:
```
 python balance.py coin_symbol #e.g BNB, BTC, ETH
 ```

## Automatic trade:
 ```
python trade.py coinpair_symbol amount_to_buy  #e.g python trade.py BNBUSDT 50
```
when price fall by 20% the bot will audomatically buy the token.
when the price raise by 20% or more the bot will automatically sell the token and wait until the price fall to buy again.


## Disclaimer
use the product at your own risk. 

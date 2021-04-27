import time

import config
import sys
from binance.client import Client
from binance.enums import *

self = Client(config.api_key, config.api_secret)
symbol = sys.argv[1]
amount = sys.argv[2]

def create_sell(symbol, amount, price):
    order = self.create_order(
        symbol=symbol,
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=amount,
        price=price)
    if 'msg' in order:
        Messages.get(order['msg'])

    # Buy order created.
    return order

def create_buy(symbol, amount, price):
    order = self.create_order(
        symbol=symbol,
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=amount,
        price=price)
    if 'msg' in order:
        Messages.get(order['msg'])

    # Buy order created.
    return order

# def monitor(symbol):
#     try:
#
#
#     except Exception as e:
#         return None
buy_sell = True
def main(symbol):
    def get_price(symbol):
        info = self.get_ticker(symbol=symbol)
        price_change = info['priceChangePercent']
        current_price = info['lastPrice']
        return price_change, current_price

    price_change, current_price = get_price(symbol)
    buy_sell = True
    if ((float(price_change) > 20) and (buy_sell == True)):
        print('sell 10% of ' + symbol)
        coin = symbol[:3]
        # 10% of the total coins have
        amount_to_sell = (float(self.get_asset_balance(asset=coin)['free']) * 0.2)
        order_info = create_sell(symbol, amount_to_sell, current_price)
        sell_order_id = order_info['orderId']
        
        # print('Sell order create id: %d' % sell_id)
        self.logger.info('Sell order create id: %d' % sell_order_id)
        
        time.sleep(self.WAIT_TIME_CHECK_SELL)
        
        if order_info['status'] == 'FILLED':
            # Database log
#             Database.write([sell_order_id, symbol, 0, current_price, 'SELL', amount])
            print('order successfully filled')
        buy_sell = False


    elif ((float(price_change) < -20) and (buy_sell == False)):
        print('buy the coins')
        coin = symbol[:3]
        # money earn from the last coins sold
        # from the dataset get the value of the coin sell
        money = 1;
        amount_to_buy = money / current_price
        order_info = create_buy(symbol, amount_to_buy, current_price)
        buy_order_id = order_info['orderId']
    
        # print('Sell order create id: %d' % sell_id)
        self.logger.info('Sell order create id: %d' % buy_order_id)
    
        time.sleep(self.WAIT_TIME_CHECK_BUY)
    
        if order_info['status'] == 'FILLED':
            # Database log
#             Database.write([buy_order_id, symbol, 0, current_price, 'BUY', amount])
            print('order successfully filled')
        buy_sell = True
    
    else:
        print('hold the coins')
#         print(current_price)


def Main():
    bot_controller = main(symbol)
    while True:
        try:
            bot_controller()
        except KeyboardInterrupt:
            return
        time.sleep(60)


if __name__ == '__main__':
    Main()



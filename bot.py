import gdax, pricelvl, threshold, trade, filled
public_client = gdax.PublicClient()
auth_client = gdax.AuthenticatedClient('1b71ebd92196b155d567b014d2cb855c',
                                       'jgn4yt3XvxqytaZS38QNolw/Or7nhVLqNke5fPYHgzby2aDQagGUMFkFhD013fXeHABQpslIHU41Ts7nkZeCeg==',
                                       'l5klovqzb8a')

id = 'LTC-USD'
cryptobalance = 0
mFactor = 0.0001 #0.0015
''' want to be able to input id(of what trading i am doing for the day), 
    passphrase, api_secret, 
    api key before program starts to run things more smoothly
    also add "recommended percentage" at beginning, otherwise can set own threshold percentages'''
account = auth_client.get_accounts()
''' auth_client.get_accounts() set equal to list[]
    list[0] is USD account
    list[1] is BTC account
    list[2] is LTC account
    list[3] is ETH account'''
usd_stats = account[0]
if 'BTC-USD' in id:
    cryptoBalance = 1
elif 'LTC-USD' in id:
    cryptoBalance = 2
elif 'ETH-USD' in id:
    cryptoBalance = 3

print(usd_stats)
crypto_stats = account[cryptoBalance]

pricing_usd = pricelvl.Pricing()
pricing_usd.set_pid(id)
alert_threshold = threshold.Threshold()
alert_threshold.set_mFactor(mFactor)
trading_usd = trade.Trading()
trading_usd.set_values(id, mFactor)
check_filled = filled.TimeDifference()
firstArrayFill = auth_client.get_fills()[0]

first = 0
postPrice = 0
prePrice = 0
dxLarge = 0
selling = 0
limit = 0
thStatus = 0
ogPrice = 0
thPrice = 0


firstbuy = 1
x = 1
a = 1

while x == 1 & firstbuy == 1:
    firstFill = firstArrayFill[0]
    if a == 1:
        price = pricing_usd.get_dx_stats(a, prePrice, postPrice,)
        if price != 0:
            a = 0
            prePrice, postPrice, dx, latest_time = float(price[0]), float(price[1]), float(price[2]), price[3]
            if first == 0:
                ogPrice = alert_threshold.set_ogPrice(postPrice)
            if first == 1:
                stats = alert_threshold.th_reached(dxLarge, dx, postPrice)
                thStatus, dxLarge = stats[0], stats[1]
#                if thStatus == 1:
#                    trade_update = trading_usd.transaction(ogPrice, selling, dxLarge, crypto_stats['balance'], usd_stats['balance'])
#                    selling, dxLarge, limit = trade_update[0], trade_update[1], trade_update[2]
#                if check_filled.check_filled(firstFill['created_at'], latest_time) == 0:
            else:
                first = 1
          #  alert_threshold.clear()
            print('\n' * 10)
            print('ogPrice:', ogPrice)
            print(dxLarge)
            print('Price at:', postPrice)
            print('limit:', limit)

    else:
        price = pricing_usd.get_dx_stats(a, prePrice, postPrice)
        if price != 0:
            a = 1
            prePrice, postPrice, latest_time = float(price[0]), float(price[1]), price[2]
    try:
        if float(auth_client.get_orders()[0][0]['price']) != float(limit) or \
                abs(float(limit) - float(postPrice)) >= float(mFactor * ogPrice):
            limit = alert_threshold.limit_set(ogPrice, selling)
            if ogPrice != alert_threshold.change_ogPrice(selling, postPrice, dx):
                ogPrice = alert_threshold.change_ogPrice(selling, postPrice, dx)
                dxLarge = 0
    except Exception as e:
        limit = alert_threshold.limit_set(ogPrice, selling)
        if ogPrice != alert_threshold.change_ogPrice(selling, postPrice, dx):
            ogPrice = alert_threshold.change_ogPrice(selling, postPrice, dx)
            dxLarge = 0

#    trading_usd.limit_set(ogPrice, selling, limit)
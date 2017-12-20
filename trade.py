import gdax, threshold, filled
auth_client = gdax.AuthenticatedClient('1b71ebd92196b155d567b014d2cb855c',
                                       'jgn4yt3XvxqytaZS38QNolw/Or7nhVLqNke5fPYHgzby2aDQagGUMFkFhD013fXeHABQpslIHU41Ts7nkZeCeg==',
                                       'l5klovqzb8a')

limitAt = 0
check_filled = filled.TimeDifference()
class Trading():

    def set_values(self, p_id, factor):
        global pid, mFactor
        pid = p_id
        mFactor = factor

    def order_limit(self):
      #  auth_client.buy(price=limitAt, size=cbalance, product_id=pid)
        print('limit ordered')

    def transaction(self, currentPrice, selling, dxLarge, cBalance, ubalance):
        global pid, mFactor
 #       limitAt = 0
        if selling == 0 and float(ubalance) > 0:
            if (((1 + mFactor) * float(currentPrice) - float(currentPrice)) >= 1):
                limitAt = (float(currentPrice) + ((1 + mFactor) * float(currentPrice) - float(currentPrice)))
            else:
                limitAt = (float(currentPrice) + 1)
#            auth_client.buy(price = limitAt, size = cbalance, product_id = pid)
#            print('BUYING: Limit set at: ', limitAt)
#            print('Amount (USD):', ubalance, 'Amount (', pid, '): ', cbalance)
        elif selling == 0 and ubalance == 0:
           print('Insufficient funds for purchase')
        elif selling == 1 and ubalance == 0:
            if (float(currentPrice) - ((1 - mFactor) * float(currentPrice)) >= 1):
                limitAt = ((1 - mFactor) * float(currentPrice))
            else:
                limitAt = (float(currentPrice) - 1)
#            auth_client.buy(price = limitAt, size = c_amount, product_id = pid)
#            print('SELLING: Limit set at:', limitAt)
#            print('Amount (USD):', ubalance, 'Amount (', pid, '): ', c_amount)
        dxLarge = 0
        return selling, dxLarge, limitAt
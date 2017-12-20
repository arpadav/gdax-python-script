import os\
    #, trade

#trading_usd = trade.order_limit()

class Threshold():

    def clear(self):
        os.system('cls')

    def set_mFactor(self, factor):
        global mFactor, thStatus
        mFactor = factor
        thStatus = 0

    def set_ogPrice(self, postPrice):
        global ogPrice
        ogPrice = postPrice
        return ogPrice

    def change_ogPrice(self, selling, currentPrice, dx):
        global ogPrice
        if selling == 0 and dx < 0 and ogPrice > currentPrice:
            ogPrice = currentPrice
            trading_usd
        elif selling == 1 and dx > 0 and ogPrice < currentPrice:
            ogPrice = currentPrice
        return ogPrice

    def limit_set(self, oggPrice, selling):
        global mFactor
        if selling == 0:
            return (oggPrice + (mFactor * oggPrice))
        else:
            return (oggPrice - (mFactor * oggPrice))

    def th_reached(self, dxLarge, dx, price):
        global thStatus
        dxLarge += dx
        if (dxLarge >= (mFactor * float(price))):
            thStatus = 1
            #set limit to buy (price is going up)
        elif (dxLarge <= (-mFactor * float(price))):
            thStatus = 1
            #set limit to sell (price is going down)
        else:
            thStatus = 0
        return thStatus, round(dxLarge, 5)
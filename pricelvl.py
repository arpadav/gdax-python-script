import gdax, time
public_client = gdax.PublicClient()

class Pricing():

    def set_pid(self, p_id):
        global pid
        pid = p_id

    def get_dx_stats(self, switch, price1, price2):
        try:
            ticker = public_client.get_product_ticker(product_id = pid)
            if switch == 1:
                try:
                    price2 = float(ticker['price'])
                    latest_time = ticker['time']
                    dx = round(float(price2) - float(price1), 5)
                    time.sleep(0.05)
                    return [price1, price2, dx, latest_time]
                except Exception as e:
                    time.sleep(0.001)
                    return 0
            else:
                try:
                    price1 = price2
                    price2 = float(ticker['price'])
                    latest_time = ticker['time']
                    time.sleep(0.05)
                    return [price1, price2, latest_time]
                except Exception as e:
                    time.sleep(0.001)
                    return 0
        except Exception as x:
            time.sleep(0.001)


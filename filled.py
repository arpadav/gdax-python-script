from datetime import datetime

class TimeDifference():

    def check_filled(self, latest_fill, latest_trade, previous_lf):
        latest_fill = latest_fill[:19]
        latest_trade = latest_trade[:19]
        latest_fill = latest_fill.replace('T', ' ')
        latest_trade = latest_trade.replace('T', ' ')
        lf_object = datetime.strptime(latest_fill, "%Y-%m-%d %H:%M:%S")
        lt_object = datetime.strptime(latest_trade, "%Y-%m-%d %H:%M:%S")
        delta_time = ()

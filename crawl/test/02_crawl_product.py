from crawl.api_caller import Crawler
from parse.auction_data_parser import Parser
import pandas as pd



# for date in dates:
dr = pd.date_range(start='20210517', end='20210517')
dates = dr.strftime('%Y%m%d').tolist()
cr = Crawler()
pa = Parser()

key = 'v8R92DMtagXwEBkXpUTDVeMnGRfqgBxl5hLAo7ZiHza6nYFzFfTmCbCxhaQ%2BtAcxai0C02ae8APsMciGrKd5xg%3D%3D'
for info in cr.get_target_prdcd()[137:]:
    code = info['prdcd']
    date = '20210526'
    r = cr.call_api(key, date, code)
    r = pa.calc_value(r)
    agg_result = []
    cr.save_data_into_db(r, date, code, info['prdnm'])



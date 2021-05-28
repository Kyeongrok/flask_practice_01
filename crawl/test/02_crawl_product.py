from crawl.api_caller import Crawler

cr = Crawler()

key = 'v8R92DMtagXwEBkXpUTDVeMnGRfqgBxl5hLAo7ZiHza6nYFzFfTmCbCxhaQ%2BtAcxai0C02ae8APsMciGrKd5xg%3D%3D'
for info in cr.get_target_prdcd()[126:]:
    code = info['prdcd']
    date = '20210527'
    r = cr.call_api(key, date, code)
    # print(r)
    cr.save_data(r, f'./20210529/{code}.json')
    # cr.save_data_into_db(r, date, code, info['prdnm'])



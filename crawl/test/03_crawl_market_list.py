from crawl.api_caller import Crawler

cr = Crawler()

key = 'v8R92DMtagXwEBkXpUTDVeMnGRfqgBxl5hLAo7ZiHza6nYFzFfTmCbCxhaQ%2BtAcxai0C02ae8APsMciGrKd5xg%3D%3D'
r = cr.call_api(key, '20210602', '1002', 'exact_market')

for item in r:
    print(item['stdPrdlstNm'], item)
print(len(r))
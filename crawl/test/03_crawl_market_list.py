from crawl.api_caller import Crawler

cr = Crawler()

key = 'v8R92DMtagXwEBkXpUTDVeMnGRfqgBxl5hLAo7ZiHza6nYFzFfTmCbCxhaQ%2BtAcxai0C02ae8APsMciGrKd5xg%3D%3D'
r = cr.call_api_market_list(key, '20210525', '110001')

# 모든 시장 리스트

print(len(r))
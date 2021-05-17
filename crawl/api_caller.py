import requests, json
import pandas as pd
import os
from parse.auction_data_parser import Parser

def call_api(key, date, prd_cd, limit=30000):
    url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
    data = requests.get(url)
    try:
        jo = json.loads(data.content)
        body = jo['response']['body']
        total_cnt = body['totalCount']
        print('total_cnt:', total_cnt)

        items = body['items']
        if items == '':
            return []
        return items['item']
    except Exception as e:
        print(date, prd_cd, e)

def save_data(data, target_filename):
    # data가 없다면 저장하지 않는다.
    if len(data) == 0:
        print(f'{target_filename} size:{len(data)} 저장하지 않습니다.')
        return 1

    #filename, path분리하기
    location, filename = os.path.split(target_filename)

    # dir이 없다면 생성합니다.
    print(os.path.isdir(location))
    if not os.path.isdir(location):
        os.makedirs(location)

    # file저장
    with open(target_filename, 'w+') as f:

        if isinstance(data, dict): # 1개인경우 dict로 오기 때문에 감싸줌
            data = [data]
        # whsalMrktNewCode별로 구분해서 저장
        data = Parser().make_map(data, 'whsalMrktNewCode')
        f.write(json.dumps(data))
        print(f'{target_filename} saved...')



if __name__ == '__main__':
    dr = pd.date_range(start='20210514', end='20210514')
    dates = dr.strftime('%Y%m%d').tolist()
    print(dates)


    for date in dates:
        for l in open('std_prd_cd.csv').readlines()[1043:1045]:
            code = l.replace('\n', '')
            print(code)
            key = 'Opchl4dUTt5YAAlLu0c%2BsGORkwekJdrfjhlKff2NiYhU%2FaEulm5Wk9fIJH2My7jhE9snVCr83ymkEj%2BLMj99Uw%3D%3D'
            r = call_api(key, date, code)
            print('r:', r)
            save_data(r, f'./{date}/{code}.json')

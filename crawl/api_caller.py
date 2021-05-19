import requests, json
import pandas as pd
import os
from flaskblog.domain.dynamo_table import Table

from parse.auction_data_parser import Parser

class Crawler():
    def __init__(self):
        self.t = Table('auction2')
        self.parser = Parser()

    def call_api(self, key, date, prd_cd, limit=30000):
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

    def save_data_into_db(self, data, delng_de, prd_cd):
        # data 저장
        if isinstance(data, dict):  # 1개인경우 dict로 오기 때문에 감싸줌
            data = [data]

        jo = data
        for value in jo:
            try:
                self.t.insert_into_db(self.parser.parse_float(value), date, prd_cd, value['rnum'])
                print(f"{value['rnum']}/{len(data)}", 'has been succeed')
            except Exception as e:
                print(e)
        print(f'{delng_de} {prd_cd} crawl finished')

        # data저장이 완료 되면 pk:<date> sk:CRAWL#<prd_cd>로 total count를 저장한다.
        row = {
            'date': f'{delng_de}',
            'prdcd_whsal_mrkt_new_cd': f'CRAWL#{prd_cd}',
            'total_cnt': len(data)
        }
        self.t.insert(row)


    def get_target_prdcd(self, delng_de):
        '''
        :param delng_de: %Y%m%d 형식
        :return 데이터를 수집할 대상을 []로
        '''

        t = []

        # 이전에 수집된 결과를 dynamodb에서 select합니다.


        for l in open('std_prd_cd.csv').readlines():
            t.append(l.replace('\n', ''))
        return t

    def save_data(self, data, target_filename):
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

        # file로 저장하지 말고 db로 바로 저장하고 결과를 보여주게
        # file저장
        with open(target_filename, 'w+') as f:

            if isinstance(data, dict): # 1개인경우 dict로 오기 때문에 감싸줌
                data = [data]
            # whsalMrktNewCode별로 구분해서 저장
            # data = Parser().make_map(data, 'whsalMrktNewCode')
            f.write(json.dumps(data))
            print(f'{target_filename} saved...')



if __name__ == '__main__':
    dr = pd.date_range(start='20210517', end='20210517')
    dates = dr.strftime('%Y%m%d').tolist()
    print(dates)
    cr = Crawler()

    # for date in dates:
    # 오늘 날짜에 이미 수집한 prd_cd는 뺀다.
    date = '20210517'

    for code in cr.get_target_prdcd(date)[127:]:
        key = 'Opchl4dUTt5YAAlLu0c%2BsGORkwekJdrfjhlKff2NiYhU%2FaEulm5Wk9fIJH2My7jhE9snVCr83ymkEj%2BLMj99Uw%3D%3D'
        r = cr.call_api(key, date, code)
        # cr.save_data(r, f'./{date}/{code}.json')
        cr.save_data_into_db(r, date, code)

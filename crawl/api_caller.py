import requests, json
import pandas as pd
import os, csv
from datetime import datetime
from flaskblog.domain.dynamo_table import Table

from parse.auction_data_parser import Parser
os.chdir(os.path.dirname(__file__))

class Crawler():
    def __init__(self):
        self.t = Table('auction2')
        self.parser = Parser()

    def call_api(self, key, date, prd_cd, api_type='normal', limit=30000):
        if api_type == 'normal':
            url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
        elif api_type == 'exact_market':
            url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactMarketPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&_type=json'
        else:
            url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getRealProdPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&delngDe={date}&prdlstCd={prd_cd}&_type=json'
        data = requests.get(url)
        print(data, url)
        try:
            jo = json.loads(data.content)
            body = jo['response']['body']
            total_cnt = body['totalCount']
            print(f'{prd_cd} total_cnt:{total_cnt} {datetime.now()}')

            items = body['items']
            if items == '':
                return []
            return items['item']
        except Exception as e:
            print(date, prd_cd, e)
            return []

    def call_api_market_list(self, key, date, whsal_cd, api_type='normal', limit=30000):
        if api_type != 'real_time':
            url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getExactMarketPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&whsalCd={whsal_cd}&delngDe={date}&_type=json'
        else:
            url = f'http://apis.data.go.kr/B552895/openapi/service/OrgPriceAuctionService/getRealMarketPriceList?ServiceKey={key}&pageNo=1&numOfRows={limit}&whsalCd={whsal_cd}&delngDe={date}&_type=json'
        print(url)
        data = requests.get(url)
        try:
            jo = json.loads(data.content)
            body = jo['response']['body']
            total_cnt = body['totalCount']
            print(f'{date} total_cnt:{total_cnt} {datetime.now()}')

            items = body['items']
            if items == '':
                return []
            return items['item']
        except Exception as e:
            print(date, e)
            return []

    def save_data_into_db(self, parse_result, delng_de, prd_cd, prd_nm):
        # data 저장

        succeed = 0
        for value in parse_result['data']:
            try:
                self.t.insert_into_db(self.parser.parse_float(value), delng_de, prd_cd, value['rnum'])
                succeed += 1
            except Exception as e:
                print('during insert into db', e)
        print(f'{delng_de} {prd_cd} crawl finished at {datetime.now()} total:{parse_result["cnt"]} succeed:{succeed}')

        # 0보다 커야 insert
        if parse_result['cnt'] > 0:
            # data저장이 완료 되면 pk:<date> sk:CRAWL#<prd_cd>로 total count를 저장한다.
            row = {
                'date': f'{delng_de}',
                'prdcd_whsal_mrkt_new_cd': f'CRAWL#{prd_cd}',
                'total_cnt': parse_result['cnt'],
                # 'mean_sbid_pric': parse_result['mean_sbid_pric'],
                # 'sum_sbid_pric': parse_result['sum_sbid_pric'],
                'prd_nm': prd_nm
            }
            self.t.insert(row)


    def get_target_prdcd(self, type='list'):
        '''
        :param delng_de: %Y%m%d 형식
        :return 데이터를 수집할 대상을 []로
        '''

        t = []
        m = {}
        # 이전에 수집된 결과를 dynamodb에서 select합니다.
        for l in self.read_csv_file_into_list('./std_prd_cd.csv', delimiter='\t'):
            t.append({'prdcd':l[0], 'prdnm':l[1]})
            m[l[0]] = l[1]

        if type == 'list':
            return t
        elif type == 'map':
            return m
        else:
            print('error')

    def read_csv_file_into_list(self, filename, delimiter=',', encoding='utf-8'):
        with open(filename, newline='', encoding=encoding) as f:
            ll = csv.reader(f, delimiter=delimiter)
            return list(ll)

    def save_data(self, data, target_filename):
        # data가 없다면 저장하지 않는다.
        print(f'start save data({data["cnt"]}) into file {target_filename}')
        if data['cnt'] == 0:
            print(f'{target_filename} size:{data["cnt"]} 저장하지 않습니다. 데이터 개수 0개')
            return 1

        #filename, path분리하기
        location, filename = os.path.split(target_filename)

        # dir이 없다면 생성합니다.
        print(f'{location} isdir:', os.path.isdir(location))
        if not os.path.isdir(location):
            os.makedirs(location)

        # file로 저장하지 말고 db로 바로 저장하고 결과를 보여주게
        # file저장
        with open(target_filename, 'w+') as f:
            # whsalMrktNewCode별로 구분해서 저장
            # data = Parser().make_map(data, 'whsalMrktNewCode')
            f.write(json.dumps(data))
            print(f'{target_filename} saved...')

if __name__ == '__main__':
    cr = Crawler()


from crawl.api_caller import Crawler
from glob import glob
import json
from crawl.aggr.aggregator import agg
from flaskblog.domain.dynamo_table import Table

t = Table('auction2')

def insert_agg(jo, date, prdcd):
    # agg해서 insert합니다.
    m = agg(jo['data'])
    t.insert({
        'date': f'{date}',
        'prdcd_whsal_mrkt_new_cd': f'CRAWL#{prdcd}',
        'total_cnt': jo['cnt'],
        'prd_nm': m_prdcd_nm[prdcd],
        'agg': m,
    })
    print('success agg insert')

cr = Crawler()

fnms = glob('../crawl/20210602/*.json')
m_prdcd_nm = cr.get_target_prdcd('map')

for fnm in fnms[1:]:
    delngde, prd_cd = fnm.replace('../crawl/', '').replace('.json','').split('/')
    with open(fnm) as f:
        print(delngde, prd_cd, m_prdcd_nm[prd_cd])
        jo = json.loads(f.read())
        cr.save_data_into_db(jo, delngde, prd_cd, m_prdcd_nm[prd_cd])
        insert_agg(jo, delngde, prd_cd)

# dir에 있는 모든 json


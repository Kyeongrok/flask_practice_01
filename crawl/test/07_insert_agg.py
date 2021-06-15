# file읽어서
from glob import glob
import json
from crawl.aggr.aggregator import agg
from flaskblog.domain.dynamo_table import Table
from crawl.api_caller import Crawler

def prdnm_map():
    m = {}
    cr = Crawler()

    for info in cr.get_target_prdcd():
        if m.get(info['prdcd']) == None:
            m[info['prdcd']] = info['prdnm']
    return m


if __name__ == '__main__':
    t = Table('auction2')
    fns = glob('../crawl/20210602/*.json')
    print(len(fns))
    m_prdnm = prdnm_map()

    for fn in fns:
        with open(fn) as f:
            fn = fn.replace('../crawl/', '').replace('.json', '')
            date, prdcd = fn.split('/')
            jo = json.loads(f.read())
            insert_agg(jo, date, prdcd)

from parse.auction_data_parser import Parser
from flaskblog.domain.dynamo_table import Table
import glob

if __name__ == '__main__':
    t = Table('auction2')

    # insert
    p = Parser()
    fl = glob.glob('../crawl/20210514/'+"*.json")
    for fn in fl[:1]:
        print('start load file', fn)
        date, prd_cd = fn.replace('../crawl/', '').replace('.json', '').split('/')
        jo = p.load_json_file(fn)
        sbid_pric_sum = 0
        for item in jo:
            print(item['stdUnitNewNm'], item[''], item['sbidPric'], type(item['sbidPric']))
        # print(len(jo))

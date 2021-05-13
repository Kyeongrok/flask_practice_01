from flaskblog.domain.dynamo_table import Table
import glob, json
from test.auction_data_parser import Parser


def file_insert_into_db(fn):
    p = Parser()
    jo = p.load_json_file(fn)
    sp = fn.replace('./data\\', '').replace('.json', '').split('_')
    row = {
        'date': f'RAW#{sp[0]}',
        'prdcd_whsal_mrkt_new_cd': f'{1202}#{sp[1]}',
        'data1': jo
    }
    try:
        t.insert(row)
    except Exception as e:
        print(e)
        print('error:', fn)
        exit(0)


if __name__ == '__main__':
    t = Table('auction2')

    # insert
    fl = glob.glob('./data/'+"*.json")
    for fn in fl[23:1000]:
        print(fn)
        file_insert_into_db(fn)
        print(f'{fn} finished')
        # file_insert_into_db('./data/20200102_350301.json')






from flaskblog.domain.dynamo_table import Table
import glob
from parse.auction_data_parser import Parser


def file_insert_into_db(jo, date, sk, rnum):
    # print(jo)
    row = {
        'date': f'{date}',
        'prdcd_whsal_mrkt_new_cd': sk,
        'data1': jo
    }
    try:
        t.insert(row)
    except Exception as e:
        print(e)
        print('error:', date, prd_cd, rnum)
        exit(0)


if __name__ == '__main__':
    t = Table('auction2')

    # insert
    p = Parser()
    fl = glob.glob('../crawl/20210514/'+"*.json")
    for fn in fl[26:100]:
        print('start load file', fn)
        date, prd_cd = fn.replace('../crawl/', '').replace('.json', '').split('/')
        jo = p.load_json_file(fn)
        print('insert started ', fn, len(jo))
        # jo = p.make_map(jo, 'whsalMrktNewCode')
        for row in jo:
            try:
                t.insert_into_db(row, date, prd_cd, row['rnum'])
                print(row['rnum'], 'has been succeed')
            except Exception as e:
                print(e)
        print(f'{fn} finished')






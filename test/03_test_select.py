from flaskblog.domain.dynamo_table import Table
import ast, json
import decimal
from libs.DecimalEncoder import DecimalEncoder


if __name__ == '__main__':
    t = Table('auction2')
    r = t.select_by_pk('20210514')
    tot = 0
    for k, v in r.items():
        if k != 'Items':
            print(k, v)
        elif k == 'Items':
            print('Items:', len(v))

    # for i in r['Items']:
    #     d = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))
    #     for row in d['data1']:
    #         print(row)
    #         # print(row['data1'])
    #         # print(row['delngDe'])
    #         tot += 1
    # print(tot)
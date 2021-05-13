from flaskblog.domain.dynamo_table import Table
import ast, json
import decimal
from libs.DecimalEncoder import DecimalEncoder


if __name__ == '__main__':
    t = Table('auction2')
    r = t.select_by_pk('RAW#20200102')
    tot = 0
    # print(r['Items'])
    for i in r['Items']:
        d = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))
        for row in d['data1']:
            print(row)
            # print(row['data1'])
            # print(row['delngDe'])
            tot += 1
    print(tot)
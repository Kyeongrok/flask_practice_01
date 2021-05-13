from flaskblog.domain.dynamo_table import Table
import ast, json
import decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return str(o)
        if isinstance(o, set):  #<---resolving sets as lists
            return list(o)
        return super(DecimalEncoder, self).default(o)

if __name__ == '__main__':
    t = Table('auction2')
    r = t.select_by_pk('RAW#20200102')
    # print(r['Items'])
    for i in r['Items']:
        # print(i)
        d = ast.literal_eval((json.dumps(i, cls=DecimalEncoder)))
        for row in d['data1']:
            print(row['delngPrut'])

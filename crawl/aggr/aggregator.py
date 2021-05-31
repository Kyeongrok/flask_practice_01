
from flaskblog.domain.dynamo_table import Table
from parse.auction_data_parser import Parser


def agg(jo):
    psr = Parser()
    m = {}
    for data1 in jo:
        # m['total_cnt'] += 1
        sum_1prut = 0
        # print(data1.get('stdFrmlcNewNm'))
        if m.get(data1['stdFrmlcNewNm']) == None:
            m[data1['stdFrmlcNewNm']] = {'cnt':0, 'sum_1prut':0}
        m[data1['stdFrmlcNewNm']]['cnt'] += 1

        # row당 1kg로 환산해서 더함
        m[data1['stdFrmlcNewNm']]['sum_1prut'] += round(data1['sbidPric'] / data1['delngPrut'], 2)
    for k1, value in m.items():
        for k2, v2 in m[k1].items():
            m[k1] = psr.parse_float(m[k1])

    return m

from flaskblog.domain.dynamo_table import Table
import csv, json


def read_csv_file_into_list(filename, delimiter=',', encoding='utf-8'):
    with open(filename, newline='', encoding=encoding) as f:
        ll = csv.reader(f, delimiter=delimiter)
        return list(ll)

def f():
    with open('std_prd_cd.json') as f:
        m = json.loads(f.read())

    r = t.select_pk_begins_with('20210521', 'CRAWL', limit=2000)

    for item in r['Items']:
        print(item['date'], item['prdcd_whsal_mrkt_new_cd'])
        prdcd = item['prdcd_whsal_mrkt_new_cd'].split('#')[1]
        ur = t.update_prdnm(item['date'], item['prdcd_whsal_mrkt_new_cd'], m[prdcd])
        print(ur)

def get_mean(items):
    # stdUnitNewNm
    for item in items:
        # delngPrut 거래되는 단위 매매단위명과 포장상태명을 조합하여 의미를 가지게 되는 숫자임
        # sbidPric, stdUnitNewNm
        data1 = item['data1']
        print(data1['stdUnitNewNm'], data1['stdMgNewNm'], data1['sbidPric'], data1['delngPrut'], data1['delngQy'])
        # print(item['data1'].get('stdUnitNewNm'))
        # print(item['stdUnitNewNm'])

if __name__ == '__main__':
    t = Table('auction2')

    prdcds = ['1001', '1010', '1011', '1012', '1014', '1015', '1016', '1017', '1019', '1020', '1021', '1022', '1023', '1024', '1027', '1028', '1029', '1030', '1031', '1034', '1035', '1036', '1037', '1038', '1039', '1041', '1043', '1050', '1051', '1052', '1053', '1055', '1057', '1063', '1099', '1101', '1102', '1103', '1104', '1105', '1106', '1107', '1201', '1202', '1204', '1205', '1207', '1208', '1209', '1210', '1213', '1216', '1301']
    r = t.select_pk_begins_with('20210525', f'RAW#{prdcds[0]}#')
    mean = get_mean(r['Items'])
    print(mean)

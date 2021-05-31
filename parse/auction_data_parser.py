import glob, json
from decimal import Decimal

class Parser():
    # db에 넣을 수 있는 모양으로 parsing해서 file에 저장하는 기능
    # float을 파싱하는 기능

    def calc_value(self, data):
        if isinstance(data, dict):  # 1개인경우 dict로 오기 때문에 감싸줌
            data = [data]

        sum_sbid_pric = 0
        cnt = len(data)

        # for item in data:
        #     # ton이면 kg단위로 변환 해줄 것
        #     # 단위가 ton인 것 문제 없는지? ton이면 가격이 *3으로 나올 것임
        #     mpk = int(round(item['sbidPric'] / item['delngPrut'], 0))
        #     sum_sbid_pric += item['sbidPric']
        #     item['mean_pric_per_prut'] = mpk
        #
        # if cnt > 0:
        #     mean_sbid_pric = int(round(sum_sbid_pric / cnt))
        # else:
        #     mean_sbid_pric = 0
        # return {'sum_sbid_pric':sum_sbid_pric, 'mean_sbid_pric':mean_sbid_pric, 'data':data, 'cnt':cnt}
        return {'data':data, 'cnt':cnt}

    def parse_float(self, d):
        '''
        float이 있으면 Decimal로 바꾼다
        :return:
        '''
        for key, value in d.items():
            # print(value, type(value), isinstance(value, float))
            if isinstance(value, float):
                value = round(value, 2) # float 2째자리에서 반올림
                dec_val = Decimal(str(value))
                value = dec_val
                d[key] = value
        return d

    def load_json_file(self, fn):
        r = []
        with open(fn) as f:
            jo = json.loads(f.read())
            if isinstance(jo, dict):
                jo = [jo]
            for i in jo:
                try:
                    r.append(self.parse_float(i))
                except Exception as e:
                    print(f'{__name__}', e)
                    exit(1)
        print('load and converted to Decimal finished...')
        return r

    def sieve_columns(self, l):
        r = []

        for item in l:
            r.append({'':''})

        return r

    def make_map(self, l, target_field='whsalMrktNewCode'):
        '''
        target_field별로 분리해서 map으로 만든다.
        :return: {'wsal1':[], ... }
        '''
        r = {}
        for item in l:
            if r.get(item[target_field]) == None:
                r[item[target_field]] = []

            r[item[target_field]].append(item)
        return r


if __name__ == '__main__':
    p = Parser()
    fn = '../crawl/20210514/1001.json'

    jo = p.load_json_file(fn)
    jo_whsal = p.make_map(jo, 'whsalMrktNewCode')
    print(len(jo))
    print(jo[0])



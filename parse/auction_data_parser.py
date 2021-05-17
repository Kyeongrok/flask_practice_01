import glob, json
from decimal import Decimal

class Parser():
    # db에 넣을 수 있는 모양으로 parsing해서 file에 저장하는 기능
    # float을 파싱하는 기능

    def parse_float(self, d):
        '''
        float이 있으면 Decimal로 바꾼다
        :return:
        '''
        for key, value in d.items():
            # print(value, type(value), isinstance(value, float))
            if isinstance(value, float):
                dec_val = Decimal(str(value))
                value = dec_val
                d[key] = value
        print('converted to Decimal finished...')
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



import glob, json
from decimal import Decimal

class Parser():
    # file로 저장하는 기능
    # db에 넣을 수 있는 모양으로 parsing하는 기능
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
                print(key, value, 'converted to Decimal')
        return d

    def load_json_file(self, fn):
        sp = fn.replace('./data\\', '').replace('.json', '').split('_')
        r = []
        with open(fn) as f:
            jo = json.loads(f.read())
            for i in jo:
                r.append(self.parse_float(i))
        return r


if __name__ == '__main__':
    p = Parser()
    fn = './data/20200102_350301.json'

    jo = p.load_json_file(fn)

    for i in jo:
        if i['rnum'] == 156:
            p.parse_float(i)


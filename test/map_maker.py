import json
# 해당 날짜로 필터링
# json을 불러옴


def make_map(l, target_field):
    r = {}
    for item in l:
        if r.get(item[target_field]) == None:
            r[item[target_field]] = []

        r[item[target_field]].append(item)
    return r

if __name__ == '__main__' :
    with open('./data/auction_price_onion_2020_2021.json', encoding='utf-8') as f:
        jo = json.loads(f.read())

    r = make_map(jo, 'delngDe')
    print(len(jo))
    print(len(r))

    with open('map_auction_price.json', 'w+') as f:
        f.write(json.dumps(r))

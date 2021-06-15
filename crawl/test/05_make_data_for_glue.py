import json

with open('../20210601/1001.json') as f:
    jo = json.loads(f.read())
    with open('../20210601/1001_glue.json', 'w+') as f2:
        f2.write(json.dumps(jo['data']))


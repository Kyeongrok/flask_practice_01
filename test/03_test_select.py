from flaskblog.domain.dynamo_table import Table

if __name__ == '__main__':
    t = Table('bbbee')
    r = t.select_all()
    print(r)


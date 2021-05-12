from flaskblog.domain.dynamo_table import Table

if __name__ == '__main__':
    t = Table('auction')

    # insert
    row = {
        'date':'RAW#2021-05-09',
        'prdcd_whsal_mrkt_new_cd':'1202#1054501',
        'price':'2000',
    }

    t.insert(row)


from flaskblog.domain.dynamo_table import Table

if __name__ == '__main__':
    t = Table('auction')
    t.select_pk_begins_with('2021-05-09')



# stdPrdlstCode 품목코드, date, whsalMrktNewCode
# 왜냐하면 위 두가지 데이터를 기준으로 저장됨

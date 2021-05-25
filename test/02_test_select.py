from flaskblog.domain.dynamo_table import Table

# def select_by_prdcd(date, prdcd):

if __name__ == '__main__':
    t = Table('auction2')
    date = '20210524'

    r = t.select_statistic(date)
    prdcds = ['1001', '1010', '1011', '1012', '1014', '1015', '1016', '1017', '1019', '1020', '1021', '1022', '1023', '1024', '1027', '1028', '1029', '1030', '1031', '1034', '1035', '1036', '1037', '1038', '1039', '1041', '1043', '1050', '1051', '1052', '1053', '1055', '1057', '1063', '1099', '1101', '1102', '1103', '1104', '1105', '1106', '1107', '1201', '1202', '1204', '1205', '1207', '1208', '1209', '1210', '1213', '1216', '1301']
    print(len(prdcds))
    for prdcd in prdcds[:10]:
        rb = t.select_pk_begins_with('20210524', f'RAW#{prdcd}')
        # # kg인것 filter
        print(date, prdcd, f'total:{len(rb["Items"])}' )
        cnt_kg = 0
        cnt_etc = 0
        for itm in rb['Items']:
            std_unit_nm = itm['data1']['stdUnitNewNm']
            if std_unit_nm == 'kg':
                cnt_kg += 1
            else:
                print(std_unit_nm)
                cnt_etc +=1

        print(cnt_kg, cnt_etc)

# stdPrdlstCode 품목코드, date, whsalMrktNewCode
# 왜냐하면 위 두가지 데이터를 기준으로 저장됨

# 전체 중에 kg의 비율은?

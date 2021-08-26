# how to run
* source venv/bin/activate
* python run.py

# Inprogress
* crawl로직 lambda로 배포하고 flask에서 parameter넘겨서 trigger하게
> date, prd_cd를 넘김
  
# Next
* 날짜별로 모든 데이터 수집
* 상품 코드표 ui만들기 -> table설계 PK가 stdPrdlstCode(품목코드)

# Solved
* column중에 float이 있는 경우 안들어가서 Decimal로 바꿔서 insert함
* 400KB 초과 하면 안됨 An error occurred (ValidationException) when calling the PutItem operation: Item size has exceeded the maximum allowed size
* crawl한 결과를 저장하는 기능
  > pk는 date, sk는 CRAWL#<prd_cd>
  > total_cnt, is_saved
* crawl_result에 작물명 입력되게
* 어제 어떤 작물이 몇건 평균가격 얼마로 sbidPric, stdUnitNewNm
* 평균 거래량
> 합계 낼 때 std_unit_new_nm이 kg또는 ton(100kg)인데 반영해서 계산
> 포장단위가 '상자'인 row의 sbidPric / delngPrut의 평균이 그날의 평균  
* bulk insert도입하기 지금은 너무 느림(insert제한 있어서 그렇슴)

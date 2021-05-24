from crawl.api_caller import Crawler

cr = Crawler()
r = cr.read_csv_file_into_list('./../std_prd_cd.csv', delimiter='\t')
print(r)

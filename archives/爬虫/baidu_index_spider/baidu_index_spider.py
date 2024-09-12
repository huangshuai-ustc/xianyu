import pandas as pd
from qdata.baidu_index import get_search_index

cookie = ('BAIDUID=16E4BBDE9537D5CBD5C0F83D3FEFFA3B:FG=1; BAIDUID_BFESS=16E4BBDE9537D5CBD5C0F83D3FEFFA3B:FG=1; '
          'BDUSS=kxVUlIYkNPbVZlU2dVc2RBZ2JnQ0hEM3J0RXhxVHBkWTdXY1Q2Rkw1RHV'
          '-UlZtRVFBQUFBJCQAAAAAAAAAAAEAAAAhyQBzZmp3eXppAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO5w7mXucO5lVW; bdindexid=7l5d31dpiu4ipc2q4p69ac9b32; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a04601428822Px6XFBjJUGIYgoV6wuqw44pVnqWp4oPnBB4Lcf%2F57KvdXlnbj11OqTfIAjOo7MYUMDpoAEyqcHg5KCgwHWOlvSQ57AJWNySO%2BKcTvjSc4dZNijNzicxytFeDstKZT8lD21onESm9oa9MytB8hhwqP72zfe57x6NdGQ6t16Cxgfvs4hYVPfTCf7LecsesLIgxqLY8e%2BHpbyyAsq7eKfw%2FcWplQEPRXOgM0mced3v9mDqs5ZBrOTzOEkVHDd812DZT2UV14SguK4NmoQQ%2F0HvuqA%3D%3D67162574229725845627191250717648; __cas__rn__=460142882; __cas__st__212=357e46b5096b7d43583cc1d1788c8a84cf42f72592ce48085428583d68fe518bef3b0db82a5e01447dec4030; __cas__id__212=53732907; CPTK_212=1725038410; CPID_212=53732907; BDUSS_BFESS=kxVUlIYkNPbVZlU2dVc2RBZ2JnQ0hEM3J0RXhxVHBkWTdXY1Q2Rkw1RHV-UlZtRVFBQUFBJCQAAAAAAAAAAAEAAAAhyQBzZmp3eXppAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO5w7mXucO5lVW; RT="z=1&dm=baidu.com&si=4f7a8be6-3d9b-4c83-92b1-b763776b98cb&ss=ltmfi76x&sl=6&tt=4sv&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=7ffs&ul=cft4"')
keywords_list = [['比亚迪新能源汽车']]
start_date = '2017-01-01'
end_date = '2023-12-31'

ALL_KIND = [['all'], ['pc'], ['wise']]
all_list = list(get_search_index(keywords_list=keywords_list,
                                 start_date=start_date, end_date=end_date, cookies=cookie, ALL_KIND=ALL_KIND[0]))
pc_list = list(get_search_index(keywords_list=keywords_list,
                                start_date=start_date, end_date=end_date, cookies=cookie, ALL_KIND=ALL_KIND[1]))
wise_list = list(get_search_index(keywords_list=keywords_list,
                                  start_date=start_date, end_date=end_date, cookies=cookie, ALL_KIND=ALL_KIND[2]))
df1 = pd.DataFrame(all_list)
df2 = pd.DataFrame(pc_list)
df3 = pd.DataFrame(wise_list)
df1.iloc[:, 0] = keywords_list[0][0]
data = pd.concat([df1.iloc[:, [0, 2, 3]], df2.iloc[:, -1], df3.iloc[:, -1]], axis=1)
data.columns = ['keyword', 'time', 'all', 'pc', 'wise']
data.to_excel('result.xlsx', index=False)

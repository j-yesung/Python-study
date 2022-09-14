# 네이버 영화 랭킹 가져오기
import time

import requests
from bs4 import BeautifulSoup

html = '''
<tr>
    <td class="ac">
        <img src="https://ssl.pstatic.net/imgmovie/2007/img/common/bullet_r_r01.gif" alt="01" width="14" height="13">
    </td>
    <td class="title">
        <div class="tit5">
            <a href="/movie/bi/mi/basic.naver?code=213364" title="인생은 뷰티풀: 비타돌체">인생은 뷰티풀: 비타돌체</a>
        </div>
    </td>
    <!-- 평점순일 때 평점 추가하기  -->
    <td>
        <div class="point_type_2">
            <div class="mask" style="width:98.4000015258789%">
                <img src="https://ssl.pstatic.net/imgmovie/2007/img/common/point_type_2_bg_on.gif" width="79" height="14" alt="">
            </div>
        </div>
    </td>
    <td class="point">9.84</td>
    <td class="ac">
        <a href="/movie/point/af/list.naver?st=mcode&amp;sword=213364" class="txt_link">평점주기</a>
    </td>
    <!----------------------------------------->  
    <td colspan="2" class="new_icon">
        <img width="20" height="5" alt="new" src="https://ssl.pstatic.net/imgmovie/2007/img/common/icon_new_1.gif">
    </td>
</tr>
'''
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20220912&page=4'

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.content, 'lxml')
# print(res)
mv_name = soup.select('div.tit5 > a')
mv_star = soup.select('td.point')
for i in range(50):
    print('영화:', mv_name[i].text, ', 평점:', mv_star[i].text)
# time.sleep(1) # 1초 실행 정지

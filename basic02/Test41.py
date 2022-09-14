# 네이버 IT 기사 헤드라인
import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=103'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
# 페이지 요청
res = requests.get(url, headers=headers)
# 파싱
soup = BeautifulSoup(res.content, 'lxml')

div_tag = soup.select('div.content')
# print(div_tag)
for a in div_tag:
    print(a.text.strip())

div_tag = soup.select('#main_content > div > div._persist > div:nth-child(1) > div:nth-child(2) > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > a')

# #main_content > div > c
# #main_content > div > div._persist > div:nth-child(1) > div:nth-child(2) > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > a
# #main_content > div > div._persist > div:nth-child(1) > div:nth-child(4) > div.cluster_body > ul > li:nth-child(1) > div.cluster_text > a
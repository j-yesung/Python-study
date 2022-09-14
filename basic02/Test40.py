# 네이버 뉴스
import requests
from bs4 import BeautifulSoup

url = 'https://n.news.naver.com/mnews/article/005/0001552410?sid=103'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
print(response)

# HTML 응답 페이지 파싱
soup = BeautifulSoup(response.content, 'lxml')
title = soup.find('title')
print(title)
print(title.text)

# 이미지 찾기
# select() : 여러개, 리스트로 리턴
# select_one() : 한개
img_tag = soup.select_one('#img1')
print(img_tag)
print(img_tag['data-src'])

# 이미지 파일 다운 : urllib.request > urlretrieve 함수
from urllib.request import urlretrieve # 함수 하나만 임포트
img_url = img_tag['data-src']
file_name = 'news_img.jpg'

# 다운 urlretreive (다운받을 데이터 url, 저장할 파일 경로)
urlretrieve(img_url, file_name)

# 뉴스 본문 가져와 출력
news_data = soup.find(id='dic_area')
txt = news_data.text
print(txt.news_data.text)




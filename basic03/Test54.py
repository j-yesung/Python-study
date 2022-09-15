# 데이터 정제, 분석, 시각화
import pandas as pd
import  matplotlib.pyplot as plt
from matplotlib import font_manager, rc # 한글깨짐 방지 처리 위한 모듈 임포트

# 한글깨짐 방지
font_path = r"C:\Users\tjoeun\AppData\Local\Microsoft\Windows\Fonts\D2Coding-Ver1.3.2-20180524-all.ttc"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

data = pd.read_csv('도로교통공단_시도시군구별교통사고통계.csv')
# print(data.head(10))

# 서울에서 사고건수가 가장 많은 데이터순
# data_acc = data[data['시도'] == '서울'].sort_values(by='사고건수', ascending=False)
# print(data_acc[['시도', '시군구', '사고건수']])
# print(data_acc.shape)

# 서울시 시군구별 교통사고 발생 top 10
# print(data_acc[['시도', '시군구', '사고건수']][:10])
# plt.figure(figsize=(10, 6))
# plt.title('서울시 시군구별 교통사고 발생 top 10')  # 제목 붙히기
# plt.bar(range(10), data_acc['사고건수'][:10])   # 막대 그래프
# plt.xticks(range(10), data_acc['시군구'][:10])  # x 축 단위 라벨
# plt.show()

# 전국 시도별 사고건수/사망자수 top 10
# '시도' 그룹
# print(data.groupby(by='시도'))
# print(data.groupby(by='시도').count())    # 시도별 구의 개수
# print(data.groupby(by='시도').sum()) # 그룹별 합계 (시도별 합계)
data_grby_city = data.groupby(by='시도', as_index=False).sum()
# print(data_grby_city.shape)
# print(data_grby_city.sort_values(by='사고건수', ascending=False))
# print(data_grby_city.sort_values(by='사망자수', ascending=False))
data_grby_city_sorted_acc = data_grby_city.sort_values(by='사고건수', ascending=False)
data_grby_city_sorted_death = data_grby_city.sort_values(by='사망자수', ascending=False)

# print(data_grby_city_sorted_acc['시도'])
# print(data_grby_city_sorted_acc['사고건수'])

# 그래프 그리기 : 사고건수 top 10
# plt.figure(figsize=(10, 6)) # 사이즈 지정
# plt.title('전국 시도별 교통 사고 발생 top 10')  # 제목 붙히기
# plt.bar(range(10), data_grby_city_sorted_acc['사고건수'][:10])   # 막대 그래프
# plt.xticks(range(10), data_grby_city_sorted_acc['시도'][:10])  # x 축 단위 라벨
# plt.savefig('전국시도별교통사고발생top10.png')
# plt.show()

# colors = ['red', 'yellow', 'purple', 'burlywood', 'lightcoral']
# plt.pie(data_grby_city_sorted_death['사망자수'][:10],
#     labels=data_grby_city_sorted_death['시도'][:10],
#     startangle=90,
#     counterclock=False,
#     autopct='%.1f%%',
#     colors=colors)
# plt.savefig('전국시도별교통사고발생top10.png')
# plt.show()

# 지도에 그리기
'''
- 라이브러리 : folium
- 지도 데이터 파일 : .geojson
    공간정보시스템연구소 : http://www.gisdeveloper.co.kr/?p=2332
    
    지도 원천 데이터는 SHP(Shape file)이 필요
    SHP 파일은 직접 핸들링 하기가 힘들어 GeoJSON 이라는 지리 정보 표시를 위한 표준 JSON 포맷으로 변환.
    
    * folium*
    - 시각화 패키지 중 하나로 지도를 그려주는 모듈. (경량)
    
    
    
'''
import json
import folium

# 전국 시도별 교통사고 지도 그래프
print(data[['시도', '사고건수']].groupby(by='시도').sum())
data_grby_city2 = data[['시도', '사고건수']].groupby(by='시도').sum()

json = json.load(open('TL_SCCO_CTPRVN_min.json', encoding='utf-8'))
# print(json['features'][0]['id'])
print(data_grby_city2['사고건수'].index[0])
for i in range(17): 
    # 'id' : 사고건수값
    json['features'][i]['id'] = data_grby_city2['사고건수'].index[i]

# map 객체 생성 : 대한민국 중심좌표를 센터로 줌 레벨 7로 시작하는 맵 생성
map = folium.Map(location=[36.2002, 127.054], zoom_start=7)
# Choropleth : 지도 위에 띄워줄 그래프 레이어 설정하여 맵에 추가
folium.Choropleth(
    geo_data=json,
    name='choropleth',
    data=data_grby_city2['사고건수'],
    key_on='feature.id',
    fill_color='YlGnBu',
    fill_opacity=0.8,
    line_opacity=0.2).add_to(map)
# 레이어 컨트롤러에 지도 추가
folium.LayerControl().add_to(map)
map.save('trafficMapResult.html') # 저장

# 대한민국 중심좌표 : 36.2002, 127.054
# 서울 중심좌표 : 37.541, 126.986




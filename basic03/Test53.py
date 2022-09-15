# 공공데이터 분석

import pandas as pd

# pandas 로 csv 파일 읽어오기
data = pd.read_csv('도로교통공단_시도시군구별교통사고통계.csv')
# print(type(data))
# print(data)

# 데이터 조회
# print(data.head(10))    # 상위 5줄
# print(data.head())      # 상위 5줄
# print(data.tail())      # 하위 5줄
# print(data.tail(3))     # 하위 3줄

# print(data.head(3))
# data = data.rename(columns={'부상신고자수':'부상신고한사람수'})
# print('=' * 100)
# print(data.head(3))

# 데이터 타입 확인
# print(data.head())
# print(data.dtypesa) # 각 열의 데이터 타입
# 만약 숫자로 봐야할 데이터가 object 로 인식하고 있다면,
# 원하는 타입으로 변경 가능 (integer, string, boolean, float)
# data['컬럼명'] = data['컬럼명'].convert_dtype(convert_integer=True)

# 데이터 개수 확인
# print(data.shape)   # (229, 7) 튜플 (행의 개수, 열의 개수) : 데이터 229행 + 1 열이름

# 다양한 정보 확인 : info() 메타 데이터 조회
# data.info()

# 컬럼별 숫자형 데이터 값의 n-percentile 분포도, 평균값, 최대값, 최소값 정보 조회
# print(data.describe())

# 컬럼의 중앙값 : median
# print(data['사고건수'].median())

# 값의 횟수
# print(data['사고건수'].value_counts())
# print(data['사고건수'].value_counts(normalize=True)) # 퍼센트로 표현 (비율)

# 축 변환
# print(data.head(3))
# print('=' * 100)
# print(data.T.head(3))
# print('=' * 100)

'''
    Pandas DataFrame [] 연산자
        numpy [] : 단일값 추출, 슬라이싱, 인덱싱등 데이터 추출 : [인덱스], [인덱스:인덱스], [행, 열]
        DataFrame : ix[], iloc[], loc[] 을 통해 동일한 작업 가능
            * ix[]      : [행index, '컬럼명' or 컬럼index(0)] --> 해당 행-컬럼값 (초기 기능, 더 이상 사용 안함)
            * iloc[]    : 위치 기반 인덱싱만 허용 [행idx, 열idx] --> 슬라이싱 가능, boolean 인덱싱 불가능
            * loc[]     : 명칭 기반 데이터 추출 [행idx, '행idx명', '컬럼명']
        boolean 인덱싱
            * [], ix[], loc[] 에서 지원
            * df[df['컬럼명'] 비교 연산자 값]
'''
# print(data.head())
# print('=' * 100)
# print(data.iloc[0, 0])  # [행idx, 열idx]
# print(data.loc[0, '시도'])    # [행idx, 열명칭]
# print(data.loc[0:5, '시도'])  # [행슬라이싱, 열명칭]

#1. 사고건수가 1000 이상인 데이터 출력
# print(data[data['사고건수'] >= 1000])
# print('=' * 100)
#2. 사고건수가 1000 이상인 시도, 시군구, 사고건수만 출력 --> 컬럼 개수가 여러개로 리스트로 컬럼 명칭 묶어서 추출
# print(data[data['사고건수'] >= 1000][['시도', '시군구', '사고건수']].head(10))
# print('=' * 100)
#3. 사고건수 1000이상, 사망자수 10이상, 중상자수 200이상
# print(data[(data['사고건수'] >= 1000) & (data['사고건수'] >= 10) & (data['중상자수'] >= 200)].head(10))

# 정렬
# index 정렬
# print(data.sort_index(axis=0, ascending=True))  # 오름차순
# print(data.sort_index(axis=0, ascending=False)) # 내림차순
# value 정렬
print(data.sort_values(by='사고건수', ascending=True)[:5])
print(data.sort_values(by='사고건수', ascending=False)[:5])

# 선택
print(data['시도'][:5])
print(data['시군구'][:5])
# index 선택
print(data[0:5])
print(data[-5:])

# label(열명칭) 로 선택
print(data.loc[:, ['시군구', '사고건수']][:5]) # 0 ~ 4
print(data.loc[:5, ['시군구', '사고건수']])    # 0 ~ 5
print(data.loc[data.index > 5, ['시군구', '사고건수']]) # 행 인덱스 5보다 크고, 열은 시군구랑 사고건수
# 서울에 시도, 시군구 사고건수 출력
print(data.loc[data['시도'] == '서울', ['시도', '시군구', '사고건수']])





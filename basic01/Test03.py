'''
* 문자열 str *
    "문자열", '문자열', """ 여러 줄 문자열 """ (홑 따옴표도 가능)

    1) 0 ~ 시작하는 인덱스 번호
    2) 인덱싱
    3) 특징
        - 수정 불가능함 (immutable)
    4) 슬라이싱
        - 문자열[시작 인덱스 번호 : 끝 인덱스 번호] -> 끝 번호는 제외
'''
str1 = "hello"
print(str1[-1])
print(str1[0: 3])  # 끝 번호는 제외
print(str1[:2])  # 시작 인덱스 번호 지정 안 하면 처음부터 시작
print(str1[2: 6])  # 끝 번호 초과돼도 마지막 번호로 인식
print(str1[:])  # 처음부터 끝까지 출력

str2 = "TheJoeun Institute"
# 문제1. TheJoeun 만 출력
print(str2[0: 8])
# 문제2. Institute 만 출력
print(str2[9: 18])
str3 = "prigraming"
# 문제3. programming 으로 변경해서 출력
print(str3[:2] + "o" + str3[3:7] + "m" + str3[-3:])

print("*" * 50)
# 날짜 잘라보기
import datetime
today = datetime.date.today()
print(today)
print(type(today))
today = str(today)
print(today[:4])

# 문자열 관련 함수
str4 = "hello python"
print(str4)
str4 = str4.replace("python", "PyCharm")
print(str4)

# split() : 문자열 나누기
# result = str4.split() # 공백 기준으로 나눠줌
result = 'hello:hahaha'.split(":")
print(result)

# len() : 문자열 길이
str5 = 'sdjflsdifjeislgjsdg'
print(len(str5))
print(str5.count('s')) # 문자 안에 해당 문자가 몇 개 포함되어 있는지 확인

name = 'thejoeun'
# find()    : 문자 인덱스 알아내기
print(name.find('e'))
print(name.find('z')) # 없는 문자는 -1 로 리턴
# index()   : 문자 인덱스 알아내기
print(name.index('n'))
# print(name.find('z')) # 없는 문자는 에러 발생

# 대/소문자로 리턴 : lower() /upper()
str6 = 'Apple Tree'
print(str6.upper())
print(str6.lower())

# 공백 지우기 : strip(),, lstrip(), rstrip()
str7 = '         python      '
print(str7)
print(str7.strip())     # 앞 뒤 공백 삭제
print(str7.lstrip())    # 왼쪽 공백 삭제
print(str7.rstrip())    # 오른쪽 공백 삭제



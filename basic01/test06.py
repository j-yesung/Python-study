'''
군집 자료형 : 문자열 str, list, tuple, dice, set
* 리스트 list *
    - 여러 데이터 한번에 저장.
    - 다양한 데이터 타입을 섞어서 저장 가능
    - 수정 가능 mutable
    - 크기 제한 없다.
    - 구분 기호 : []
'''
a = [] # 빈 리스트 생성
b = list() # 빈 리스트 생성
print(a)
print(b)
print(type(a))
print(type(b))
c = [1, 2, 3, 4, 5]
print(c)
d = [1, 2, True, 'hello', 'python', [10, 20 ,30]]
print(d)
print(d[-1][-2]) # 배열 안에 배열 꺼내기

lst1 = [1, 2, 3, [4, 5, 6], 7]
# 숫자 4, 3, 7 출력
print(lst1[-2][-3])
print(lst1[2])
print(lst1[-1])

lst2 = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
print(lst2[2 : -1])
print(lst2[-3][:2])

# 값 수정
lst3 = [1, 2, 3]
lst3[0] = 100
print(lst3)

lst4 = [1, 2, 3, 4, 5]
# 인덱스 번호 1번의 요소를 'a', 'b', 'c' 로 수정
lst4[1] = ['a', 'b', 'c']
print(lst4)
lst4[1] = 'a', 'b', 'c' # 튜플
print(lst4)

# 리스트 관련 함수
#1. 요소 추가 : append()
lst5 = []
print(lst5)
lst5.append(10)
lst5.append(['a', 'b', 'c'])
print(lst5)

#2. 리스트 확장 : extend()
lst6 = [1, 2, 3]
lst7 = [4, 5, 6]
print(lst6)
lst6.extend(lst7)
print(lst6)

#3. 요소 중간에 삽입 : insert(인덱스, 값)
lst8 = [1, 2, 3, 4, 5]
lst8.insert(1, 10)
print(lst8)

#4. 요소 제거 : remove(값)
lst8.remove(10)
print(lst8)

#5. 정렬
lst9 = [1, 3, 4, 5, 2]
print(lst9)
lst9.sort() # 오름차순
print(lst9)
lst9.reverse() # 내림차순
print(lst9)

#6. 리스트 길이
print(len(lst9))

lst10 = [100] * 5
print(lst10)
lst10 = [1, 2, 3, 4, 5]
print(3 in lst10)

lst11 = [10, 20, 30]
lst12 = [40, 50, 60]
lst13 = lst11 + lst12 # extend() 확장
print(lst13)

# random
import random
num1 = random.random()
print(num1)

# 1 ~ 5 사이 랜덤값
num2 = random.randint(1, 5)
print(num2)

lst14 = [10, 20, 30, 40, 50]
num3 = random.choice(lst14) # 리스트 값 중 하나를 무작위로 선택
print(num3)

num4 = random.sample(lst14, 3) # 지정한 배열, 원하는 개수 만큼 무작위로 뽑아서 리턴
print(num4)

# 배열 안 요소 무작위로 섞기
random.shuffle(lst14)
print(lst14)
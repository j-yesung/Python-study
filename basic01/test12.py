'''
파라미와 인자 : 개수, 순서가 일치 해야 된다.
파라미터의 초기값 지정.
초기값이 파라미터에 지정되어 있으면 인자 생략 가능
'''
def func(username, password, name, gender, email, nation = "S.korea"):
    print(username)
    print(password)
    print(name)
    print(gender)
    print(email)
    print(nation)

func("ironman", "1234", "아이언맨", "M", "email@naver.com")
print("=" * 70)
'''
파라미터와 인자 : 개수, 순서가 일치 해야된다.
파라미터 순서 바꿔도 사용 가능한 방법
함수 호출할 때, 인자 기입시 파라미터명 = 값
'''
func(username="ironman", password="1234", name="아이언맨", email="hello@naver.com", gender="M", nation="korea")
print("=" * 70)

# 리턴
def calc(num1, num2):
    return num1 + num2, num1 - num2

print(calc(10, 20))

res1, res2 = calc(100, 400) # (500, -300) 튜플로 리턴, unpacking 되서 각각 변수에 저장
print(res1)
print(res2)
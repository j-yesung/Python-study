'''
* 함수 (function) def *
    - def 함수명(파라미터, 파라미터, ..):
        실행문들..
        return 값

    - 변수 = 함수명(인자, 인자, ..)

    1) 함수의 종류
        - 사용자 정의 함수
        - 내장 함수 builts-in : print(), len(), range()...
        - 메서드 : 클래스 안에 정의된 함수
'''
def showInfo(name):
    print("이름은 {}입니다.".format(name))
    return 100

num = showInfo("ironman")
print(num)

'''
* 변수의 scope *
    scope : 변수의 선언 위치에 따라 변수의 유효 범위가 결정된다.
    변수의 종류
        1. 전역변수 global variable
            선언위치 : 함수 밖
            유효범위 : 프로그램 종료 전까지 유효
                      함수 안에서 사용할 시 참조형으로 사용 가능 (수정 불가)
                      * 함수 안에서 전역변수의 값을 변경하는 방법
                        - 리턴값 이용
                        - global 키워드 이용
            
        2. 지역변수 local variable
            선언위치 : 함수 안
            유효범위 : 함수 안
            
'''
print("=" * 100)

def func(num):
    # 지역변수
    num += 10
    print("func num >> ", num)

# 전역변수
num = 100
func(num) # num = 전역변수 값 전달
print(num) # 전역변수 출력

def func2():
    global num # 전역변수를 함수 안에서 사용 하겠다고 선언
    num += 10
    print("func num >> ", num)

func2()
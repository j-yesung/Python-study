'''
1. 출력문
    print()
    * 연결하여 출력
    문자 + 문자 : 문자 연결되어 출력
    문자, 문자  : 띄어쓰기되어 출력
    숫자 + 숫자 : 연산 결과 출력
    숫자, 숫자  : 나란히 출력
    문자, 숫자  : 나란히 출력
    문자 + 숫자 : 에러!
    문자 * 숫자 : 문자가 숫자 만큼 반복되어 출력

'''
print(10)
print('1. ' + "hello")
print('2. ' + 'hello')
print('3. ' + '10' + '10')
print('4. ' + '10', '10')
print('5. ' + '10' + '10')
print('6. ' + '문자1', '문자2')
print('7. ' + '문자1' + '문자2')
print('8. ' + 'hello' * 10)
print('9. ' + '엔터 기능 없애기', end = ' ')
print('10. ' + '다음 줄에 출력?')

'''
* 이스케이프 문자 *
    /n  : 줄 바꿈
    /t  : 탭 간격
    /'  : 홑 따옴표 문자로 출력
    /"  : 겹 따옴표 문자로 출력
'''
print('\n')
print("내 이름은 \"피카츄\"입니다.")

name = "뽀로로"
age = 10
print("내 이름은 " + name + "입니다.")

# 서식문자 : 정수 %d, 실수 %f, 문자열 %s
print("내 이름은 %s입니다." % name)
print("내 이름은 %s입니다. 나이는 %d살입니다." % (name, age))
# format
print("내 이름은 {}입니다. 나이는 {}살입니다." .format(name, age))

'''
* 데이터 타입 * 
    1) 숫자형
        정수  : int   (python ver. 3.x)    int, long   (python ver. 2.x)
        실수  : float
                (python ver. 3.x)   : 5000/3 = 1666.66666
                (python ver. 2.x)   : 5000/3 = 1666
        
    2) 참/거짓형
        bool    : True / False
        
    3) 군집 자료형
        문자열형    : str
        리스트      : list
        튜플        : tuple
        딕셔너리     : dict
        집합         : set

* 변수 variable *        
    변수명 = 값
    
    type(값/변수) : 데이터 타입 확인 가능
    
    변수 명명규칙
        - 숫자로 시작 X, 대소문자 구분 (num 이랑 Num 은 다른 변수임)
        - 특수기호는 _ (밑줄)만 허용
        - keyword 사용 불가
        - 
'''
print("*" * 50)

num = 10
print(num)
print(type(num))
print(id(num))
num2 = 2.14
print(num2)

hello = "안녕하세요."
print(hello)

'''
* 입력문 *
: 콘솔을 통해서 값 입력. (문자열로 리턴)

    변수 = input("콘솔에 띄울 메세지")
    
* 형변환 casting, convert *
    문자 -> 숫자
        int(값)
    
    문자 -> 실수
        float(값)
        
    int, float -> 문자
        str(값)
'''
print("*" * 50)

# msg = input("메세지 입력 >> ")
# print(msg)
# age = int(input("나이 입력 >> "))
# print(age + 1)


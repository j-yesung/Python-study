'''
* 클래스 class *
    class 클래스명:
        필드(변수)
        메서드(함수)

    클래스명()

    1) 필드(변수)
        - 클래스 변수
            선언위치 : 메서드 밖
            사용방법 : 클래스명.변수명
            -> 모든 객체가 접근할 수 있는 "공용" 변수
            -> 레퍼런스 변수명으로 클래스 변수의 값을 변경하면, 인스턴스 변수로 새로 생성된다. (메모리 후위 선점 방식이라고 부른다.)
            -> 프로그램 종료시 소멸

        - 인스턴스 변수
            선언위치 : 메서드 안
            사용방법 : 레퍼런스 변수명.변수명
            -> 객체 만의 고유한 저장 공간이 필요시
            -> 객체 소멸시 삭제

        - 지역 변수
            선언위치 : 메서드 안
            사용방법 : 변수명
            -> 메서드가 종료하면 소멸

    2) 메서드(변수)
        - 인스턴스 메서드
            클래스 안에 정의하는 일반 메서드
            -> 첫번째 파라미터는 self 키워드 작성
            -> self는 이 메서드를 호출할 때, 객체 자기 자신을 전달받는 파라미터. (호출시 self에 해당하는 인자는 작성 안함.)
             
        - __init__(self) : init 메서드 (생성자)
            -> 클래스를 통해 객체를 생성할 때, 자동으로 한번 호출되는 생성자

        - 클래스 메서드
            -> 클래스 전체에 영향을 미치는 메서드
            -> 첫번째 파라미터는 클래스 자신으로 cls라는 키워드 작성
            -> 클래스 메서드 정의문 위해 @classmethod 라는 데코레이터를 작성
            -> 클래스 변수의 값 변경을 위해 주로 사용

        - 스태틱 메서드
            -> 클래스나 객체에 영향을 미치지 못하는 메서드. (단지, 편의를 위해 사용하는 그냥 메서드)
            -> 클래스 안에서 메서드가 아닌 일반 함수를 사용하기 위한 메서드
            -> 파라미터에 self를 안 적는다. 대신, 메서드 위에 @staticmethod 데코레이터 기술
'''
class Person:
    name = "사람"
    age = 0

    def eat(self, food):
        print(food, "를 먹는다!", sep="")
    def showInfo(self):
        print("이름 : ", self.name)
        print("나이 : ", self.age)


p1 = Person() # 객체 생성
print(p1)
print(p1.name)
print(p1.age)
p1.eat("피자")
p1.showInfo()

# 클래스 변수 vs 인스턴스 변수
class Starbucks: # 본사
    shape = "" # 클래스 변수 (공용 변수)

    def say(self):
        self.msg = "스타벅스" # 인스턴스 변수 : self.변수명 이라고 메서드 안에 작성
        a = 10 # 지역 변수
        print("안녕하세요, {}입니다.".format(self.msg))

s1 = Starbucks() # 1호점
s2 = Starbucks() # 2호점

# 클래스 변수 : 클래스명.변수명
print("=" * 50)
Starbucks.shape = "star"
print("Starbucks : ", Starbucks.shape)
print("s1 : ", s1.shape)
print("s2 : ",s2.shape)
print("=" * 50)

# 클래스로 값 대입
Starbucks.shape = "square"
print("Starbucks : ", Starbucks.shape)
print("s1 : ", s1.shape)
print("s2 : ", s2.shape)
print("=" * 50)

# s1 값 대입
s1.shape = "diamond" # s1의 shape 공간 점유
print("Starbucks : ", Starbucks.shape)
print("s1 : ", s1.shape)
print("s2 : ", s2.shape) # 본사 참조
print("=" * 50)

# 클래스로 값 대입
Starbucks.shape = "heart"
print("Starbucks : ", Starbucks.shape)
print("s1 : ", s1.shape)
print("s2 : ", s2.shape)
print("=" * 50)

# s2 값 대입
s2.shape = "circle"
print("Starbucks : ", Starbucks.shape)
print("s1 : ", s1.shape)
print("s2 : ", s2.shape)
print("=" * 50)

# 클래스로 값 대입
Starbucks.shape = "kimuti"
print("Starbucks : ", Starbucks.shape)
print("s1 : ", s1.shape)
print("s2 : ", s2.shape)
print("=" * 50)
# 상속
class Student1:
    def python(self):
        print("재밌는 이썬이")

class Student2:
    def c(self):
        print("C언어가 뭐죠")

class Student3:
    def java(self):
        print("자바란..")

# 상속 받는 클래스 : 다중 상속 가능
class Ironman(Student1, Student2, Student3):
    pass

man = Ironman()
man.java()

class Person:
    __jumin = "101010-1111111" # 은닉화

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("1. 부모 생성자!")

    def show(self):
        print("4. 부모")
        print("5. 이름:", self.name)
        print("6. 나이:", self.age)
# ===========================================================================
class Student(Person):
    # 생성자 오버라이딩
    def __init__(self, name, age, number):
        super().__init__(name, age) # 부모 생성자 호출
        self.number = number
        print("2. 자식 생성자!")

    def show(self):
        print("3. 자식")
        super().show() # 부모 생성자 show() 메서드로 이동하여 실행
        print("7. 학번:", self.number)
# ===========================================================================
pk = Student("이즈", 20, 2022)
pk.show()

print("=" * 50)
print(Person._Person__jumin)

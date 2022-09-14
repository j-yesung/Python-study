'''
* 생성자 init 메서드 *
'''
class Person:
    def __init__(self, name, age):
        # 인스턴스 변수
        self.name = name
        self.age = age
        print("생성자 호출!")
# ===========================================================================
person = Person("ironman", 10)
print(person.name)
print(person.age)

class Npc:
    count = 0 # Npc가 만들어질 때 마다, Npc의 수를 카운팅 할 변수 (공용)

    def __init__(self, name):
        self.name = name
        print("{} 만들어지는 중..".format(self.name))
        Npc.count += 1

    def die(self):
        print("{}가 죽었습니다..".format(self.name))
        Npc.count -= 1

    def showInfo(self):
        print("생존하고 있는 NPC는 {}명입니다.".format(Npc.count))
# ===========================================================================
# elf1 = Npc("엘프1")
# elf2 = Npc("엘프2")
# elf3 = Npc("엘프3")
# elf1.showInfo()
# elf2.die()
# elf2.showInfo()
# ===========================================================================

# 상점 계산기
class Payment:
    count = 0       # 계산된 제품의 총 개수
    discount = 0.2  # 할인율

    # 생성자
    def __init__(self, price, number):
        # 인스턴스 변수
        self.price = price
        self.number = number
        Payment.count += 1

    # 인스턴스 메서드
    def calulator(self):
        # 인스턴스 변수
        self.pay = self.price * self.number # 정가 (할인X)
        self.dc_pay = self.pay - (self.pay * Payment.discount)  # 할인금액

    # 인스턴스 메서드
    def display(self):
        print(Payment.count, "번째 제품입니다.")
        print("[정가] ", self.price)
        print("[수량] ", self.number)
        print("[정상금액] ", self.pay)
        print("[할인금액] ", self.dc_pay)

    # 스태틱 메서드
    @staticmethod
    def welcome():
        print("어서오세요~")
        print("할인 중입니다~")

    # 클래스 메서드
    @classmethod
    def update(cls, value): # cls 는 Payment 클래스에서 끌고옴.
        # 할인율 조정 : 1 이상 이거나, 0 이하이면 할인율 입력받도록
        while value >= 1 or value <= 0:
            value = float(input("할인율을 다시 입력하세요: "))
        cls.discount = value

# ===========================================================================
print("=" * 30)
p1 = Payment(1000, 5)
p1.calulator()
p1.display()

print("=" * 30)
Payment.update(1)

print("=" * 30)
p2 = Payment(2000, 4)
p2.calulator()
p2.display()

print("=" * 30)
p2.welcome()






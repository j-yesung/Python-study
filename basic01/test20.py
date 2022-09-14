'''
* 특수 메서드 *
__init__()      : 생성자
__del__()       : 소멸자 (레퍼런스 카운트가 0이 되면 자동으로 호출)
__call__()      : 객체 호출시 실행되는 메서드
__getitem__()   : 딕셔너리 처럼 객체.['키값']을 이용해 속성을 찾게 해주는 메서드
                  메서드 내에서 입력한 키에 대한 값을 리턴해 주어야 한다.

__name__() / __main__() : Dunder name

'''
class Char:
    def __init__(self, hp, attack, defence):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        print("플레이어 생성 완료!")

    def __call__(self, *args, **kwargs):
        print("[체력] {} | [공격력] {} | [방어력] {}".format(self.hp, self.attack, self.defence))
        print(kwargs)

        for i, j in kwargs.items():
            self.__setattr__(i, j) # 속성 추가, 변수 생성 __setattr__(변수명, 값) -> (key, value)

    def __getitem__(self, item):
        print(item)
        if item == "체력":
            return self.hp
        elif item == "공격력":
            return self.attack
        elif item == "방어력":
            return self.defence
        else:
            return "존재하지 않은 값입니다."

a = Char(10, 200, 150)
b = Char(30, 100, 200)

a(abc="1234", de="6789") # __call__() 호출
b()

print(a["방어력"]) # __getitem__() 호출

print(a.abc)
print(a.de)
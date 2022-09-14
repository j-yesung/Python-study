def packer(name=None, **kwargs):
    print(name)
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())
    for i, j in kwargs.items():
        print("{} : {}".format(i, j))

packer(age="30", mobile="010-1234-5678", city="seoul")

# dict unpacking
def unpacker(name=None, score=None):
    if name and score:
        print("안녕하세요, {}님의 점수는 {}점 입니다.".format(name,score))
    else:
        print("이름이나 점수가 없네요.")

unpacker(**{"name" : "콜라"})
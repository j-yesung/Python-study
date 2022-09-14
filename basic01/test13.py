'''
예상할 수 없는 함수
def 함수명(*파라미터): 매개변수에 전달되는 인자가 여러개일 경우 한 곳에 받아 줄 수 있는 기능
    실행문들..
'''
def sum(*num):
    tot = 0
    print(num)
    print(type(num))
    for i in num:
        tot += i
    return tot

print(sum(10, 20, 30, 40, 50, 60))

def calc(oper, *num, test="haha"):
    if oper == 'sum':
        tot = 0
        for i in num:
            tot += i
    elif oper == 'mul':
        tot = 1
        for i in num:
            tot *= i
    print(tot)
    return tot

result = calc("sum", 10, 20, 30, 40, test="kkukkukkkakka")
print("총합 >> ", result)

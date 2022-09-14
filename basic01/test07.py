'''
* 제어문 *
    조건문 : if
    반복문 : for, while
    보조 제어문 : continue, break

* 반복문 while *
    while 조건식:
        반복할 실행문들..

    while True:
        실행문들..
        if 조건식 break * 종료 시점 필요 *
'''
'''
i = 0
while i < 10:
    print(i)
    i += 1
'''
# 1 ~ 10 까지의 짝수를 모두 더한 값 출력
j = 1
sum = 0

while j < 11:
    if j % 2 == 0:
        sum += j
    j += 1
print(sum)

print("=" * 100)

while True:
    num = int(input("숫자 입력 >> "))
    print(num)
    if num == 9:
        break
print("종료")

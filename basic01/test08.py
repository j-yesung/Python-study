'''
* 제어문 *
    조건문 : if
    반복문 : for, while
    보조 제어문 : continue, break

    for 변수 in 문자열|리스트|튜플:
        실행문들..

'''
for i in "hello":
    print(i)

lst1 = [10, 20, 30, 40]
for i in lst1:
    print(i)

print(range(5))

print("=" * 100)
for i in range(5): # 0 ~ 5 이전까지
    print(i)

print("=" * 100)
for i in range(10, 15): # (start, end) end 이전까지
    print(i)

print("=" * 100)
for i in range(1, 10 ,2): # (start, end, step) start 부터 end 이전까지 step 씩 증감
    print(i)

# 구구단 3단 출력
print("=" * 100)
print("********* 구구단 3단 출력 *********")
for i in range(1, 10):
    print(3, "*", i, "=", (3 * i))
# 구구단 전체 출력
print("********* 구구단 전체 출력 *********")
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", (i * j))

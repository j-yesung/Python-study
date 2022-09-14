'''
* 조건문 if *
    if 조건식:
        조건 참일 경우 실행할 명령문들..
    if 조건식:
        명령문들..
    else:
        명령문들..
    if 조건식:
        명령문들..
    elif:
        명령문들..
    elif 조건식:
        명령문들..
    else:
        명령문들..
'''
num = 10
if num > 10:
    print("10보다 크거나 같다.")
elif num < 10:
    print("10보다 작다.")
else:
    print("10이다.")

print("*" * 30)

'''
국어 영어 수학 점수를 입력 받아 세 과목의 평균을 학점으로 출력하세요.
평균 90이상 "A", 80이상 "B". 70이상 "C", 그 이하 "F"
'''
msg1 = int(input("국어 점수 >> "))
print(msg1)
msg2 = int(input("국어 점수 >> "))
print(msg2)
msg3 = int(input("국어 점수 >> "))
print(msg3)

avg = (msg1 + msg2 + msg3) / 3

if avg >= 90 and avg < 101:
    print("A")
elif avg >= 80 and avg < 90:
    print("B")
elif avg >= 70 and avg < 80:
    print("C")
else:
    print("F")



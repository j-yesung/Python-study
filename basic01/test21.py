'''
* 예외처리 exception handler *
    에러 ex)
        IOError (파일, 이미지 등 못 찼을 때)
        IndexError
        ImportError
        ValueError
        ZeroDivisionError
        FileNotFoundError
        SyntaxError
        EOFError
        
    예외처리 구문
        try:
            (에러 발생할 수 있는 코드들)
        except:
            (에러 발생시 처리할 코드들)
        try:
            (에러 발생할 수 있는 코드들)
        except (발생 에러 코드 as (에러 메세지 담을 변수)):
            (에러 발생시 처리할 코드들)
'''
# print("프로그램 시작할게요.")
# while True:
#     try:
#         num = input("정수 입력 >> ")
#         int(num)
#         print(num)
#         if int(num) == 0: break
#     except ValueError as e:
#         print("에러 발생.. 값이 이상해요..", e)
#     finally:
#         print("예외 발생 여부와 상관 없이 무조건 실행되는 블럭이예요.")
#
# print("프로그램 종료할게요.")

# def func():
#     try:
#         num = int(input("1 ~ 5 사이 정수 입력해 주세요. >> "))
#         if num > 5 or num < 1:
#             print("잘못 입력")
#             raise RuntimeError # 강제로 예외 발생
#     except ValueError:
#         print("func() 내부에서 바로 잡을게")
#     else:
#         print("입력값 : ", num)
#
# try:
#     func()
# except RuntimeError:
#     print("예외 잡자.")

num = [1, 2, 3, 4]
result = [a * 3 for a in num] # num 배열 안 요소들한테 * 3 해주기
print(result)
# dunder name / main
def print_hello():
    print("hello method")

print("__name__ : ", __name__)

# 현재 main 스레드로 이 파일을 실행 시켰으면 print_hello()를 실행
# -> 아래 구문으로 코드가 실행되는 것인지 import 된 것인지 체크함
if __name__ == '__main__':
    print_hello()


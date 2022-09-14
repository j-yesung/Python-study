# import basic01.test22 as test22
from basic01 import test22

print("test23에서 출력")
print("test23 : ", __name__)
# basic01.test22.print_hello()
test22.print_hello()

'''
* 모듈과 패키지 *
    1) 모듈
        - 함수가 파이썬이 제공하는 내장 함수가 있듯이, 모듈 또한 파이썬이 제공하는 표준 모듈이 있다.
        - 함수도 모듈도 이미 개발된 코드를 재사용하기 위한 기술
        - 함수는 단순 명령문들의 집합이지만, 모듈은 클래스/함수/변수 등으로 구성된다.
        - 함수는 사용자가 작성하는 프로그램 파일 내에 존재하지만, 모듈은 별도의 .py 파일로 존재한다.

    2) 모듈 사용법
        - import 클래스 : 외부 묘듈 가져와 사용할 때, 여러 폴더가 들어 있는 모듈을 통으로 가져올 수도 있고 하나만 가져올 수도 있다.
        - 여러 개의 요소/쉼표를 구분자로 나열하면 한 import 명령에서 여러 개 동시에 가져올 수도 있다.
        
        - import 클래스/모듈 패키지 as 별칭 : 해당 파일에서 import 된 것을 별칭으로 사용
        - from 모듈 패키지 ... import 클래스 : 모듈 패키지 안에 클래스 가져오기
        -> import 뒤에 있는 명칭만 인식, 패키지명은 필요 없다.
        -> 클래스명이 길면 as로 별칭 추가 기능
        
* 파일 입출력 I/O *
    1) 기본 절차
        # 쓰기
        1. open file
        2. write 
        3. close file
        
        open("파일명", "파일 열기 모드")
        - 파일 열기 모드
            r : 읽기 모드   read (default)
            w : 쓰기 모드   write
                > 파일명이 존재하지 않을 경우, 새로운 파일 생성
                > 파일명이 이미 존재할 경우, 기존 내용을 지우고  새로 작성
            
            a : 추가 모드   append : 써 있는 내용에 이어서 쓰기
'''
# 파일 쓰기 1.
# f = open("newFile.txt", "w")
# f.write("뽀로로\n")
# f.write("뽀로로\n")
# f.write("뽀로로\n")
# f.close()

# 파일 쓰기 2. 다른 경로로 지정
# f = open("D:\\yesung\\newFile01.txt", 'w')
# f. write("아이언맨\n")
# f. write("아이언맨\n")
# f. write("아이언맨\n")
# f. write("아이언맨\n")
# f.close()

import codecs
f = codecs.open("testText.txt", 'w', 'utf-8')
f.write("하하\n")
f.write("하하\n")
f.write("하하\n")
f.close()
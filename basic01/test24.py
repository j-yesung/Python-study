'''
with 키워드 이용해서 context manager 만들기
'''
# with open("database.txt", "w") as file:
#     file.write("하하하\n")
#     file.write("하하하\n")
    # file.close() : 블럭이 끝나면 file이 없어져 close도 필요 없음

with open("database.txt", "r") as file:
    result = file.readlines() # 파일 전체 읽어오기 -> 모든 줄을 리스트에 담아 리턴
    print(result)
    for r in result:
        print(r, end="")

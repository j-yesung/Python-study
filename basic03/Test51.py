'''
데이터 저장
파이썬 Oracle DB 연동
1. 라이브러리 설치
    - cx-Oracle (Pycharm) cx_oracle (pip install cx_oracle)
    - oracle instantclient 설치
'''
import cx_Oracle

# 오라클 인스턴트 클라이언트 경로
cx_Oracle.init_oracle_client(lib_dir=r"C:\oracle\instantclient_19_16")
'''
cx_Oracle.connect : 오라클 커넥션 접속 ('username/password/@url:port/sid')
.cursor : 쿼리 실행하고 결과 데이터 담을 객체 선언
.execute : SQL 실행, 결과가 cursor에 담김
.fetchall : 쿼리 실행 결과에서 데이터를 한 행씩  fetch 한다. 전부 all
.description : 데이터의 컬럼명 추출
'''
conn = cx_Oracle.connect('java13', 'java13', '192.168.100.250:1521/orcl')
cursor = conn.cursor()  # cursor 객체 얻어오기

# 데이터 조회
# sql = "select * from test"
# cursor.execute(sql) # 쿼리문 실행
#
# # 커서에 담긴 결과를 하나씩 추출
# for result in cursor:
#     # print(result)
#     print(result[0])
#     print(result[1])
#     print(result[2])
#     print(result[3])
#     print("=" * 50)
# # 사용 후 닫기
# cursor.close()
# conn.close()

# 데이터 저장
import datetime
#
# sql = 'insert into test values (:1, :2, :3, :4)'
# data = ('py01', '0000', 20, datetime.datetime.now()) # 바인딩 시킬 데이터 튜플 형태로 만들고
# cursor.execute(sql, data)
#
# cursor.close()
# conn.commit()
# conn.close()

# 데이터 여러개 추가
'''
sql = 'insert into test values (:1, :2, :3, :4)'
data = [
    ('py02', '0002', 20, datetime.datetime.now()),
    ('py03', '0003', 30, datetime.datetime.now()),
    ('py04', '0004', 40, datetime.datetime.now()),
    ('py05', '0005', 50, datetime.datetime.now())
]
cursor.arraysize = len(data)    # 리스트의 개수 전달
cursor.executemany(sql, data)   # 한번에 여러 레코드 insert

cursor.close()
conn.commit()
conn.close()

'''
'''
# 레코드 개수 조회
sql = 'select count(*) from test'
cursor.execute(sql)
count = cursor.fetchone() # 쿼리문 실행 결과에서 레코드 한개 추출
print(count) # 튜플 형태
print('회원수 >> ', count[0], '명')

cursor.close()
conn.commit()
conn.close()
'''
'''
# 레코드 수정
sql = 'update test set pw=:1, age=:2 where id=:3'
data = ('1234', 43, 'java01')
cursor.execute(sql, data)

cursor.close()
conn.commit()
conn.close()
'''

# 레코드 삭제
sql = 'delete from test where id=:1'
data = ('py01',)
cursor.execute(sql, data)
cursor.close()
conn.commit()
conn.close()

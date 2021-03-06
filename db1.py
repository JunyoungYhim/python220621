# db1.py

import sqlite3

#연결 객체를 리턴받기
con = sqlite3.connect(":memory:")
#커서 객체를 리턴받기
cur = con.cursor()
#테이블(스키마)를 생성
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-222');")

#입력 파라미터 처리
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?,?);", (name, phoneNumber))

#여러건을 입력
datalist = (("tom","011-123"), ("dsp","010-456"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)

#검색
cur.execute("select * from PhoneBook;") # 폰북테이블의 조건없이 모든 컬럼을 가져와

#검색 매서드 사용
print("---fetchone()---")
print(cur.fetchone())
print("---fetchmany(2)---")
print(cur.fetchmany(2))
print("---fetchall()---")
print(cur.fetchall())
# 1건 2,건 4건이 나오는게 아니라 이미 가져온거는 가져오는 대상에서 빠짐
# 때문에 fetchall을 하더라도 마지막 데이터 1개만 가져오게 된다.

print("---fetchall()---")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())

# for row in cur:
#     print(row)

#이렇게도 출력해서 볼 수 있다.
# for row in cur:
#     print(row[0] + "," + row[1])



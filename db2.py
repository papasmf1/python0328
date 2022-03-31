# db1.py 
import sqlite3

#전역함수로 연결객체 리턴(파일에 영구적으로 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#두번째 인스턴스인 커서를 리턴받기
cur = con.cursor()
#테이블을 가장 먼저 생성
#ANSI SQL 92, 99(미국 표준안)
cur.execute("create table PhoneBook (name text, phoneNum text);")
#1건을 입력
cur.execute("insert into PhoneBook values ('derick','010-222');")
#입력 파라메터 처리(?, @name )
name = "gildong"
phoneNumber = "010-123"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#여러건을 입력(배열의 배열은 2차원배열)
datalist = (("tom","010-333"),("dsp","010-555"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

cur.execute("select * from PhoneBook;")
print(cur.fetchall())

#작업완료(정상적으로 작업종료)
con.commit() 

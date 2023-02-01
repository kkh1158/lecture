# pip install cx-Oracle
import cx_Oracle

#---------------------------------------------------
# --오라클에서...
# CREATE TABLE ADDR (
#     SEQ number PRIMARY KEY ,
#     NAME VARCHAR2(10),
#     TEL VARCHAR2(15)
# );
#
# drop sequence addr_seq;
#
# create sequence addr_seq
# start with 1
# increment by 1
# nocache;
#
# insert into addr values(addr_seq.nextval, '홍길동', '000');
# select * from addr;
# commit;
#----------------------------------------------------


# with cx.connect('ai', '0000', 'localhost:1521/XE') as conn:
#     if bool(conn) :
#         print('연결 성공')
#     else:
#         print('연결 실패')
#
#     with conn.cursor() as cur:
#         cur.execute("select * from emp")
#         for row in cur:
#             print(list(row))
#     #cur.close()
# #conn.close()
# 이처럼 with as를 쓰면 close()를 안써도되지만 연습 겸 직접 열고 닫자.

# 연결 하고 닫기
conn =  cx_Oracle.connect('ai', '0000', 'localhost:1521/XE')
if bool(conn):
    print('연결 성공')
else:
    print('연결 실패')
conn.close()

# insert
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
# cur = conn.cursor()
# cur.execute(sql, ['아무개', '555'])
# cur.execute(sql, ['함소영', '2525'])
# conn.commit()
# cur.close()
# conn.close()

# insert2
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# vnm = '나변수'
# vtel = '999'
# cur.execute(sql, [vnm, vtel])
# conn.commit()
# cur.close()
# conn.close()

# insert3
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.execute(sql, {'vnm':'나변수2', 'vtel':'8989'})
# conn.commit()
# cur.close()
# conn.close()

# insert4
# datas = [{'vnm':'나이름1', 'vtel':'111'},
#          {'vnm':'나이름2', 'vtel':'222'},
#          {'vnm':'나이름3', 'vtel':'333'}]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :vnm, :vtel)"
# cur = conn.cursor()
# cur.executemany(sql, datas)
# conn.commit()
# cur.close()
# conn.close()

# insert5
# datas = [['리스트1', '6666'],
#          ['리스트2', '8888'],
#          ['리스트3', '9999']]
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "insert into addr(seq, name, tel) values(addr_seq.nextval, :1, :2)"
# cur = conn.cursor()
# cur.executemany(sql, datas)
# conn.commit()
# cur.close()
# conn.close()

# update
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "update addr set name=:1, tel=:2 where seq=:3"
# cur = conn.cursor()
# cur.execute(sql, ['홍길순', '999', 1])
# conn.commit()
# cur.close()
# conn.close()

# delete
# conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
# sql = "delete from addr where name like :1 or name like :2"
# cur = conn.cursor()
# cur.execute(sql, ['%나이름%', '%리스트%'])
# conn.commit()
# cur.close()
# conn.close()

# select
# conn =  cx_Oracle.connect('ai', '0000', 'localhost:1521/XE')
# sql = 'select * from addr'
# cur = conn.cursor()
# cur.execute(sql)
# for row in cur:
#     print(list(row))
# cur.close()
# conn.close()

#select2
# conn =  cx_Oracle.connect('ai', '0000', 'localhost:1521/XE')
# sql = 'select * from addr where seq=:1'
# cur = conn.cursor()
# cur.execute(sql, [5])
# for row in cur:
#     print(list(row))
# cur.close()
# conn.close()

#select3
# conn =  cx_Oracle.connect('ai', '0000', 'localhost:1521/XE')
# sql = 'select * from addr where seq in {}'.format((1,3,5))
# cur = conn.cursor()
# cur.execute(sql)
# for row in cur:
#     print(list(row))
# cur.close()
# conn.close()
#############################################
# KIO_GOODS
#############################################
# GOOD_SEQ
# GOOD_NAME
# GOOD_IMG
# GOOD_PRICE
# GOOD_DESC
# REG_DATE
##############################################
# KIO_CART
##############################################
# CART_SEQ
# TEL
# GOOD_SEQ
# GOOD_PRICE
# ORDER_AMOUNT
# REG_DATE
##############################################
# KIO_ORDER
##############################################
# ORDER_SEQ
# TEL
# ORDER_PRICE
# PAY_GUBUN
# REG_DATE
# ############################################
import os
import cx_Oracle

def get_goods_list():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select GOOD_NAME, GOOD_IMG, GOOD_PRICE, GOOD_DESC from KIO_GOODS"
    cur = conn.cursor()
    cur.execute(sql)
    goods_list = []
    for row in cur:
        good_dict = {}
        good_dict['GOOD_NAME'] = row[0]
        good_dict['GOOD_IMG'] = row[1]
        good_dict['GOOD_PRICE'] = row[2]
        good_dict['GOOD_DESC'] = row[3]
        goods_list.append(good_dict)
    cur.close()
    conn.close()

    return goods_list

#select GOOD_PRICE from KIO_GOODS where good_seq=1;
def get_good_price(good_seq):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """   select GOOD_PRICE from KIO_GOODS where good_seq = :1"""
    cur = conn.cursor()
    cur.execute(sql, [good_seq])
    price = list(cur)[0][0]
    conn.commit()
    cur.close()
    conn.close()
    return price

def cart_add():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    tel = input('뒷번호 4자리 입력: ')
    good_seq = int(input('상품 번호 입력: '))
    order_price = get_good_price(good_seq)
    order_amount = int(input('몇개드실?: '))

    cart_list = [tel, good_seq, order_price, order_amount]
    sql = """   insert into KIO_CART(CART_SEQ,TEL,GOOD_SEQ,GOOD_PRICE,ORDER_AMOUNT, REG_DATE)
                values(KIO_CART_SEQ.nextval, :1, :2, :3, :4, sysdate)"""
    cur = conn.cursor()
    cur.execute(sql, cart_list)
    conn.commit()
    cur.close()
    conn.close()


def get_total_price(tel):
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """   select sum(good_price*order_amount) from KIO_CART
                where tel = :1
                group by tel"""
    cur = conn.cursor()
    cur.execute(sql, [tel])
    tot_price = list(cur)[0][0]
    conn.commit()
    cur.close()
    conn.close()

    return tot_price

def orders():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    tel = input('뒷번호 4자리 입력: ')
    order_price = get_total_price(tel)
    pay_gubun = input('카드?(1): ')

    order_list = [tel, order_price, pay_gubun]
    print(order_list)
    sql = """   insert into kio_order(ORDER_SEQ,TEL,ORDER_PRICE,PAY_GUBUN,REG_DATE)
                values (kio_order_seq.nextval, :1, :2, :3, sysdate)"""
    cur = conn.cursor()
    cur.execute(sql, order_list)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    get_goods_list()
    # while True:
    #     goods_list()
    #     cart_add()
    #     orders()
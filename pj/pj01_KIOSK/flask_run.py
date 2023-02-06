# pip install flask, requests
# 파이썬으로 개발 가능한 웹 프레임워크
# 쓰고싶은 샘플을 받고
# 폴더는 static디렉토리로 / 동적인것들
# html은 templates디렉토리로 / 디자인
# 맘에드는놈을 index.html로 변경
# 이미지경로 수정


# mvc패턴 view-controller-model 원래는 가운데 controller가 있어야 진짜 웹임

from flask import Flask, make_response, jsonify, request, render_template, redirect
import cx_Oracle
import random

app = Flask(__name__)
app.secret_key = "0000"

@app.route('/')
def index():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select GOOD_SEQ, GOOD_NAME, GOOD_IMG, GOOD_PRICE, GOOD_DESC from KIO_GOODS"
    cur = conn.cursor()
    cur.execute(sql)
    goods_list = []
    for row in cur:
        good_dict = {}
        good_dict['GOOD_SEQ'] = row[0]
        good_dict['GOOD_NAME'] = row[1]
        good_dict['GOOD_IMG'] = row[2]
        good_dict['GOOD_PRICE'] = row[3]
        good_dict['GOOD_DESC'] = row[4]
        goods_list.append(good_dict)
    cur.close()
    conn.close()
    return render_template('index.html', GOODS_LIST = goods_list)
# 알아서 templates디렉토리 들어가서 index.html 불러옴

@app.route('/detail_view', methods=['GET']) # 아무거도 안해주면 겟방식임 근데 써주자
def detail_view():
    print('상세보기')
    prm_good_seq = request.args.get('prm_good_seq')
    print(prm_good_seq)
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """select GOOD_SEQ, GOOD_NAME, GOOD_IMG, GOOD_PRICE, GOOD_DESC from KIO_GOODS where GOOD_SEQ = :1"""
    cur = conn.cursor()
    cur.execute(sql, [prm_good_seq])
    goods_list = []
    for row in cur:
        good_dict = {}
        good_dict['GOOD_SEQ'] = row[0]
        good_dict['GOOD_NAME'] = row[1]
        good_dict['GOOD_IMG'] = row[2]
        good_dict['GOOD_PRICE'] = row[3]
        good_dict['GOOD_DESC'] = row[4]
        goods_list.append(good_dict)
    cur.close()
    conn.close()

    return render_template('product-single.html', GOOD_DICT = goods_list[0])

@app.route('/add_cart', methods=['POST'])
def add_cart():
    print("카트담기")
    good_seq = request.form.get('good_seq')
    amount = request.form.get('amount')
    price = request.form.get('good_price')
    print(good_seq, amount, price)

    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")

    sql = """   insert into KIO_CART(CART_SEQ,TEL,GOOD_SEQ,GOOD_PRICE,ORDER_AMOUNT, REG_DATE)
                    values(KIO_CART_SEQ.nextval, :1, :2, :3, :4, sysdate)"""
    cur = conn.cursor()
    cur.execute(sql, ['0505', good_seq, price, amount])
    conn.commit()

    sql = """   select g.GOOD_SEQ, g.GOOD_NAME, g.GOOD_IMG, g.GOOD_DESC, c.GOOD_PRICE, c.ORDER_AMOUNT, (c.GOOD_PRICE*c.ORDER_AMOUNT) as TOT_PRICE, c.CART_SEQ
                from KIO_GOODS g,  KIO_CART c
                where g.GOOD_SEQ = c.GOOD_SEQ
                and TEL = :1 """
    cur = conn.cursor()
    cur.execute(sql, ['0505'])
    cart_list = []
    for row in cur:
        good_dict = {}
        good_dict['GOOD_SEQ'] = row[0]
        good_dict['GOOD_NAME'] = row[1]
        good_dict['GOOD_IMG'] = row[2]
        good_dict['GOOD_DESC'] = row[3]
        good_dict['GOOD_PRICE'] = row[4]
        good_dict['ORDER_AMOUNT'] = row[5]
        good_dict['ORDER_PRICE'] = row[6]
        good_dict["CART_SEQ"] = row[7]
        cart_list.append(good_dict)

    sql = """   select sum(good_price*order_amount) as TOT from KIO_CART
                where tel= :1
                group by tel """
    cur = conn.cursor()
    cur.execute(sql, ['0505'])
    tot_price = list(cur)[0][0]

    cur.close()
    conn.close()
    print(tot_price)

    return render_template('cart.html', CART_LIST = cart_list, TOT_PRICE = tot_price)


@app.route('/del_cart', methods=['GET'])
def del_cart():
    print("삭제완료")
    prm_cart_seq = request.args.get('prm_cart_seq')
    print(prm_cart_seq)

    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """ delete from kio_cart where cart_seq = :1 """
    cur = conn.cursor()
    cur.execute(sql, [prm_cart_seq])
    conn.commit()

    sql = """   select g.GOOD_SEQ, g.GOOD_NAME, g.GOOD_IMG, g.GOOD_DESC, c.GOOD_PRICE, c.ORDER_AMOUNT, (c.GOOD_PRICE*c.ORDER_AMOUNT) as TOT_PRICE, c.CART_SEQ
                    from KIO_GOODS g,  KIO_CART c
                    where g.GOOD_SEQ = c.GOOD_SEQ
                    and TEL = :1 """
    cur = conn.cursor()
    cur.execute(sql, ['0505'])
    cart_list = []
    for row in cur:
        good_dict = {}
        good_dict['GOOD_SEQ'] = row[0]
        good_dict['GOOD_NAME'] = row[1]
        good_dict['GOOD_IMG'] = row[2]
        good_dict['GOOD_DESC'] = row[3]
        good_dict['GOOD_PRICE'] = row[4]
        good_dict['ORDER_AMOUNT'] = row[5]
        good_dict['ORDER_PRICE'] = row[6]
        good_dict["CART_SEQ"] = row[7]
        cart_list.append(good_dict)

    sql = """   select sum(good_price*order_amount) as TOT from KIO_CART
                    where tel= :1
                    group by tel """
    cur = conn.cursor()
    cur.execute(sql, ['0505'])
    tot_price = list(cur)[0][0]

    cur.close()
    conn.close()
    print(tot_price)

    return render_template('cart.html', CART_LIST=cart_list, TOT_PRICE=tot_price)


@app.route('/orders', methods=['POST'])
def orders():
    print("주문완료")
    order_price = request.form.get('order_price')
    pay_gubun = request.form.get('pay_gubun')
    print(order_price, pay_gubun)

    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """   insert into kio_order(ORDER_SEQ,TEL,ORDER_PRICE,PAY_GUBUN,REG_DATE)
                    values (kio_order_seq.nextval, :1, :2, :3, sysdate)"""
    cur = conn.cursor()
    cur.execute(sql, ['0505', order_price, str(pay_gubun)])
    conn.commit()
    cur.close()
    conn.close()

    return redirect("/")  #플라스크에서 플라스크 갈때  redirect("/주소주소")





@app.route('/test')
def test_list():
    test_list = [1,2,3]
    test_dict = {'uid':'kim', 'upw':'111'}
    test_list_dict = [{'uid':'kim2', 'upw':'222'},
                       {'uid':'kim3', 'upw':'333'}]

    return render_template('test.html',
                           KEY_TEST_LIST = test_list,
                           KEY_TEST_DICT = test_dict,
                           KEY_TEST_LIST_DICT = test_list_dict)

@app.route('/test_prm_get', methods=['GET'])
def test_prm_get():
    print('겟방식')
    id = request.args.get('DDD_ID') # 폼태그를 쓰면 name뒤에 있는걸 써야하고 폼태그가 아니면 ?뒤에 키값을 써줘야함
    pw = request.args.get('DDD_PW')
    print(id, pw)
    return id+','+pw

@app.route('/test_prm_post', methods=['POST'])
def test_prm_post():
    print('포스트방식')
    id = request.form.get('DDD_ID') # 포스트는 무조건 폼안에 넣고 name뒤에 있는거 써야함
    pw = request.form.get('DDD_PW')
    print(id, pw)
    return id+','+pw

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost', port=80) # 0.0.0.0: 'localhost' 웹서비스 기본포트 80
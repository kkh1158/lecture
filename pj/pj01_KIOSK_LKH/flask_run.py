#------------------------------------------------
# pip install Flask,  requests
#------------------------------------------------

from flask import Flask, session, render_template, make_response, jsonify, request, redirect, url_for

import cx_Oracle

import random
app = Flask(__name__)

app.secret_key = "1111122222"


@app.route('/')
def index():

    tel = str(random.randint(10, 99)) + str(random.randint(10, 99))
    session['MY_TEL_SESSION'] = tel
    return render_template('index.html')



@app.route('/menu')
def menu():
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "select GOOD_SEQ,GOOD_NAME,GOOD_IMG,GOOD_PRICE,GOOD_DESC from kio_goods order by reg_date desc"
    cur = conn.cursor()
    cur.execute(sql)
    goods_list_dict = []
    for row in cur:
        #[3, 'CRISPY CHICKEN', 'static/images/menu/burger-11.jpg', 11, 'Chicken breast, chilli sauce, tomatoes, pickles, coleslaw']
        dic = {}
        dic["GOOD_SEQ"]  = row[0]
        dic["GOOD_NAME"] = row[1]
        dic["GOOD_IMG"]  = row[2]
        dic["GOOD_PRICE"] = row[3]
        dic["GOOD_DESC"] = row[4]
        goods_list_dict.append(dic)
    cur.close()
    conn.close()
    print(goods_list_dict)

    return render_template('menu.html'
                           , KEY_GOODS_LIST_DICT = goods_list_dict)





@app.route('/detail_view',  methods=['GET'])
def detail_view():
    v_seq = request.args.get("prm_good_seq")

    print("상세보기")
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """  select GOOD_SEQ,GOOD_NAME,GOOD_IMG,GOOD_PRICE,GOOD_DESC
                from kio_goods
                where good_seq= :1"""
    cur = conn.cursor()
    cur.execute(sql, [v_seq])
    goods_list_dict = []
    for row in cur:
        # [3, 'CRISPY CHICKEN', 'static/images/menu/burger-11.jpg', 11, 'Chicken breast, chilli sauce, tomatoes, pickles, coleslaw']
        dic = {}
        dic["GOOD_SEQ"] = row[0]
        dic["GOOD_NAME"] = row[1]
        dic["GOOD_IMG"] = row[2]
        dic["GOOD_PRICE"] = row[3]
        dic["GOOD_DESC"] = row[4]
        goods_list_dict.append(dic)
    cur.close()
    conn.close()
    print(goods_list_dict)

    return render_template('product-single.html', KEY_GOODS_LIST_DICT = goods_list_dict)



def mydef_cart_list() :
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """ select g.GOOD_SEQ, g.GOOD_NAME, g.GOOD_IMG, g.GOOD_DESC
                          , c.GOOD_PRICE,  c.ORDER_AMOUNT
                          ,  (c.GOOD_PRICE*c.ORDER_AMOUNT) as TOT_PRICE
                          , c.CART_SEQ , c.TEL
                    from KIO_GOODS g,  KIO_CART c
                    where g.GOOD_SEQ = c.GOOD_SEQ
                          and TEL = :1
                """
    cur = conn.cursor()
    cur.execute(sql,  [session['MY_TEL_SESSION']])
    goods_list_dict = []
    for row in cur:
        # [3, 'CRISPY CHICKEN', 'static/images/menu/burger-11.jpg', 11, 'Chicken breast, chilli sauce, tomatoes, pickles, coleslaw']
        dic = {}
        dic["GOOD_SEQ"] = row[0]
        dic["GOOD_NAME"] = row[1]
        dic["GOOD_IMG"] = row[2]
        dic["GOOD_DESC"] = row[3]
        dic["GOOD_PRICE"] = row[4]
        dic["ORDER_AMOUNT"] = row[5]
        dic["TOT_PRICE"] = row[6]
        dic["CART_SEQ"] = row[7]
        dic["TEL"] = row[8]
        goods_list_dict.append(dic)
    cur.close()
    conn.close()
    return goods_list_dict


@app.route('/add_cart',  methods=['POST'])
def add_cart():

    v_good_seq   = request.form.get("good_seq")      #hidden
    v_good_price = request.form.get("good_price")  #hidden
    v_amount     = request.form.get("amount")        #수량
    print("카트담기")

    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """ insert into
        KIO_CART(CART_SEQ, TEL, GOOD_SEQ, GOOD_PRICE, ORDER_AMOUNT, REG_DATE)
        values(KIO_CART_SEQ.nextval, :1, :2, :3, :4, sysdate)"""
    cur = conn.cursor()
    cur.execute(sql, [ session['MY_TEL_SESSION'], v_good_seq, v_good_price, v_amount])
    conn.commit()
    cur.close()
    conn.close()

    goods_list_dict = mydef_cart_list()
    return render_template('cart.html'
                           , KEY_GOODS_LIST_DICT = goods_list_dict)


@app.route('/cart_delete',  methods=['GET'])
def cart_delete():
    v_cart_seq = request.args.get("prm_cart_seq")
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = "delete from kio_cart where cart_seq = :1"
    cur = conn.cursor()
    cur.execute(sql, [v_cart_seq])
    conn.commit()
    cur.close()
    conn.close()

    goods_list_dict = mydef_cart_list()
    return render_template('cart.html', KEY_GOODS_LIST_DICT=goods_list_dict)


@app.route('/orders',  methods=['POST'])
def orders():
    v_price = int(request.form.get("order_price"))

    print("주문완료")
    conn = cx_Oracle.connect("ai", "0000", "localhost:1521/XE")
    sql = """insert into
        kio_order(ORDER_SEQ, TEL, ORDER_PRICE, PAY_GUBUN, REG_DATE)
        values(kio_order_seq.nextval, :1, :2, '1', sysdate)"""
    cur = conn.cursor()
    cur.execute(sql, [session['MY_TEL_SESSION'], v_price])
    conn.commit()
    cur.close()
    conn.close()

    session.pop('MY_TEL_SESSION')

    return redirect("/")  #메인화면으로 가기


@app.route('/test')
def test_list():
    test_list = [1,2,3]
    test_dict = {"uid":"kim", "upw":"111"}
    test_list_dict= [ {"uid": "kim1", "upw": "555"},
                      {"uid": "kim2", "upw": "666"} ]

    return render_template('test.html'
        , KEY_TEST_LIST = test_list
        , aaa = test_dict
        , KEY_TEST_LIST_DICT = test_list_dict
                           )


@app.route('/test_prm_get', methods=['GET'])
def test_prm_get():
    id = request.args.get('DDD_ID')
    pw = request.args.get('DDD_PW')
    print(id, pw)
    return id+","+pw

@app.route('/test_prm_post', methods=['POST'])
def test_prm_post():
    id = request.form.get('DDD_ID')
    pw = request.form.get('DDD_PW')
    print(id, pw)
    return id+","+pw



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
from flask import Flask, make_response, jsonify, request, render_template, redirect
import cx_Oracle
import random

app = Flask(__name__)
app.secret_key = "0000"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_get', methods=['GET'])
def form_get():
    print('get방식')
    id = request.args.get('userid')
    pw = request.args.get('userpw')
    print('id:', id)
    print('pw:', pw)
    mylist = [id, pw]
    return render_template('result.html', KEY_MYDATA=mylist)

@app.route('/form_post', methods=['POST'])
def form_post():
    print('post방식')
    id = request.form.get('userid')
    pw = request.form.get('userpw')
    print('id:', id)
    print('pw:', pw)
    mylist = [id, pw]
    var_list_dict = [{"KID": id, "KPW": pw},
                     {"KID": "kim", "KPW": 111},
                     {"KID": "park", "KPW": 222}]
    return render_template('result.html', KEY_MYDATA=var_list_dict)

# rest란?
# 1. 비동기/동기
# 2. 외부 자원을 텍스트나 제이슨으로 가져오기
# 3. 웹서비스 요청/응답
# 4. 분산서버 서비스
@app.route('/form_rest_text_text', methods=['POST'])
def form_rest_text_text():
    print('receive: text')
    id = request.form.get('userid')
    pw = request.form.get('userpw')
    print(id+pw)
    print('return: text')
    return id+pw

@app.route('/form_rest_json_text', methods=['POST'])
def form_rest_json_text():
    print('receive: json')
    dict = request.get_json()
    print(dict)
    print('return: text')
    return dict

@app.route('/form_rest_json_json', methods=['POST'])
def form_rest_json_json():
    print('receive: json')
    dict = request.get_json()
    print(dict)
    print('return: json')
    return jsonify(dict)
## return json.dump({"msg":"form_rest_json_json"})

@app.route('/form_rest_uri/<prm1>/<prm2>', methods=['POST'])
def form_rest_uri(prm1, prm2):
    print(prm1, prm2)
    return "form_rest_uri"

if __name__ == '__main__':
    app.debug = True
    app.run(host='127.0.0.1', port=80)
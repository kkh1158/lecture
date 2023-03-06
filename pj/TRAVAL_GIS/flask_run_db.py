#------------------------------------------------
# pip install Flask,  requests
# ----------------------------------OpenAPI KEY : cptjvrh7ki6dxd9q
# 제주관광공사_비짓제주 관광정보 오픈 (API)
# https://www.data.go.kr/data/15076361/openapi.do
# http://api.visitjeju.net/vsjApi/contents/searchlist
#------------------------------------------------

from flask import Flask, session, render_template, make_response, jsonify, request, redirect, url_for
from sqlalchemy import create_engine, text
import cx_Oracle

import pandas as pd
import numpy as np
import random

import json
import folium
from folium import plugins
import re
import googlemaps
import pprint
import requests

app = Flask(__name__)
app.secret_key = "1111122222"


##################################################################################################################
"""
CREATE TABLE JEJU_USERS 
(
  SEQ VARCHAR2(20) PRIMARY KEY 
, USERID VARCHAR2(20) NOT NULL 
, COLUMN2 VARCHAR2(20) NOT NULL 
, USERNM VARCHAR2(20) NOT NULL 
);
create sequence JEJU_USERS_SEQ start with 1 increment by 1;
insert into jeju_users values(JEJU_USERS_SEQ.nextval, 'lee', '111','아무개');
insert into jeju_users values(JEJU_USERS_SEQ.nextval, 'hong', '222','홍길동');
commit;
"""

""" -----------------------------------------------------
[화면] 로그인 폼
 ----------------------------------------------------- """
@app.route('/login_form', methods=["get"])
def login_form():
    return render_template('login_form.html')

""" -----------------------------------------------------
[처리부] 로그인 
 ----------------------------------------------------- """
@app.route('/login', methods=["post"])
def login():
    userid = request.form.get("userid")
    userpw = request.form.get("userpw")

    engine = create_engine("oracle+cx_oracle://ai:0000@localhost:1521/XE")
    df = pd.read_sql(text(f"SELECT * FROM JEJU_USERS where userid='{userid}' and userpw='{userpw}'"), con=engine.connect())
    engine.dispose()

    if df.shape[0] > 0 :
        session['USER_ID_SESSION'] = userid
        return redirect("/")
    else :
        return redirect("/login_form")

""" -----------------------------------------------------
[처리부] 로그아웃
 ----------------------------------------------------- """
@app.route('/logout', methods=["get"])
def logout():
    session.pop('USER_ID_SESSION')
    return redirect("/")

""" -----------------------------------------------------
[화면] 회원가입 폼
 ----------------------------------------------------- """
@app.route('/register_form', methods=["get"])
def register_form():
    return render_template('register_form.html')


##################################################################################################################

""" -----------------------------------------------------
[공통함수] 리스트+지도마커 생성
 ----------------------------------------------------- """
def make_map_html(cate='숙박', search_str="", contentsid_list=None):
    # df = pd.read_csv("./datasets_jeju/data.csv")
    # print(df['label'].value_counts())
    engine = create_engine("oracle+cx_oracle://ai:0000@localhost:1521/XE")




    """ -----------------------------------------------------
    [처리부] 리스트 
    ----------------------------------------------------- """
    #----------- 메인화면 : 관광명소 검색 시
    if len(search_str) > 0 :
        # df = df[ df['title'].str.contains(search_str) ]
        df = pd.read_sql(text(f"SELECT * FROM JEJU_TRAVEL where title like '%{search_str}%'"), con=engine.connect())
    # ----------- 로그인 > 마이페이지 : 찜목록 출력 시
    elif contentsid_list is not None:
        # df = df[df['contentsid'].isin( contentsid_list ) ]   # ['CONT_000000000500349', 'CONT_000000000500477', 'CNTS_000000000001195']
        df = pd.read_sql(text(f"SELECT * FROM JEJU_TRAVEL where contentsid in {contentsid_list}"), con=engine.connect())
    # ----------- 메인화면 기본 관광지 출력
    else :
        # df = df[ df['label'] == cate ]
        df = pd.read_sql(text(f"SELECT * FROM JEJU_TRAVEL where label = '{cate}'"), con=engine.connect())

    #df['tag'] = df['tag'].apply(lambda x: x.split(",")[0] if len(x) > 0 else cate)
    df = df[['contentsid', 'title', 'latitude','longitude', 'address', 'phoneno', 'tag', 'likecnt', 'reviewcnt', 'evelpt', 'thumb']]

    engine.dispose()

    """ -----------------------------------------------------
    [처리부] 지도마커 
    ----------------------------------------------------- """
    geo_list  = []
    name_list = []
    for i in range(len(df)):
        lat = df.iloc[i]['latitude']
        lng = df.iloc[i]['longitude']
        sname = df.iloc[i]['title']
        sid = df.iloc[i]['contentsid']
        geo_list.append((lat, lng))
        popup_url = f"'/detail_view?contentsid={sid}'"
        popup_option = "'status=no,menubar=no,toolbar=no,scrollbars=yes,resizable=yes,width=400,height=600'"
        popup_html = f"""<font size=2><b><a href=\"javascript:window.open({popup_url},'',{popup_option})\">{sname}</a></b></font><br> 
                        {df.iloc[i]['address']}
                        <img src='{df.iloc[i]['thumb']}' width=150 height=100>
                        {df.iloc[i]['phoneno']}"""
        name_list.append(popup_html)
    map = folium.Map(location=[33.41041350000001, 126.4913534], zoom_start=11,
                     tiles='OpenStreetMap')  # Stamen Terrain')
    plugins.MarkerCluster(geo_list, popups=name_list).add_to(map)
    # ---------------------------------------------------
    # web browser에 보이기 위한 준비
    map.get_root().width = "800px"
    map.get_root().height = "600px"
    html_str = map.get_root()._repr_html_()

    return html_str, df[:4]



##################################################################################################################

""" -----------------------------------------------------
[처리부 : REST] 메인화면 우측 지도하단 네이게시션 바 - 카테별 리스트+지도마커 생성
        카테 : '음식점', '관광지', '숙박', '쇼핑' 
 ----------------------------------------------------- """
@app.route('/search_map_html') #, methods=['''POST'])
def search_map_html(cate='숙박', search_str=""):
    # prm_dic = request.get_json()
    # print(prm_dic['cate'])

    if request.method == "GET":
        cate = request.args.get("cate")
        search_str = request.args.get("search_str")
        print("GET", cate, search_str)
    elif request.method == "POST":
        cate = request.form.get("cate", default='숙박')
        search_str = request.form.get("search_str", default='숙박')
        print("POST", cate, search_str)

    if bool(cate) == False:
        cate = '숙박'
    if bool(search_str) == False:
        search_str = ''

    """ -----------------------------------------------------
    [호출] 리스트+지도마커 공통함수 
    ----------------------------------------------------- """
    html_str, df = make_map_html(cate=cate, search_str=search_str)

    #-------------------STRING으로 전달할 경우 ----------------------
    # df_json_str = df.to_json(orient='records')
    # res_string = json.dumps({"KEY_MAP_HTML": html_str, "KEY_DF_JSON": df_json_str})
    # return res_string

    # -------------------OBJECT로 전달할 경우 ----------------------
    df_json_str = df.to_json(orient='records')
    res_object  = {"KEY_MAP_HTML": html_str, "KEY_DF_JSON_STR": df_json_str}
    #print(type(jsonify( res_object )), jsonify( res_object ))   # <Response 311603 bytes [200 OK]>
    #print(type(json.dumps(res_object)) ,  json.dumps(res_object) )
    #return jsonify( res_object )
    return json.dumps(res_object)


""" -----------------------------------------------------
[화면] 메인
 ----------------------------------------------------- """
@app.route('/', methods=["get", "post"])
def index():
    # session['USER_ID_SESSION'] = USER_ID
    if request.method == "GET":
        cate = request.args.get("cate")
        search_str = request.args.get("search_str")
        print("GET", cate, search_str)
    elif request.method == "POST":
        cate = request.form.get("cate", default='숙박')
        search_str = request.form.get("search_str", default='숙박')
        print("POST", cate, search_str)


    """ -----------------------------------------------------
    [호출] 리스트+지도마커 공통함수 
    ----------------------------------------------------- """
    if bool(cate) == False :
        cate = '숙박'
    if bool(search_str) == False:
        search_str = ''
    html_str, df = make_map_html(cate=cate, search_str=search_str)
    df_json_str = df.to_json(orient='records')
    df_json     = json.loads(df_json_str)

    return render_template('index.html' ,
                           KEY_CATE=cate,
                           KEY_MAP_HTML=html_str,
                           KEY_DF_JSON_STR=df_json)


##################################################################################################################

""" -----------------------------------------------------
[처리부 -> 화면 : 찜목록] 리스트+지도마커 생성 --> 화면 이동
 ----------------------------------------------------- """
@app.route('/booking', methods=["get"])
def booking():
    if session['USER_ID_SESSION'] == False:
        return redirect("/login_form")
    else :
        try :
            """ -----------------------------------------------------
           [호출] 리스트+지도마커 공통함수 
           ----------------------------------------------------- """
            with open(file=f"./user_booking/{session['USER_ID_SESSION']}.txt", encoding='UTF-8', mode='r') as fr:
                contentsid_list = fr.readlines()
            contentsid_list = [contentsid.strip()  for contentsid in contentsid_list]
            html_str, df = make_map_html(cate="", search_str="", contentsid_list= contentsid_list)
            df_json_str = df.to_json(orient='records')
            df_json = json.loads(df_json_str)

            return render_template('booking.html',
                                   KEY_MAP_HTML=html_str,
                                   KEY_DF_JSON=df_json)

        except :
            return redirect("/")


@app.route('/booking_add', methods=["get"])
def booking_add():
    contentsid = request.args.get("contentsid")
    print("GET", contentsid)

    if bool(contentsid) == False:
        return "500"
    elif session['USER_ID_SESSION'] == False:
        return "403"
    else :
        try :
            with open(file=f"./user_booking/{session['USER_ID_SESSION']}.txt", encoding='UTF-8', mode='a') as fw:
                fw.write(contentsid+"\n")
            return "200"
        except :
            return "500"


##################################################################################################################

""" -----------------------------------------------------
[처리부 : 상세화면] 관련 유튜브영상 가져오기
# pip install youtube-search-python
 ----------------------------------------------------- """
from youtubesearchpython import VideosSearch
# import pandas as pd
# import json
#------------------------------------------------------------
def my_youtube_search(search_str='제주도', nrows=3) :
	videosSearch = VideosSearch(search_str, limit=nrows)
	json_res = videosSearch.result()
	#print(videosSearch.result())  ## [{},{},{}]
	#print(json.dumps(videosSearch.result(), sort_keys=True, indent=4))
	movie_list = json_res['result']
	#print(json.dumps(movie_list, sort_keys=True, indent=4))

	tot_list = []
	for movie in movie_list:
		dict = {}
		# print(movie['thumbnails'][0]['url'])
		# print(movie['link'])
		# print(movie['title'])
		dict["title"] 	 = movie['title']
		try :
			dict["movie"] = movie['richThumbnail']['url']
		except :
			dict["movie"] = movie['thumbnails'][0]['url']

		dict["img"] 	 = movie['thumbnails'][0]['url']
		dict["duration"] = movie['duration']
		dict["url"] 	 = movie['link']
		dict["rdate"] 	 = movie['publishedTime']
		dict["cnt"]  = movie['viewCount']['text']
		tot_list.append(dict)
	return tot_list  #[{},{}]


""" -----------------------------------------------------
[처리부 : 상세화면] 관련 리뷰댓글 가져오기
# pip install youtube-search-python
 ----------------------------------------------------- """
def get_review_list(contentsid) :
    contentsid = "CONT_000000000500811"
    headers_val={
    'Cookie':'_gcl_au=1.1.1634613698.1677463189; Hm_lvt_f6d5e380b023c5b1e946de764e07a2a2=1677463189; _fbp=fb.1.1677463189486.1921927163; iceJWT=SDP+eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJBbm9ueW1vdXMiLCJhdWQiOiJlMjQ0NGQwOC05YjA0LTRjYmEtYWE5ZS1mZjdmYWQwNTFiZWIiLCJqdGkiOiJlMjQ0NGQwOC05YjA0LTRjYmEtYWE5ZS1mZjdmYWQwNTFiZWIiLCJpc3MiOiJJLU9OIiwiaWF0IjoxNjc3NzI5NTQwLCJleHAiOjE2Nzc4Mzc1NDB9.1vOyTpGacBX1tpd0HWvdiyIZJqwVSOgeg1LjzUsyLLOQKSe97czp7VAzOTi-_22JGGWRp1pBpdydYbvnGc1Svg; iceRefreshJWT=SDP+eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJBbm9ueW1vdXMiLCJhdWQiOiJiMjJiZDkyZC1lMDc5LTRhZTgtOGFhMy05NWQwZTJkNjY1OTMiLCJpc3MiOiJJLU9OIiwianRpIjoiZjY0NGE4NzMtZGNlMi00YTQ1LTljN2MtMThkZWNjMmVmYTcwIiwiaWF0IjoxNjc3NzI5NTQwLCJleHAiOjQxMDI0MTI0MDB9.JksFE8AaH3_BjU8YBiYy7KftXVYicOgc4coi4LZeJ_OsDButjABpsXuGN8qE6kpmgH1hh-KijjZnRdbiSQJZJg; _gid=GA1.2.1598970783.1677729565; Hm_lpvt_f6d5e380b023c5b1e946de764e07a2a2=1677730295; _ga=GA1.1.1913362389.1677463189; _ga_WR7WEFWP2T=GS1.1.1677729564.5.1.1677730541.0.0.0',
    'Host': 'api.visitjeju.net',
    }
    res = requests.get(f"https://api.visitjeju.net/api/contentsreview/list.json?_siteId=jejuavj&locale=kr&device=pc&contentsid={contentsid}&noUserid=xxxxx&sorting=created+desc,created+desc&pageSize=5&page=1"
                      , headers=headers_val)
    json_dic = json.loads(res.text)
    # print( json_dic )
    # print( len(json_dic["items"]) , json_dic["items"] )
    review_list = []
    for dic in json_dic["items"]:
        if bool(dic["created"]):
            created = dic["created"][:4] + "-" + dic["created"][4:6] + "-" + dic["created"][6:8]
        # print( dic["evelpt"], dic["tag"], dic["evelcontent"], dic["created"], dic["userid"]["usernm"])
        review_list.append( {"evelpt" : dic["evelpt"],
                             "tag" : dic["tag"],
                             "evelcontent" : dic["evelcontent"],
                             "created" : created,
                             "usernm" : dic["userid"]["usernm"]
                           })
    return review_list



""" -----------------------------------------------------
[화면] 상세화면 
 ----------------------------------------------------- """
@app.route('/detail_view', methods=['GET','POST'])
def detail():
    if request.method == "GET" :
        contentsid = request.args.get("contentsid", default='CONT_000000000500811')
        print("GET", contentsid)
    elif request.method == "POST" :
        contentsid = request.form.get("contentsid", default='CONT_000000000500349')
        print("POST", contentsid)
    else:
        contentsid = 'CONT_000000000500349'
        print("etc", contentsid)

    """ -----------------------------------------------------
   [호출] 리스트+지도마커 공통함수 
   ----------------------------------------------------- """
    html_str, df = make_map_html(cate="", search_str="",contentsid_list=[contentsid])
    df_json_str = df.to_json(orient='records')
    df_json = json.loads(df_json_str)


    """ -----------------------------------------------------
    [호출] 관련댓글
    ----------------------------------------------------- """
    try :
        review_list = get_review_list(contentsid)
        print(review_list)
    except :
        review_list = []

    """ -----------------------------------------------------
    [호출] 유튜브영상 
    ----------------------------------------------------- """
    try:
        search_str = df['title'].values[0]
        if bool(search_str) == False:
            search_str = "제주도"
        print(search_str)
        movie_list = my_youtube_search(search_str, 4)  # [  {title:}, {title:}, {}]
        print(movie_list)
    except:
        movie_list = []

    return render_template('detail.html', KEY_MAP_HTML=html_str
                           , KEY_DF=df_json[0]
                           , KEY_YT_LIST=movie_list
                           , KEY_REVIEW_LIST=review_list
                           )



##################################################################################################################

@app.route('/chart')
def chart():
    return render_template('chart_test.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8877)
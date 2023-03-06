
import flask
import pprint
import json
import pandas as pd
df = pd.DataFrame({"name":["kim","park"], "pw":[11,22]})
print(df.head())
print("-"*30)


dj_str = df.to_json()  #orient="records")
#aa = df.to_json(orient="records")
print("1  df.to_json() : ", type(dj_str), dj_str)

df_dict = df.to_dict()
print("2  df.to_dict() : ", type(df_dict) , df_dict)



df_dict_str = json.dumps(df_dict)
print("3  json.dumps(df_dict) : ", type(df_dict_str), df_dict_str)

ddstr_json = json.loads(df_dict_str)
print("4  json.loads(df_dict_str) : ", type(ddstr_json), ddstr_json)


# dic = jsonify( {"name":["kim","park"], "pw":[11,22]} )
# print(dic)


# https://velog.io/@matisse/flask-jsonify-%EC%99%80-json.dumps%EC%9D%98-%EC%B0%A8%EC%9D%B4
# def jsonify(*args, **kwargs):
#     if __debug__:
#         _assert_have_json()
#     return current_app.response_class(json.dumps(dict(*args, **kwargs),
#         indent=None if request.is_xhr else 2), mimetype='application/json')


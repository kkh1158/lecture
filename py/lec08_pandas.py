# pip install
# numpy
# pandas
# jupyter
# jupyterlab

# 파일 세팅 툴 터미널 쉘패스에
# powershell -NoExit -File ".\venv\Scripts\activate.ps1"
import numpy as np
import pandas as pd

s = pd.Series( [1, 3, 5, np.nan, 6, 8] ) # Series 클래스 안에 리스트를 넣어줌
print(s)
print(type(s))

dates = pd.date_range("20130101", periods=6) # dtype='datetime64[ns]'
print(dates)

a = np.random.randn(6, 4)
print(type(a))

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=['A', 'B', 'C', 'D'])
print(df)
print(df.values)
print(df.to_numpy())
print(type(df.values))
print(type(df.to_numpy()))
print(df.index)
print(df.columns)
# 1리스트타입 2np.배열 3딕트

my_array = np.array([1,2,3])
print(my_array)

pd.read_csv()

from shutil import copy, copy2, copyfile

orig="C:\\AI\\pythonProject\\venv\\lecture\\file\\test_utf8.txt"
dest="C:\\AI\\pythonProject\\venv\\lecture\\file\\test_write.txt"
# copy(원본파일경로, 타겟파일경로)
# copy("/etc/memo/a.txt", "/etc/memo2/b.txt")
# copy2("/etc/memo/a.txt", "/etc/memo2")  --> /etc/memo2/a.txt
copyfile(orig, dest)

# ------------------------------
# 파일 디렉토리 내장함수
# 절대경로(Absolute Path): C:\AI\pythonProject\venv\lecture\py\lec05_파일디렉토리함수.py
# 상대경로(Relative Path)
#   /   아래
#   .   현재폴더
#   ..  상위폴더
# ------------------------------
import os
from os.path import isfile, isdir, join

# getcwd(): 현재 경로
path = os.getcwd()
print('현재 경로:', path) # C:\AI\pythonProject\venv\lecture\py

# listdir(): 경로를 리스트로
path_list=os.listdir(os.getcwd())
print('현재 경로에 뭐뭐있나 리스트로:', path_list)

# dirname(경로): 상위 경로
ppath=os.path.dirname(os.getcwd())
print('상위 경로:', ppath)

# join: 경로 붙이기
fpath = join(ppath, 'file')
print('file 디렉토리:', fpath)

# 원하는 경로의 목록을 리스트로
flist = os.listdir(join(os.path.dirname(os.getcwd()), 'file'))
print('\\file list', flist)
print('--------------------------------------------------')

import datetime as dt

# path = "C:\\AI\\test.txt"
# time_f = os.path.getmtime(path)
# print(type(time_f), time_f)
# time_t = dt.datetime.fromtimestamp(time_f)
# print(type(time_t), time_t)
# time_s = dt.datetime.strftime(time_t, '%Y-%m-%d %H:%M:%S')
# print(type(time_s), time_s)

# p = "C:\\AI\\pythonProject\\venv\\lecture"
# for f in os.listdir(p):
#     path = join(p, f)
#     time_f = os.path.getmtime(path)
#     time_t = dt.datetime.fromtimestamp(time_f)
#     time_s = dt.datetime.strftime(time_t, '%Y-%m-%d %H:%M:%S')
#     if os.path.isdir(path):
#         print('\t[D]\t', time_s, '\t', f)
#     elif os.path.isfile(path):
#         fsize = os.path.getsize(path) # byte
#         print('\t[F]\t', time_s, '\t', f, '\t', fsize/1024, 'KB')

# p = "C:\\AI"
# for f in os.listdir(p):
#     path = join(p, f)
#     time_f = os.path.getmtime(path)
#     time_t = dt.datetime.fromtimestamp(time_f)
#     time_s = dt.datetime.strftime(time_t, '%Y-%m-%d %H:%M:%S')
#     if os.path.isdir(path):
#         print('\t[D]\t', time_s, '\t', f)
#
#         for ff in os.listdir(path):
#             subpath = join(path, ff)
#             subtime_f = os.path.getmtime(path)
#             subtime_t = dt.datetime.fromtimestamp(subtime_f)
#             subtime_s = dt.datetime.strftime(subtime_t, '%Y-%m-%d %H:%M:%S')
#             if os.path.isdir(subpath):
#                 print('\t\t[D]\t', subtime_s, '\t', ff)
#
#             elif os.path.isfile(subpath):
#                 fsize = os.path.getsize(path)  # byte
#                 print('\t\t[F]\t', subtime_s, '\t', ff, '\t', fsize/1024, 'KB')
#
#     elif os.path.isfile(path):
#         fsize = os.path.getsize(path)  # byte
#         print('\t[F]\t', time_s, '\t', f, '\t', fsize/1024, 'KB')

# 탐색기
def tam(p, cnt=0):
    for f in os.listdir(p):
        path = join(p, f)
        time_f = os.path.getmtime(path)
        time_t = dt.datetime.fromtimestamp(time_f)
        time_s = dt.datetime.strftime(time_t, '%Y-%m-%d %H:%M:%S')
        if os.path.isdir(path): # 디렉토리면
            print(cnt * '\t', end='')
            print('[D]\t', time_s, '\t', f)
            tam(path, cnt+1)

        elif os.path.isfile(path): # 파일이면
            fsize = os.path.getsize(path)  # byte
            print(cnt * '\t', end='')
            print('[F]\t', time_s, '\t', f, '\t', fsize/1024, 'KB')

tam(os.getcwd())
#tam(os.path.dirname(os.getcwd()))

# ------------------------------
# glob.py
# /etc/*.txt
# /etc/*c/a*.log
# -------------------------------

# import glob

# print(glob.glob("C:\\p*")) # glob의 결과값은 리스트

# glob_list = glob.glob("C:\\AI\\pythonProject\\venv\\lecture\\py\\lec*.py")
# module_list = []
# for g in glob_list:
#     sp = g.split('\\')
#     py = sp[-1]
#     module_list.append(py)
# print(module_list)

# for g in glob_list:
#     print('----------')
#     print(os.path.split(g))     # (경로, 파일명)
#     print(os.path.basename(g))  # 파일명
#     print(os.path.dirname(g))   # 경로
#     print(os.path.splitext(g))  # (확장자빠진나머지, 확장자)
#     print('----------')
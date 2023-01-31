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

print(os.getcwd()) # 내 경로
path=os.listdir(os.getcwd())
print('path', path)
uppath=os.listdir('../')
print('uppath', uppath)

p = join("C:\\AI\\pythonProject\\venv\\lecture", 'file')
p = "C:\\AI\\pythonProject\\venv\\lecture"
print('--------------------------------------------------')

import datetime as dt

# path = "C:\\AI\\test.txt"
# time_f = os.path.getmtime(path)
# print(type(time_f), time_f)
# time_t = dt.datetime.fromtimestamp(time_f)
# print(type(time_t), time_t)
# time_s = dt.datetime.strftime(time_t, '%Y-%m-%d %H:%M:%S')
# print(type(time_s), time_s)

#print(dt.datetime.strftime(mtime), 'YYYY-MM-DD')

# p = "C:\\AI\\pythonProject\\venv\\lecture"
# p = "C:\\AI\\pythonProject\\venv"
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

def tam(p, cnt=0):
    for f in os.listdir(p):
        path = join(p, f)
        time_f = os.path.getmtime(path)
        time_t = dt.datetime.fromtimestamp(time_f)
        time_s = dt.datetime.strftime(time_t, '%Y-%m-%d %H:%M:%S')
        if os.path.isdir(path):
            print(cnt*'\t',end='')
            print('[D]\t', time_s, '\t', f)
            tam(path, cnt+1)

        elif os.path.isfile(path):
            fsize = os.path.getsize(path)  # byte
            print(cnt * '\t', end='')
            print('[F]\t', time_s, '\t', f, '\t', fsize, 'byte')

tam("C:\\AI")
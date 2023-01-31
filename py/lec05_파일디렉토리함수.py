from shutil import copy, copy2, copyfile

orig="C:\\AI\\pythonProject\\venv\\lecture\\file\\test_utf8.txt"
dest="C:\\AI\\pythonProject\\venv\\lecture\\file\\test_write.txt"
# copy(원본파일경로, 타겟파일경로)
# copy("/etc/memo/a.txt", "/etc/memo2/b.txt")
# copy2("/etc/memo/a.txt", "/etc/memo2")  --> /etc/memo2/a.txt
copyfile(orig, dest)

# 파일 디렉토리 내장함수
import os
from os.path import isfile, isdir, join

print(os.getcwd())
print(os.listdir(os.getcwd()))
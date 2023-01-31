# 빅데이터를 다루는 툴
# NOSQL(HBase, MongoDB)
# 데이터를 파일로 저장

# 분산 파일 서버
# HDFS(Hadoop)
# 리눅스or유닉스 고가용 장비



# 파일 생성
# open(파일경로, 모드{'r':읽기, 'w':쓰기, 'a':추가})
# 리눅스/유닉스:      /etc/guest/aa/txt
# 윈도우:            C:\ai\bb.txt
# 파이썬 프로그래밍:   C:\\ai\\bb.txt or C:/ai/bb.txt
ansi = "C:\\AI\\pythonProject\\venv\\lecture\\file\\test_ansi.txt"
utf8 = "C:\\AI\\pythonProject\\venv\\lecture\\file\\test_utf8.txt"
file_ansi = open(file=ansi, mode='r')
file_utf8 = open(file=utf8, mode='r', encoding='UTF-8')


# 파일 읽기/쓰기
# readline() - 라인 1줄로 리턴
print('\n'+'readline()'+'-'*99)
txt_ansi = file_ansi.readline()
print(txt_ansi) # 동해물과
file_ansi.close()

# 문자열 처리 방식: while
print('\n'+'readline()', 'while'+'-'*99)
while True:
    line = file_utf8.readline()
    if not line: break
    print(line, end='')
file_utf8.close()

# readlines() - 리스트로 리턴
print('\n'+'readlines()'+'-'*99)
f = open(file=utf8, mode='r', encoding='UTF-8')
lines = f.readlines() # 리스트값 근데 끝에 \n이 붙음
print(lines)    # ['동해물과\n', '백두산이\n', '마르고 닳도록']
                # \n: replace나 split 써서 데이터처리

# 리스트 처리 방식: 형진식 ''.join()
print('\n'+'readlines()', "''.join()"+'-'*99)
print(''.join(lines))

# 리스트 처리 방식: for
print('\n'+'readlines()', 'for () in []'+'-'*99)
for txt in lines:
    txt=txt.strip() # 공백,줄바꿈 제거
    print(txt)
f.close()

# read() - 전체 그대로 출력
print('\n'+'read()'+'-'*99)
f = open(file=utf8, mode='r', encoding='UTF-8')
txts = f.read()
print(txts)
f.close()

# with open() as
# close 까먹기 쉬우니 with open
print('\n'+'with open() as'+'-'*99)
with open(file=utf8, mode='r', encoding='UTF-8') as f:
    fread = f.read()
    print(fread)

# -----------------------------------------
# 파일 쓰기
# with open(file=파일경로, mode='w', encoding='UTF-8') as f
# -----------------------------------------
wpath="C:\\AI\\pythonProject\\venv\\lecture\\file\\test_write.txt"
with open(file=wpath, mode='w', encoding='UTF-8') as f:
    for i in range(1,11):
        f.write(str(i)+'\n')
print('=== write done ===')

# test_utf8.txt 파일을 test_write.txt에 복사
wpath="C:\\AI\\pythonProject\\venv\\lecture\\file\\test_write.txt"
rpath="C:\\AI\\pythonProject\\venv\\lecture\\file\\test_utf8.txt"
with open(file=wpath, mode='a', encoding='UTF-8') as wf: # mode={'a': 추가, 'w': 덮어쓰기}
    with open(file=rpath, mode='r', encoding='UTF-8') as rf:
        f=rf.read()
        print(f)
        print(type(f))
        print(len(f))
        wf.write(f)
print('=== write done ===')
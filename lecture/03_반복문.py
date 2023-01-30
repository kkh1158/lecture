# for 변수 in 리스트 :
#     반복실행문
#
# for 변수 in range(10) :
#     반복실행문
#
# while 조건식 :
#     반복실행문

emp=[7788, 7799, 7800]
empno=emp[0]
print(empno)
empno=emp[1]
print(empno)
empno=emp[2]
print(empno)

for empno in emp:
    print(empno)

#
# range(시작번호 '이상', 끝번호 '미만', 증감분)
# 시작번호 이상
# 끝번호 미만미만미만미만미만

print(list(range(5)))
print(list(range(1,6))) # 1부터 6미만의 값의 객체를 리스트를 통해 출력
print(list(range(1,10,2)))
print(list(range(10,0,-1)))

# range를 이용하여 1~10까지 출력
for n in range(1,11):
    print(n, end='\t')

print()

# 중첩 for문
for won in range(100,600,100):
    print(won, end='\t')
    for cnt in range(1,4):
        print(cnt, end='\t')
    print()

# 구구단
# 2단
# 2 * 1 = 2 ... 2 * 9 = 18
# 3단
# ......
# 9단
for dan in range(2,10):
    print(dan, '단', sep='')
    for gob in range(1,10):
        print(dan, 'X', gob, '=', dan*gob, sep='', end='\t')
    print()

# 2 4 6 8단
# *5만
for dan in range(2,10,2):
    print(dan, '단', sep='')
    for gob in range(1,6):
        print(dan, 'X', gob, '=', dan*gob, sep='', end='\t')
    print()

# 9 7 5 3단
# *9 *8 ... *5
for dan in range(9,2,-2):
    print(dan, '단', sep='')
    for gob in range(9,4,-1):
        print(dan, 'X', gob, '=', dan*gob, sep='', end='\t')
    print()

# 별찍기   n   2-n   1+n*2
#   *     0   2     1
#  ***    1   1     3
# *****   2   0     5
for n in range(3):
    for space in range(2-n):
        print(' ', end='')
    for star in range(1+n*2):
        print('*', end='')
    print()

for i in range(3):
    print(' ' * (2-i), end='')
    print((i * 2 + 1) * '*')

#       n   _   *(4-n)
# ****  0   0   4
#  ***  1   1   3
#   **  2   2   2
#    *  3   3   1

print()
for n in range(4):
    print(' '*n, end='')
    print('*'*(4-n))

print()
for j in range(4):
    for k in range(4):
        if j<=k:
            print('*', end='')
        else:
            print(' ', end='')
    print()

#       n   3-n n+1
#    *  0   3   1
#   **  1   2   2
#  ***  2   1   3
# ****  3   0   4
print()
for n in range(4):
    print(' '*(3-n), end='')
    print('*'*(n+1))

print()
for k in range(4):
    for j in range(4):
        if k<(3-j):
            print(' ', end='')
        else:
            print('*', end='')
    print()






# while 조건식:
#     반복실행문

num=5
while num<10:
    print('그렇다', num)
    num=num+1
print(num)

# while문 구구단
dan=2
while dan<=9:
    gob=1
    print(dan, '단', sep='')
    while gob<=9:
        print(dan, 'X', gob, '=', dan * gob, end='\t')
        gob=gob+1
    dan=dan+1
    print()
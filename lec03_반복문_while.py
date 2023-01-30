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
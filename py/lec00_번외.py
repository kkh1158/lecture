# 포문을 한줄로
# [ print(n*10) for n in range(5) ]

# 2중포문을 한줄로
# [ [ print(dan,'X',gob) for gob in range(1,10) ] for dan in range(2,10) ]

# 이프문을 한줄로
# print('1' if True else '0')

# 다중이프문을 한줄로
# s = 81
# print('A' if s>=90 else ('B' if s>=80 else 'C'))

# 포안에 이프
# [ print('이' if n==2 else '그외') for n in [1,2,3] ]

# 포안에 이프엘스
# [ print(i) for i in range(5) if i>=2 ]

# 람다
# print( ( lambda n1,n2:n1+n2 )( 5,7 ) )

# 함수를 람다로
# def jeomsu(score):
#     if score>=90:
#         return True
#     else:
#         return False
# print( ( lambda score:True if score>=90 else False )(99) )
# print( ( lambda x:jeomsu(x) )(88) )

# map 람다에 리스트넣기
# print( list( map( ( lambda x:x*10 ), [1,2,3,4,5] ) ) )

# 그렇다면 람다식을 사용하여 다음 연락처를 지역명을 뿌려보아라
# tel = ["02-222-3333", "032-222-3333","032-222-3333","031-222-3333"]
# 02  :  서울
# 032 : 인천
# 031 : 경기
# tel = ["02-222-3333", "032-222-3333","032-222-3333","031-222-3333"]
# print( list( map( ( lambda s:'서울' if s.split('-')[0]=='02' else ('경기' if s.split('-')[0]=='031' else '인천') ), tel ) ) )

#1부터100 합 출력
# s=0
# for i in range(1,101):
#     s = s + i
# print(s)
#
# def sum_lam(n):
#     sum=0
#     for i in range(1,n+1):
#         sum = sum + i
#     print(sum)
#
# (lambda x:sum_lam(x))(100)
#
# def nujeokhab(s,i):
#     s=s+i
#     if i==100:
#         return print(s)
#     nujeokhab(s,i+1)
# nujeokhab(0,1)
#
# print( ( lambda b:int(b*(b+1)/2) )( 100 ) )
# print('mmm')
# print(sum([1,2,3]))
# print(sum(x for x in range(1,101)))
# print( ( lambda s,e:sum(range(s,e+1)) )(1,100) )
# print( sum(x for x in range(1,101)) )

# 람다연습
# print(( lambda b : b/2*(b+1) )( 100 ))

# 정규표현식 연습
import re

res = re.search('\w+[.]','Heikkinend, Miss. Laina')
print(res.group)
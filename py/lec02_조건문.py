# if 조건식1 :
#     실행1
# [elif 조건식2 :
#     실행2
# elif 조건식3 :
#     실행3
# [else :
#     실행]]
# 들여쓰기를 스페이스나 탭으로 구분하여 명확하게 해줘야 함

# 90 이상이면 A
# 80 이상이면 B
# 아니면 C
score=80
if score>=90:
    print('A')
elif score>=80:
    print('B')
else:
    print('C')

# 90 이상이면  성별이 남성이면 1 여성이면 2
# 80 이상이면  성별이 남성이면 11 여성이면 22
# 아니면 0
score=80
gen='남'
if score>=90:
    if gen=='남':
        print(1)
    elif gen == '여':
        print(2)
elif score>=80:
    if gen=='남':
        print(11)
    elif gen=='여':
        print(22)
else:
    print(0)

# if문안에 and or 가능
if score>=90 and gen=='남':
    print(1)
elif score>=90 and gen=='여':
    print(2)
elif score>=80 and gen=='남':
    print(11)
elif score>=80 and gen=='여':
    print(22)
else:
    print(0)
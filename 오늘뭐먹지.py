import random
import time

요일 = ['월', '화', '수', '목', '금']
맛집리스트 = ['필동순대국', '부자돈까스', '설렁탕', '오매가매', '명궁', '닭한마리', '편의점도시락']
어제메뉴 = ''
오늘메뉴 = random.choice(맛집리스트)

for i, n in enumerate(range(5)):
    while 어제메뉴 == 오늘메뉴:
        오늘메뉴 = random.choice(맛집리스트)
    print(요일[i], ':', 오늘메뉴)
    어제메뉴 = 오늘메뉴

# for n in range(5):
#     print(오늘메뉴)
#     while True:
#         어제메뉴 = 오늘메뉴
#         오늘메뉴 = random.choice(맛집리스트)
#         if 오늘메뉴 != 어제메뉴:
#             break
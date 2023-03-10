a="10" # 바인딩한다
b="20"
print(a+b) # 1020

a="ABC"
b=10
print(a*b) # ABCABCABCABCABCABCABCABCABCABC

# 리스트 - index 0번째부터 시작
a=[1,2,3,4,'A']
a[2]='z'            # [1, 2, 'z', 4, 'A']
a.append(6)         # [1, 2, 'z', 4, 'A', 6]
a.insert(1,'bbb')   # [1, 'bbb', 2, 'z', 4, 'A', 6]
a.pop(0)            # ['bbb', 2, 'z', 4, 'A', 6]
a.remove('A')       # ['bbb', 2, 'z', 4, 6]
del a[3]            # ['bbb', 2, 'z', 6]
print(a)            # ['bbb', 2, 'z', 6]

# 튜플 - 리스트랑 비슷한데 내부값 변경 불가
# 데이터 전달할때 튜플로 전달
b=(1,2,3,4,5)
# b.append(6) 튜플은 이런거 안됨
print(b)        # 튜플은 조회용
print(b[1])

# 딕셔너리 - {키:값, 키:값}중복이면 겹쳐짐
d={'empno':7733, 'ename':'SMITH'}
print(d['empno'])   # 7733
d['job']='SALES'
d['ename']='CHANGE'
print(d)            # {'empno': 7733, 'ename': 'CHANGE', 'job': 'SALES'}

mem=[1,2,3,{0:'B', 1:'C'}]
print(mem[3][1])    # C

ytb = {
    "kind": "youtube#videoListResponse",
    "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/sDAlsG9NGKfr6v5AlPZKSEZdtqA\"",
    "videos": [
        {
            "id": "7lCDEYXw3mM",
            "kind": "youtube#video",
            "etag": "\"UCBpFjp2h75_b92t44sqraUcyu0/iYynQR8AtacsFUwWmrVaw4Smb_Q\"",
            "snippet": {
                "publishedAt": "2012-06-20T22:45:24.000Z",
                "channelId": "UC_x5XG1OV2P6uZZ5FSM9Ttw",
                "title": "Google I/O 101: Q&A On Using Google APIs",
                "description": "Antonio Fuentes speaks to us and takes questions on working with Google APIs and OAuth 2.0.",
                "thumbnails": {
                    "default": {
                        "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/default.jpg"
                    },
                    "medium": {
                        "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/mqdefault.jpg"
                    },
                    "high": {
                        "url": "https://i.ytimg.com/vi/7lCDEYXw3mM/hqdefault.jpg"
                    }
                },
                "categoryId": "28"
            },
            "contentDetails": {
                "duration": "PT15M51S",
                "aspectRatio": "RATIO_16_9"
            },
            "statistics": {
                "viewCount": "3057",
                "likeCount": "25",
                "dislikeCount": "0",
                "favoriteCount": "17",
                "commentCount": "12"
            },
            "status": {
                "uploadStatus": "STATUS_PROCESSED",
                "privacyStatus": "PRIVACY_PUBLIC"
            }
        }
    ]
}

# title, url, viewCount 출력
print(ytb['videos'][0]['snippet']['title'])
print(ytb['videos'][0]['snippet']['thumbnails']['default']['url'])
print(ytb['videos'][0]['statistics']['viewCount'])

nvr = {
    "urls": [
        {
            "url": "http://www.your-site.com/article-1",
            "type": "update"
        },
        {
            "url": "http://www.your-site.com/article-2",
            "type": "update"
        },
        {
            "url": "http://www.your-site.com/article-3",
            "type": "delete"
        },
        {
            "url": "http://www.your-site.com/article-4",
            "type": "delete"
        }
    ]
}

# type이 delete인 애들 url 출력
print(nvr['urls'][2]['url'])
print(nvr['urls'][3]['url'])

# 타입
print(type(5), 5)               # int
print(type('abc'), 'abc')       # str
print(type(1.1), 1.1)           # float
print(type([1,2,3]), [1,2,3])   # list
print(type((1,2,3)), (1,2,3))   # tuple
print(type({'empno':777,'deptno':10}), {'empno':777,'deptno':10}) # dict
print(type(True), True)         # bool: True, False (앞글자 대문자)

# 타입변환 형변환 cating
# print(3+'4')
print(str(3)+'4')   # 34
print(3+int('4'))   # 7
# print(4+3.7)
print(float(4)+3.7) # 7.7
print(bool(0))      # False
print(int(True))    # 1
print(float(True))  # 1.0
print(str(True))    # True

# 슬라이싱 slicing
# 문자열[시작이상:끝미만:증감(-거꾸로)]
msg='ABCDE'
print(msg[0:2]) # AB
print(msg[3:])  # DE
print(msg[-2:]) # DE

# 리스트[시작이상:끝미만:증감(-거꾸로)]
emps=[7733, 7822, 7922, 8000]
print(emps[1:3]) # [7822, 7922]

# license_plate = "24가 2210" 뒤에 네자리만
license_plate = "24가 2210"
print(license_plate[-4:])

# string='홀짝홀짝홀짝' 홀홀홀만
string='홀짝홀짝홀짝'
print(string[::2])

# string='python' 뒤집어서
string='python'
print(string[::-1])

# phone_number = "010-1111-2222" 하이픈 제거
phone_number = "010-1111-2222"
print(phone_number[:3], phone_number[4:8], phone_number[9:])
print(phone_number.replace('-', ' ')) # replace('이거를', '이거로')

print(('python', 'java')*4)

# 공백제거 strip() 정말정말 많이많이 쓰는 함수
data = '                 삼성전자             '
print(data.strip())

# 공백 또는 구분자 단위로 문자열 자르기 split()
a = 'hello world'
print(a.split()) # 리스트로 나오네?

# 폰넘버 가운데만 출력
print(phone_number.split('-')[1])

# 리스트 병합
lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang3 = lang1 + lang2
print(lang3)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang1.append(lang2) # lang1에 lang2를 리스트 통채로 넣음
print(lang1)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]
lang1.extend(lang2) # lang1에 lang2를 갖다 붙임
print(lang1)

# 길이체크
print(len(lang1))

# 홀수만 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

#-----------------
addr_list = [1, 2 , 3 ,'AA', {"name":"홍길동", "tel":123}]
# addr_list.pop(0)        #index삭제, 그냥은 맨뒤삭제
# addr_list.remove( {"name":"홍길동", "tel":123} )  #AA라는값삭제
# del addr_list[0]

print(addr_list)
for i, val in enumerate(addr_list):
    print(i, val)
    if val == "AA":
        del addr_list[i]
print(addr_list)
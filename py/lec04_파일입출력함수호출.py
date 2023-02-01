# 패키지     모듈              클래스     함수
# 폴더      .py               class     def
# venv      lec04            CalClass   add

# from 패키지 import 모듈명(*비추) 클래스명 함수명
# 1. from   : 패키지명.모듈명
# 2. import : 묘듈명, 클래스명, 함수명
# 3. 모듈명은 일반적으로 별칭(as)을 사용한다
# 4. import 함수명1, 함수명2이 길어지면 imort 모듈명으로 한다

#               ex) from 패키지명.모듈명   import 클래스명
#               ex) from 패키지명.모듈명   import 함수명1, 함수명2 ...
#               ex) from 패키지명         import 모듈명 as 별명

from lecture.py.lec04_파일입출력함수 import CalClass           # from 패키지명.모듈명 import 클래스명
from lecture.py.lec04_파일입출력함수 import MemberClass        # from 패키지명.모듈명 import 클래스명
from lecture.py.lec04_파일입출력함수 import myprint, uprint    # from 패키지명.모듈명 import 함수명, 함수명

s = CalClass.add(1, 5)
print(s)
MemberClass.add('Kim', 50)
myprint(1)
uprint(2)

# 비추천   import 뒤에는 클래스명이나 함수명이 바람직
from lecture.py import lec04_파일입출력함수 as mymy
mymy.uprint(4)
mymy.MemberClass.add('park', 10)
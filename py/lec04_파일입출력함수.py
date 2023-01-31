# 패키지     모듈              클래스     함수
# 폴더      .py               class     def
# venv      04파일입출력함수   CalClass   add

class CalClass:
    def add(n1, n2):
        res = n1 + n2
        return res

class MemberClass:
    def add(name, age):
        print(name, '저장')

def myprint(n):
    print(n, '입력되었습니다')

def uprint(n):
    print(n, '입력입력')

# -------------------------------------------------
# 함수에 return이 있는 경우 변수에 바인딩해 사용할 수 있음
# -------------------------------------------------

# s = CalClass.add(1, 5)
# print(s)
# MemberClass.add('Kim', 50)
# myprint(1)
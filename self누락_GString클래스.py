#전역변수
str = "Not Class Member"

#클래스를 정의
class GString:
    def __init__(self):
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 실수에 따른 버그 발생
        print(self.str)

#인스턴스 생성
g = GString()
g.set("First Message")
g.print()

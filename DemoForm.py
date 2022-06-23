# DemoForm.py
# DemoForm.ui(디자인) + DemoForm.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm.ui")[0] #ui tag이 하나가 아닌 경우가 있어서 슬라이싱을 하는 것

# 폼 클래스 정의
class DemoForm(QDialog, form_class):  #두개를 동시에 상속받음(다중상속)
    #생성자 매서드
    def __init__(self):
        super().__init__() #양쪽의 초기화매서드를 불러줌(2개의 부모)
        self.setupUi(self) 
        self.label.setText("첫번째 데모~~")

#진입점 체크
if __name__ == "__main__":
    #실행프로세스
    app = QApplication(sys.argv)
    #창을 실행
    demoWindow = DemoForm()
    demoWindow.show() 
    #이벤트 처리 대기
    app.exec_()


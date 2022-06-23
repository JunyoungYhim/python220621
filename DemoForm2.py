# DemoForm2.py
# DemoForm2.ui(디자인) + DemoForm2.py(로직)

import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

#웹 크롤링
import urllib.request
from bs4 import BeautifulSoup

# 디자인 파일 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0] #ui tag이 하나가 아닌 경우가 있어서 슬라이싱을 하는 것

# 폼 클래스 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):  #두개를 동시에 상속받음(다중상속)
    #생성자 매서드
    def __init__(self):
        super().__init__() #양쪽의 초기화매서드를 불러줌(2개의 부모)
        self.setupUi(self) 
    #슬롯 메서드 정의
    def firstClick(self):
        # web3.py에서 코드 가져오기
        f = open("c:\\work\\webtoon.txt","wt",encoding="utf-8")
        for i in range(1,6):
            url = "https://comic.naver.com/webtoon/list?titleId=20853&weekday=fri%20import%20urllib.request&page=" + \
                str(i)
            data = urllib.request.urlopen(url)
            soup = BeautifulSoup(data, "html.parser")
            cartoons = soup.find_all("td", class_="title")

            for item in cartoons:
                title = item.find("a").text
                print(title.strip())
                f.write(title.strip()+"\n")
        f.close()
        self.label.setText("네이버 웹툰 크롤링 종료")    
    def secondClick(self):
        self.label.setText("두번째 버튼클릭~~")           
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")   

#진입점 체크
if __name__ == "__main__":
    #실행프로세스
    app = QApplication(sys.argv)
    #창을 실행
    demoWindow = DemoForm()
    demoWindow.show() 
    #이벤트 처리 대기
    app.exec_()


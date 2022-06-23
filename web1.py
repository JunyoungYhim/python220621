# web1.py

# 웹크롤링을 위한 선언 (패키지명이 bs4, 모듈명이 BeautifulSoup)
from bs4 import BeautifulSoup

# 페이지 로딩
page = open("c:\\work\\test01.html", "rt", encoding = "utf-8").read()
# 검색이 용이한 객체
soup = BeautifulSoup(page, "html.parser")
# 문서를 그대로 보기
#print(soup.prettify())

# <p>태그 전체를 검색
#print(soup.find_all("p"))

# 첫번째 <p> 검색
#print(soup.find("p"))

# 조건이 있는 경우 : <p class = outer-text>
#print(soup.find_all("p", class_=  "outer-text")) #class뒤에 언더바가 들어가야함

# id속성으로 검색
#print(soup.find_all(id = "first"))

# 문자열만 리턴
for item in soup.find_all("p"):
    title = item.text #.text가 앞뒤의 태그를 삭제
    title = title.replace("\n","") # 줄바꿈 문자를 삭제
    print(title.strip()) #strip은 앞뒤 공백을 제거해줌


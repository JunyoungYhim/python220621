# DemoRE.py
import re

#print(dir(re))
result = re.search("[0-9]*th","35th")
print(result)
print(result.group())

result = re.match("[0-9]*th","35th")
print(result)
print(result.group())


result = re.search("[0-9]*th","  35th") #search는 빈칸을 포함해도 찾을 수 있으나
print(result)
print(result.group())

#다중라인 주석처리 : ctrl + /
# result = re.match("[0-9]*th","  35th") #match는 빈칸을 포함하는 경우 찾을 수 없음
# print(result)
# print(result.group())

#검색여부만 표시
print(bool(re.search("ap","this is apple")))
print(bool(re.match("ap","this is apple")))

# 연도를 가져오는 경우
result = re.search("\d{4}", "올해는 2022년입니다.") #연속으로 네자리 있는거를 가져오기
print(result.group())

#우편번호
result = re.search("\d{5}", "우리동네는 52300입니다.")
print(result.group())


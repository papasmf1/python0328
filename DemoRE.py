# DemoRE.py
import re 

#print(dir(re))

#서치는 처음부터 끝까지 검색
result = re.search("[0-9]*th", "  35th")
print(result)
#처음을 보고 바로 포기 
result = re.match("[0-9]*th", "  35th")
print(result)
#print(result.group())

print(bool(re.search("apple", "this is apple")))
print(bool(re.match("apple", "this is apple")))
print(bool(re.search("\d{4}", "올해는 2022년")))
print(bool(re.search("\d{5}", "우리동네는 51233")))



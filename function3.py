# function3.py 

#가변인자
def union(*ar):
    #지역변수를 리스트로 초기화
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출
#디버깅할 때 중단점(Break Point)
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))



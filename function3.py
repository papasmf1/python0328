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

#정의되지 않은 인자
def userURIBuilder(server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL += key + "=" + user[key] + "&"
    return strURL 

#호출
print(userURIBuilder("credu.com","80",id="kim", age="30"))
print(userURIBuilder("credu.com","80",id="kim", age="30",name="mike"))

#람다 함수(이름이 없다!)
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))

print((lambda x:x*x)(3))

print(globals())



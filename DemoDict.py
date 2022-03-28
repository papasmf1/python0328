# DemoDict.py 

#함수를 정의
def calc(a,b):
    return a+b, a*b 

#첫번째 컬럼 이동
result = calc(3,4)
#슬라이싱 사용 
print(result[0])
print(result[1])

#하나로 모아서 입력
args = (5,6)
print(calc(*args))

#타입캐스팅(형식변환):List, Tuple, Set 형식 변환 
a = set((1,2,3))
print(a)
print(type(a))
b = list(a)
print(b)
b.append(5)
print(b)

#딕셔너리(JSON: 자바스크립트의 객체 표기)
d = {"apple":"red", "kiwi":"green"}
print(len(d))
print(d["apple"])
d["banana"] = "yellow"
print(d)

device = {"아이폰":5, "아이패드":10, "윈도우":20}
#입력
device["맥"] = 15
print(device)
#수정
device["아이폰"] = 6
#삭제
del device["아이폰"]
print(device)

#참조를 복사
mydevice = device 

mydevice["에어팟"] = 10 

print(id(device))
print(id(mydevice))

print(device)



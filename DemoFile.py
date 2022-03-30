# DemoFile.py 

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("--약간 서식을 변경---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3))

#문자열 결합 연산
url = "http://www.credu.com/?page=" + str(1) 
print(url)

print("--서식문자--")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(10))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000000))





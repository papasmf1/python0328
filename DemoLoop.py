# DemoLoop.py 

print("---파이썬의 판단근거---")
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("데이터"))
print(bool([]))
print(bool([1,2,3]))

lst = [1,2,3,4,5,6,7,8,9,10]

for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))


print("---여기까지 실행하면 종료---")

for i in lst:
    # %는 나머지값을 구한다. ==(동일한지) !=(다른지) =(대입)
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))


#수열함수: range(start, end, step)
#인공지능(딥러닝), 데이터사이언스(통계)
#방통대(통계학과)
item = list(range(10))
print(item)
print(list(range(1,101)))
year = list(range(2000,2023))
print(year)

#리스트 컴프리헨션(리스트 내장)
#파이썬 개발자: 파이썬스럽다! 
lst = list(range(1,11))
result = [i**2 for i in lst if i > 5]
print(result)

#수동으로 for루프 사용
for i in range(5):
    print(i)

#반복문에서 필터링하는 함수
#스칼라(단일값) 리스트(배열)
lst = [20,25,30]

#필터링하는 함수 정의
def getBiggerThan20(i):
    return i>20

#파이썬은 무조건 참조가 복사되서 전달
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    #서식문자로 지정: {0}, {1}, {2} 포지션을 예약해서 변경
    print("item:{0}".format(item))

#람다 함수로 정의
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    #서식문자로 지정: {0}, {1}, {2} 포지션을 예약해서 변경
    print("item:{0}".format(item))


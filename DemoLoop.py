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



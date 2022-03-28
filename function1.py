#함수를 정의
def times(a,b):
    return a*b 

#함수를 호출
print(times(2,3))

#불변형식과 가변형식 
a = 1.2
print(id(a))

a = 2.3
print(id(a))

print("---가변형식---")
lst = [1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

#함수를 정의
def change(x):
    x[0] = "H"

#호출
wordlist = ["J","A","M"]
change(wordlist)
print("함수 호출후:", wordlist)

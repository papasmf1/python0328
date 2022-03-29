# class1.py 

#클래스:새로운 Type을 정의
class Person:
    #초기화(생성자 메서드)
    def __init__(self):
        #인스턴스 멤버 변수를 초기화(복사본)
        self.name = "default name"
    def print(self):
        print("내 이름은 {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person() 
p2.name = "전우치"

p1.print()
p2.print() 


    
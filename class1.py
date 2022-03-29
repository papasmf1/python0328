# class1.py 

#클래스:새로운 Type을 정의
class Person:
    #클래스 멤버 변수(static키워드 없이 위치를 가지고 구분)
    #주로 데이터를 공유
    num_person = 0 
    #초기화(생성자 메서드)
    def __init__(self):
        #인스턴스 멤버 변수를 초기화(복사본)
        self.name = "default name"
        Person.num_person += 1 
    def print(self):
        print("내 이름은 {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person() 
p3 = Person()

print("인스턴스 개수:{0}".format(Person.num_person))

    
# -*- 생성자와 소멸자 -*-
class MyClass:
    #생성자(초기화)
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    #소멸자(가장 마지막 정리, 청소)
    def __del__(self):
        print("Instance is deleted!")


#인스턴스 생성
my = MyClass(5)
#파이썬에서 가비지 컬렉션 서비스를 사용(자동 수거 서비스)
#del my 

print("전체 코드 실행 종료")

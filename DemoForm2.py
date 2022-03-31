# DemoForm2.ui(화면) + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹크롤링
import urllib.request 
from bs4 import BeautifulSoup 


#디자인 파일을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#클래스 정의(QMainWindow클래스 상속):다중상속은 C++, Python정도만 허용 
class DemoForm(QMainWindow, form_class):
    #초기화 메서드(self, this, super, base)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")
    #슬롯메서드정의
    def firstClick(self):
        f = open("c:\\work\\webtoon.txt", "a+", encoding="utf-8")
        data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
        soup = BeautifulSoup(data, 'html.parser')
        cartoons = soup.find_all('td', class_='title')
        for item in cartoons:
            title = item.find('a').text
            print(title)
            f.write(title + "\n")
        self.label.setText("네이버 웹툰 리스트 완료")    
        f.close() 
    def secondClick(self):
        self.label.setText("두번째 버튼~~")    
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")    

#인스턴스 생성
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec_() 


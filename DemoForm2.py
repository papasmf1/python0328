# DemoForm2.ui(화면) + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

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
        self.label.setText("첫번째 버튼")    
    def secondClick(self):
        self.label.setText("두번째 버튼~~")    
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭~~")    

#인스턴스 생성
app = QApplication(sys.argv)
demoWindow = DemoForm()
demoWindow.show()
app.exec_() 


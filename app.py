import sys 
from PyQt5 import QtWidgets
import design

class QtTwitter(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super(QtTwitter, self).__init__()
        self.setupUi(self)
        
        self.actionAbout_QtTwitter.triggered.connect(self.about_app)
        
    def about_app(self):
    	import about
    	modal = about.AboutApp()
    	modal.exec_()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = QtTwitter()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()

import sys
from PyQt5 import QtWidgets
import aboutapp

class AboutApp(QtWidgets.QDialog, aboutapp.Ui_Dialog):
    def __init__(self):
        super(AboutApp, self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.close)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AboutApp()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
        

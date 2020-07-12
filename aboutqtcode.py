import sys
from PyQt5 import QtWidgets
import aboutqt

class AboutQt(QtWidgets.QDialog, aboutqt.Ui_Dialog):
    def __init__(self):
        super(AboutQt, self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.close)
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = AboutQt()
    window.show()
    app.exec_()
    
if __name__ == "__main__":
    main()
        

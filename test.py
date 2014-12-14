#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

def hello():
    print("Hello, World!")

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QtGui.QPushButton('Button', self)
        btn.clicked.connect(hello)
        btn.setToolTip('Click for a greeting!')
        btn.resize(btn.sizeHint())
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('PyRSS')
        self.setWindowIcon(QtGui.QIcon('PyRSS_logo.png'))        
    
        self.show()

def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

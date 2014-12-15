#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

buttons = {}

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
layout = QtGui.QGridLayout()

def hello():
    print("Hello, World!")

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')

        for j in range(10):
            # keep a reference to the buttons
            #j, 1 is a kludge for not knowing horzn. formatting for Qt, yet:
            buttons[(j, 1)] = QtGui.QPushButton('Button %d' % j, self)
            buttons[(j, 1)].clicked.connect(hello)
            buttons[(j, 1)].setToolTip('Click for a greeting!')
            buttons[(j, 1)].resize(buttons[(j, 1)].sizeHint())
            # add to the layout
            layout.addWidget(buttons[(j, 1)], j, 1)

        
        widget.setGeometry(300, 300, 250, 15)
        widget.setWindowTitle('PyRSS')
        widget.setWindowIcon(QtGui.QIcon('logo.png'))        
    
        widget.show()

def main():
    widget.setLayout(layout)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

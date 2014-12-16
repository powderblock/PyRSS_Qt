#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import webbrowser
from PyQt4 import QtGui
import feedparser
import appdirs

appname = "PyRSS"
appauthor = "Adventurous"

# If the data directory doesn't exist, create it
datadir = appdirs.user_data_dir(appname, appauthor)
if (not os.path.isdir(datadir)):
    os.makedirs(datadir)
# Path for saved RSS site feeds
path = os.path.join(datadir, "sites.txt")

# Open sites.txt
try:
    with open(path, 'r') as f:
        # Get rid of all the newlines while you're reading it in
        text = [x.strip() for x in f.readlines()]
except:
    pass

buttons = {}
urls = []

app = QtGui.QApplication(sys.argv)
widget = QtGui.QWidget()
layout = QtGui.QGridLayout()

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()


    def initUI(self):

        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        
        self.setToolTip('This is a <b>QWidget</b> widget')
            # Go through each line in sites.txt
        for line in text:
            line = line.strip()
            # we don't want to process the same URL more than once
            if line in urls:
                continue

            urls.append(line)
            # Feed line found in file to feedparser
            site = feedparser.parse(line)
            print line

            num = min(3, len(site['entries']))
            # Top three entries from the RSS feed
            global buttonNum
            buttonNum = 0
            for entry in site['entries'][:num]:
                buttonNum += 1
                title = entry['title']
                link = entry['link']
                self.link = link
                # keep a reference to the buttons
                #1 is a kludge for not knowing horzn. formatting for Qt, yet:
                buttons[(buttonNum, 0)] = QtGui.QPushButton(title)
                #buttons[(buttonNum, 0)].clicked.connect(webbrowser.get().open(self.link))
                buttons[(buttonNum, 0)].setToolTip('Click to open story.')
                buttons[(buttonNum, 0)].resize(buttons[(buttonNum, 0)].sizeHint())
                # add to the layout
                layout.addWidget(buttons[(buttonNum, 0)], buttonNum, 0)
        
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

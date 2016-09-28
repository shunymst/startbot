#!/usr/bin/env python

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
import docomo

def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        #オウム返しゾーン------------
        self.inputLine = QLineEdit()
        self.outputLine = QLineEdit()
        self.outputLine.setReadOnly(True)

        self.calcButton = QPushButton("&会話")
        self.calcButton.clicked.connect(self.oumu)

        #docomo対話ゾーン------------
        self.inputLine2 = QLineEdit()
        self.outputLine2 = QLineEdit()
        self.outputLine2.setReadOnly(True)

        self.calcButton2 = QPushButton("&会話")
        self.calcButton2.clicked.connect(self.kaiwa)

        lineLayout = QGridLayout()
        lineLayout.addWidget(QLabel("----------オウム返し----------"), 0, 0)
        lineLayout.addWidget(QLabel("話したいこと"), 1, 0)
        lineLayout.addWidget(self.inputLine, 1, 1)
        lineLayout.addWidget(QLabel("お返事"), 2, 0)
        lineLayout.addWidget(self.outputLine, 2, 1)
        lineLayout.addWidget(QLabel("----------雑談----------"), 3, 0)
        lineLayout.addWidget(QLabel("話したいこと"), 4, 0)
        lineLayout.addWidget(self.inputLine2, 4, 1)
        lineLayout.addWidget(QLabel("お返事"), 5, 0)
        lineLayout.addWidget(self.outputLine2, 5, 1)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.calcButton)
        buttonLayout.addWidget(self.calcButton2)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(lineLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("会話")

    def oumu(self):
        n = self.inputLine.text()
        self.outputLine.setText(str(n))

    def kaiwa(self):
        n = self.inputLine2.text()
        #self.outputLine.setText(str(n))
        self.outputLine2.setText(docomo.kaiwa(str(n)))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())
#!/usr/bin/env python

from PyQt5.QtWidgets import (QApplication, QWidget,
                             QGridLayout, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QPushButton)
from PyQt5.QtGui import QPixmap, QIcon
import docomo
import json
import pprint

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # QPixmapオブジェクト作成
        pixmap = QPixmap("baby.png")
        # ラベルを作ってその中に画像を置く
        img = QLabel(self)
        img.setPixmap(pixmap)
        img.move(100, 100)

        # docomo対話ゾーン------------

        # 会話コンテキスト保持
        self.contextId = ""

        self.inputLine2 = QLineEdit()
        self.inputLine2.setFixedWidth(200)
        self.outputLine2 = QLabel()
        self.outputLine2.setFixedWidth(200)
        self.outputLine2.setText("おはなししてね")
        # self.outputLine2.setReadOnly(True)

        self.calcButton2 = QPushButton("&おはなし")
        self.calcButton2.clicked.connect(self.kaiwa)

        lineLayoutImg = QGridLayout()
        lineLayoutImg.addWidget(img, 0, 0)

        lineLayout = QGridLayout()
        lineLayout.addWidget(QLabel("はなしたいこと:"), 1, 0)
        lineLayout.addWidget(self.inputLine2, 1, 1)
        lineLayout.addWidget(QLabel("へんじ　　　　:"), 2, 0)
        lineLayout.addWidget(self.outputLine2, 2, 1)

        buttonLayout = QVBoxLayout()
        buttonLayout.addWidget(self.calcButton2)

        mainLayout = QHBoxLayout()
        mainLayout.addLayout(lineLayoutImg)
        mainLayout.addLayout(lineLayout)
        mainLayout.addLayout(buttonLayout)

        self.setLayout(mainLayout)
        self.setWindowTitle("おはなししよう")

    def oumu(self):
        n = self.inputLine.text()
        self.outputLine.setText(str(n))

    def kaiwa(self):
        n = self.inputLine2.text()
        # self.outputLine.setText(str(n))
        pprint.pprint(self.contextId)
        resjson = docomo.kaiwa(str(n), self.contextId)
        self.outputLine2.setText(resjson["utt"])
        self.contextId = resjson["context"]


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()
    sys.exit(app.exec_())

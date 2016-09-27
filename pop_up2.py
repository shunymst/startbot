#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication, QLineEdit)
from PyQt5.QtGui import QPixmap, QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        app = QApplication(sys.argv)

        window = QWidget()
        #  ボタンを作成
        button1 = QPushButton('1')
        button2 = QPushButton('2')
        button3 = QPushButton('3')

        # レイアウト作成
        layout = QHBoxLayout()
        # レイアウトにボタンを追加
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)

        # レイアウトをセット
        window.setLayout(layout)
        window.show()

    def onChanged(self, text):
        # ラベルに入力されたテキストを挿入
        self.lbl.setText(text)
        # 入力されたテキストによって、ラベルの長さを調整
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

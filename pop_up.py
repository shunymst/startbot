#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout,
                             QLabel, QApplication, QLineEdit)
from PyQt5.QtGui import QPixmap, QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        # ラベルオブジェクト作成
        self.lbl = QLabel(self)
        # QLineEditオブジェクト作成
        qle = QLineEdit(self)

        qle.move(230, 20)
        self.lbl.move(230, 50)

        # qleに文字が入力されたら、onChanged関数の呼び出し
        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 500, 480, 300)

        # QPixmapオブジェクト作成
        pixmap = QPixmap("sota.jpg")
        # ラベルを作ってその中に画像を置く
        lbl = QLabel(self)
        lbl.setPixmap(pixmap)
        lbl.move(100, 100)

        hbox.addWidget(lbl)
        self.setLayout(hbox)

        self.move(200, 200)
        self.setWindowTitle('Sota dayo!')
        # 画面左上のアイコンを設定
        self.setWindowIcon(QIcon('sota.jpg'))

        self.show()

    def onChanged(self, text):
        # ラベルに入力されたテキストを挿入
        self.lbl.setText(text)
        # 入力されたテキストによって、ラベルの長さを調整
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

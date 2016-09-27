#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QHBoxLayout, QVBoxLayout,
                             QLabel, QApplication, QLineEdit, QPushButton)
from PyQt5.QtGui import QPixmap, QIcon


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        # QPixmapオブジェクト作成
        pixmap = QPixmap("sota.jpg")
        # ラベルを作ってその中に画像を置く
        img = QLabel(self)
        img.setPixmap(pixmap)
        img.move(100, 100)

        # QLineEditオブジェクト作成
        txt = QLineEdit(self)
        # ボタン
        button = QPushButton("会話", self)
        # ラベルオブジェクト作成
        #ans = QLabel(self)
        ans = QLabel("ここに回答がでてきます")


        # スロットを設定
        button.clicked.connect(self.submit)

        # qleに文字が入力されたら、onChanged関数の呼び出し
        #txt.textChanged[str].connect(self.onChanged)

        #ウィジェット設定
        hbox.addWidget(img)

        #vbox = QVBoxLayout()
        #vbox.addWidget(txt)
        #vbox.addWidget(button)
        #hbox.addLayout(vbox)
        hbox.addWidget(txt)
        hbox.addWidget(button)
        #hbox.addWidget(ans)
        self.setLayout(hbox)

        self.move(200, 200)
        self.setWindowTitle('Sota dayo!')
        # 画面左上のアイコンを設定
        self.setWindowIcon(QIcon('sota.jpg'))

        self.show()

    def submit(self, text):
        # ラベルに入力されたテキストを挿入

        #hbox = QHBoxLayout(self)
        #hbox.removeWidget()

        self.ans.setText('hoge')
        #self.setWindowIcon(QIcon('sota2.jpg'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

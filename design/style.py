
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import * 


class style():
    def style_btn(text):
        btn= QPushButton(text)
        btn.setMinimumHeight(30)
        btn.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
        return btn
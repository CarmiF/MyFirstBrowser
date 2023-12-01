
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import * 

from .left_v_layout_build import *
from .right_v_layout_build import *

class MyWebBrowser(QMainWindow):


    def __init__(self, general, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)
        
        self.general = general

        self.current_tab_button = None
        self.window = QWidget()
        self.window.setWindowTitle("Your All in one ### browser")
        self.window.setStyleSheet("background-color: black;") 

        # self.browser.setUrl(QUrl("https://www.youtube.com/watch?v=Yh4CnDL44O8&t=0s"))
        self.right_v_layout =  right_v_layout_build(self)
        self.left_v_layout = left_v_layout_build(self)

        self.main_window =QHBoxLayout()

        self.main_window.addLayout(self.left_v_layout, stretch=10)
        self.main_window.addLayout(self.right_v_layout, stretch=90)

        self.window.setLayout(self.main_window)
        print("huoli")
        self.window.show()




from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import * 
from .right_v_layout_actions import *
 

def right_v_layout_build(self):
    right_horizontal_layout =QVBoxLayout()

    self.browser_stacked_window=browser_window_build(self)
    self.status_browser_bar = status_browser_bar_build(self.browser_stacked_window.browser)

    right_horizontal_layout.addLayout(self.status_browser_bar)
    right_horizontal_layout.addWidget(self.browser_stacked_window)
    return right_horizontal_layout

def browser_window_build(self):
    browser_stacked_window = QStackedWidget()
    browser_stacked_window.browser = QWebEngineView()
    self.general.browsers.append(browser_stacked_window.browser)
    browser_stacked_window.addWidget(browser_stacked_window.browser)
    browser_stacked_window.setCurrentIndex(0)

    return browser_stacked_window
      
def status_browser_bar_build(browser):    
    status_browser_bar=QHBoxLayout() 

    top_browser_bar_left=QHBoxLayout() 
    top_browser_bar_right=QHBoxLayout() 

    go_btn = style_btn("Go")
    go_btn.clicked.connect(lambda: navigate("https://www.example2.com"))
    back_btn=style_btn("back")
    back_btn.clicked.connect(browser.back)
    forward_btn =style_btn("forward")
    forward_btn.clicked.connect(browser.forward)
    hello_btn = style_btn("hello")
    hello_btn.clicked.connect(browser.forward)

    top_browser_bar_right.addWidget(go_btn)
    top_browser_bar_right.addWidget(back_btn)
    top_browser_bar_right.addWidget(forward_btn)
    top_browser_bar_left.addWidget(hello_btn)

    status_browser_bar.addLayout(top_browser_bar_left, stretch=80, )

    status_browser_bar.addLayout(top_browser_bar_right, stretch=20)
    
    return status_browser_bar

def style_btn(text):
        btn= QPushButton(text)
        btn.setMinimumHeight(30)
        btn.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
        return btn

if __name__ == '__main__':

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Your All in one ### browser")
    window.setStyleSheet("background-color: black;") 
    # window.setLayout(build_right_h_layout())
    window.show()
    app.exec_()
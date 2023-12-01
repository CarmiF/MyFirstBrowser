
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import * 
from .right_v_layout_actions import *

def add_btn_with_url(left_h_layout):
        new_label = QPushButton("New Label")
        new_label.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
        left_h_layout.addWidget(new_label)
        left_h_layout.update()

def create_new_tab(self): 
    print("create tab")
    
    new_tab = QPushButton(self.sender().text())
    new_tab.setStyleSheet("color: white; background-color: black; border: 1px solid black;")
    new_tab.url= self.sender().url
    new_tab.clicked.connect(lambda: show_tab(self, self.sender(), False))
    self.status_browser_bar.addWidget(new_tab)
    self.general.all_open_tabs.append(new_tab)

    browser = QWebEngineView()
    browser.url = self.sender().url
    browser.setUrl(QUrl(self.sender().url))
    self.general.browsers.append(browser)
    self.browser_stacked_window.addWidget(browser)
    show_tab(self, new_tab, True)

def check_if_tab_exists(self):
    for item in self.general.all_open_tabs:
        if self.sender().url == item.url:
            print(self.sender().url)
            print("tab exists")
            return item
    print("tab is not exists")
    return False
    
def btn_with_url_clicked(self):
    tab = check_if_tab_exists(self)
    if tab == False:
        create_new_tab(self)
    else:
        show_tab(self, tab, True)

def style_btn(text):
    btn= QPushButton(text)
    btn.setMinimumHeight(30)
    btn.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
    return btn
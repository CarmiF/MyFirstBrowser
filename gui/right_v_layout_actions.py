

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import * 
 
def show_tab(self, tab, refresh):
    update_new_tab_btn_style(self, tab)
    update_browser_widget(self, tab, refresh)


def update_browser_widget(self, tab, refresh):  
    print("update_browser")  
    for index, item in enumerate(self.general.browsers):
        if item.url == tab.url:
            print(item.url)  
            print("browser num:"+str(index))
            print("the length of the browser list is"+ str(len(self.general.browsers) ))
            print("refresh:"+str(refresh))

            if refresh:
                navigate(self, tab.url)

            else:
                self.browser_stacked_window.setCurrentIndex(index)
                self.general.current_browser = item
            
            self.current_browser = item

            break
    
      
def check_tab_open(self):
        
        for index, item in enumerate(self.all_open_tabs):
            if self.sender().url == item.url:
                print("exists")
                self.update_selected_tab(item)

                self.stacked_widget.setCurrentWidget(self.all_open_browsers[index])
                self.current_url=item.url
                self.current_browser=self.all_open_browsers[index]


                return True
        return False

def update_new_tab_btn_style(self, new_tab):
    new_tab.setStyleSheet("color: white; background-color: black; border: 1px solid black;")
    if self.general.current_tab_btn is None:
        print("none")
    else:
        self.general.current_tab_btn.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
    self.general.current_tab_btn = new_tab

def add_Url_Btn(self):
        new_label = QPushButton("New Label")
        new_label.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
        self.side_bar.addWidget(new_label)
        self.side_bar.update()

def navigate(self, url):
    if not url.startswith("http"):
        url="http://"+ url 
        self.url_bar.setText(url)

    self.browser_stacked_window.browser.setUrl(QUrl(url))
    self.general.current_browser= self.browser_stacked_window.browser
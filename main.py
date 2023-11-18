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

class MyWebBrowser(QMainWindow):

    def update_selected_tab(self, new_tab_btn):
        if self.current_tab_button is not None:
            self.current_tab_button.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
            print("previos")
        if new_tab_btn is not None:
            new_tab_btn.setStyleSheet("color: white; background-color: black; border: 1px solid black;")
            print("current")
        self.current_tab_button = new_tab_btn

    def navigate(self, url):
            if not url.startswith("http"):
                url="http://"+ url 
                self.url_bar.setText(url)

            self.browser.setUrl(QUrl(url))


    def build_top_browser_bar(self):

        self.tabs = []
        self.top_browser_bar=QHBoxLayout() 

        self.top_browser_bar_left=QHBoxLayout() 
        self.top_browser_bar_right=QHBoxLayout() 

        self.go_btn = style.style_btn("Go")
        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))

        self.back_btn=style.style_btn("back")
        self.back_btn.clicked.connect(self.browser.back)

        self.forward_btn =style.style_btn("forward")
        self.forward_btn.clicked.connect(self.browser.forward)

        self.hello_btn = style.style_btn("hello")
        self.hello_btn.clicked.connect(self.browser.forward)

        self.top_browser_bar_right.addWidget(self.go_btn)
        self.top_browser_bar_right.addWidget(self.back_btn)
        self.top_browser_bar_right.addWidget(self.forward_btn)

        self.top_browser_bar_left.addWidget(self.hello_btn)

        self.top_browser_bar.addLayout(self.top_browser_bar_left, stretch=80, )

        self.top_browser_bar.addLayout(self.top_browser_bar_right, stretch=20)

    def build_side_bar(self):
        
        self.side_bar=QVBoxLayout() 
        
        self.top_side_bar=QHBoxLayout()

        self.add_url_btn= style.style_btn("+")
        self.add_url_btn.clicked.connect(self.add_Url_Btn)


        self.explorer_label =QLabel("Explorer")
        self.explorer_label.setMinimumHeight(30)
        self.explorer_label.setStyleSheet("color: white; background-color: black;border: 1px solid darkblue;")

        self.top_side_bar.addWidget(self.add_url_btn, stretch=20)
        self.top_side_bar.addWidget(self.explorer_label, stretch=80)

        self.url_bar=QTextEdit()
        self.url_bar.setMaximumHeight(30)
        self.url_bar.setStyleSheet("color: white; background-color: black;border: 1px solid darkblue;")

        self.url_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        # self.btn= style.style_btn("bing")
        # self.btn.url= "https://www.bing.com/search?form=MY0291&OCID=MY0291&q=Bing+AI&showconv=0"
        # self.btn.clicked.connect(self.create_new_tab)
        
        self.side_bar.addLayout(self.top_side_bar)
        self.side_bar.addWidget(self.url_bar)
        
        with open('AIsites.txt', 'r') as file:
            for line in file:
                parts = line.strip().split(' ')
                if len(parts) == 2:
                    name, url = parts
                    self.btn = style.style_btn(name)
                    self.btn.url=url
                    self.btn.clicked.connect(self.create_new_tab)
                    self.side_bar.addWidget(self.btn)
        # self.side_bar.addWidget(self.btn)
        
        self.side_bar.setAlignment(Qt.AlignTop)
        self.side_bar.setSpacing(0)


    def add_Url_Btn(self):
        new_label = QPushButton("New Label")
        new_label.setStyleSheet("color: white; background-color: black; border: 1px solid darkblue;")
        self.side_bar.addWidget(new_label)
        self.side_bar.update()

    def create_new_tab(self):

        tab_exist=False
        for item in self.all_open_tabs:
            if self.sender().url == item.url:
                print("exists")
                self.update_selected_tab(item)
                tab_exist=True

        if tab_exist==False:
            new_tab = QPushButton(self.sender().text())
            new_tab.setStyleSheet("color: white; background-color: black; border: 1px solid black;")
            new_tab.url= self.sender().url
            new_tab.tab=True
            new_tab.clicked.connect(self.tab_clicked)
            
            self.all_open_tabs.append(new_tab)

            self.update_selected_tab(new_tab)
            self.top_browser_bar_left.addWidget(self.all_open_tabs[-1])
            self.top_browser_bar_left.update()

        
        self.navigate(self.sender().url)

        
    def tab_clicked(self):
    
        sender_button = self.sender()
        self.navigate(sender_button.url)
        self.update_selected_tab(sender_button)

    
    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.all_open_tabs=[]

        self.current_tab_button = None
        self.window = QWidget()
        self.window.setWindowTitle("Your All in one ### browser")
        self.window.setStyleSheet("background-color: black;") 

        self.browser_layout =QVBoxLayout()

        self.browser = QWebEngineView()
        self.build_top_browser_bar()

        self.browser_layout.addLayout(self.top_browser_bar)
        self.browser_layout.addWidget(self.browser)

        # self.browser.setUrl(QUrl("https://www.youtube.com/watch?v=Yh4CnDL44O8&t=0s"))


        self.build_side_bar()

        self.general_layout =QHBoxLayout()

        self.general_layout.addLayout(self.side_bar, stretch=10)
        self.general_layout.addLayout(self.browser_layout, stretch=90)

        self.setStyleSheet("background-color: lightblue;")

        self.window.setLayout(self.general_layout)
        self.window.show()

        

app = QApplication([])
window = MyWebBrowser()
app.exec_()








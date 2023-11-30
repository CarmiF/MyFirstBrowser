
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import * 
from .left_v_layout_actions import *
 

def top_part_build(left_h_layout):
    top_part=QHBoxLayout()
    add_url_tosidebar= style_btn("+")
    add_url_tosidebar.clicked.connect(lambda: add_btn_with_url(left_h_layout))

    explorer_label =QLabel("Explorer")
    explorer_label.setMinimumHeight(30)
    explorer_label.setStyleSheet("color: white; background-color: black;border: 1px solid darkblue;")

    top_part.addWidget(add_url_tosidebar, stretch=20)
    top_part.addWidget(explorer_label, stretch=80)

    return top_part


def url_part_build():
    url_bar=QTextEdit()
    url_bar.setMaximumHeight(30)
    url_bar.setStyleSheet("color: white; background-color: black;border: 1px solid darkblue;")
    url_bar.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
    return url_bar

def buttom_part(self):
    buttom_part = QVBoxLayout()
    for name, url in self.general.url_dict.items():
        btn = style_btn(name)
        print(name)

        btn.url= url
        print(btn.url)
        btn.clicked.connect(lambda: btn_with_url_clicked(self))
        buttom_part.addWidget(btn)
    
    return buttom_part



def left_v_layout_build(self):
    left_v_layout=QVBoxLayout() 

    left_v_layout.addLayout(top_part_build(left_v_layout))
    left_v_layout.addWidget(url_part_build())
    left_v_layout.addLayout(buttom_part(self))

    

    # self.btn= style.style_btn("bing")
    # self.btn.url= "https://www.bing.com/search?form=MY0291&OCID=MY0291&q=Bing+AI&showconv=0"
    # self.btn.clicked.connect(self.create_new_tab)
    
    left_v_layout.setAlignment(Qt.AlignTop)
    left_v_layout.setSpacing(0)

    return left_v_layout



if __name__ == '__main__':

    app = QApplication([])
    window = QWidget()
    window.setWindowTitle("Your All in one ### browser")
    window.setStyleSheet("background-color: black;") 
    window.setLayout(left_v_layout_build())
    window.show()
    app.exec_()

    
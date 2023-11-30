

from design.style import *
from gui.main_page import MyWebBrowser

class General():
    def __init__(self):
        
        self.all_open_tabs=[]
        self.current_tab_btn=None
        
        
        self.path_to_url_file= 'AIsites.txt'
        self.url_dict = create_url_dictionary(self.path_to_url_file)
        self.browsers = []
        self.current_browser = None
        

        
    
def create_url_dictionary(path_to_url_file):
    url_dict = {}
    with open(path_to_url_file, 'r') as file:            
            for line in file:
                parts = line.split(' ')
                if len(parts) >= 2:
                    name, url = parts[0], ' '.join(parts[1:])
                    url_dict[name] = url
    return url_dict
                    





if __name__ == '__main__':
    
    general = General()
    app = QApplication([])
    window = MyWebBrowser(general)
    app.exec_()

    

    
    

    

    
                
    
    
        
    
          







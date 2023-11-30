def navigate_to_new_url(self, url):
            if not url.startswith("http"):
                url="http://"+ url 
                self.url_bar.setText(url)

            self.current_browser.setUrl(QUrl(url))

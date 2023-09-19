from selenium import webdriver
class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(30)
        self.wd.set_window_size(800, 600)
    def destroy (self):
        self.wd.quit()
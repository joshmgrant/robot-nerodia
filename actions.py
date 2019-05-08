from nerodia.browser import Browser
from robot.api.deco import keyword

BASE_TEST_URL = 'http://localhost:9292/'

class LoginPage():

    def __init__(self):
        self.browser = object()

    @keyword
    def open_browser(self, name='firefox'):
        self.browser = Browser(browser=name)
        return self.browser

    @keyword
    def go_to_login(self):
        self.browser.goto(BASE_TEST_URL + "login")

    @keyword
    def login_as(self, username, password):
        self.browser.input(id='username').send_keys(username)
        self.browser.input(id='password').send_keys(password)
        self.browser.button(class_name='radius').click()

    @keyword
    def close_browser(self):
        self.browser.quit()

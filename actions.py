from nerodia.browser import Browser
from robot.api.deco import keyword

BASE_TEST_URL = 'http://the-internet.herokuapp.com/'

class Login():

    def __init__(self):
        self.browser = {}

    @keyword
    def open_browser(self, name='chrome'):
        self.browser = Browser(browser=name)

    @keyword
    def go_to_login(self):
        self.browser.goto(BASE_TEST_URL + "login")

    @keyword
    def login_as(self, username, password):
        self.browser.input(id='username').send_keys(username)
        self.browser.input(id='password').send_keys(password)
        self.browser.button(class_name='radius').click()

    @keyword
    def is_error_message_visible(self):
        assert self.browser.element(class_name='error').present

    @keyword
    def is_login_successful(self):
        assert self.browser.element(class_name='success').present

    @keyword
    def close_browser(self):
        self.browser.quit()

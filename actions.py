from nerodia.browser import Browser

BASE_TEST_URL = 'http:/localhost:9292/'

def open_browser(name='firefox'):
    browser = Browser(browser=name)
    return browser

def go_to_login(browser):
    browser.goto(BASE_TEST_URL + "login")

def login_as(browser, username, password):
    browser.input(id='username').send_keys(username)
    browser.input(id='password').send_keys(password)
    browser.button(class_name='radius').click()

def close_browser(browser):
    browser.quit()

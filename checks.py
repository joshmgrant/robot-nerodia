from nerodia.browser import Browser

def should_be_displayed(browser, css):
    return browser.element(css_selector=css).present

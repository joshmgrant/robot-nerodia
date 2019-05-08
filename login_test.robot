*** Settings ***
Library  actions.py
Library  actions.Login

Test Setup    Open Browser
Test Teardown    Close Browser

*** Test Cases ***

Valid Login with Standard User

	Go To Login
	Login As    tomsmith    SuperSecretPassword!
	Is Login Successful

Invalid Login with Unknown User

	Go To Login
	Login As    bad    also_bad
	Is Error Message Visible

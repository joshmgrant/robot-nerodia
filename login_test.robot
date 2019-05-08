*** Settings ***
Library  actions.py
Library  checks.py

*** Test Cases ***

Valid Login with Standard User

        Open Browser
	Go To Login 
	Login As    tomsmith    SuperSecretPassword!
	Should Be Displayed    .success
        Close Browser

# Invalid Login with Unknown User

#         ${browser}    Open Browser   chrome
# 	Go To Login    ${browser}
# 	Login As    ${browser}    bad    also_bad
# 	Should Be Displayed     ${browser}    .error
#         Close Browser    ${browser}

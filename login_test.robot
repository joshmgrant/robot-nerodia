*** Settings ***
Library  actions.py
Library  checks.py

*** Test Cases ***

Valid Login with Standard User

        ${browser}    Open Browser   chrome
	Go To Login    ${browser}
	Login As    ${browser}    tomsmith    SuperSecretPassword!
	Should Be Displayed     ${browser}    .success
        Close Browser    ${browser}

Invalid Login with Unknown User

        ${browser}    Open Browser   chrome
	Go To Login    ${browser}
	Login As    ${browser}    bad    also_bad
	Should Be Displayed     ${browser}    .error
        Close Browser    ${browser}

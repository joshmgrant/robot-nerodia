*** Settings ***
Library  actions.py


*** Test Cases ***

Valid Login with Standard User

        ${browser}    Open Browser   firefox
	Go To Login    ${browser}
	Login As    ${browser}    tomsmith    SuperSecretPassword!
        Close Browser    ${browser}
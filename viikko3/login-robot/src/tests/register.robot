*** Settings ***
Library  ../AppLibrary.py
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Create User With Credentials  kalle  kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User With Credentials  kalle  kalle123
    Create User With Credentials  kalle  someotherpassw0rd
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Create User With Credentials  ka  kalle123
    Output Should Contain  Username too short or contains invalid characters

Register With Valid Username And Too Short Password
    Create User With Credentials  kalle  k4ll3
    Output Should Contain  Password must be at least 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Create User With Credentials  kalle  thisisalongpasswordconsistingoflettersonly
    Output Should Contain  Password must contain non-alphabetical character

*** Keywords ***
Create User With Credentials
    [Arguments]  ${username}  ${password}
    Input New Command
    Input Credentials  ${username}  ${password}
    Run Application

*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ville
    Set Password  ville123
    Set Confirmation Password  ville123
    Submit Registration
    Registration Should Succeed

Login After Successful Registration
    Go To Login Page
    Set Username  ville
    Set Password  ville123
    Submit Credentials
    Login Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ka
    Set Password  kalle123
    Set Confirmation Password  kalle123
    Submit Registration
    Registration Should Fail With Message  Username too short or contains invalid characters

Login After Failed Registration
    Go To Login Page
    Set Username  ka
    Set Password  kalle123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  kalle
    Set Password  lyhy7
    Set Confirmation Password  lyhy7
    Submit Registration
    Registration Should Fail With Message  Password must be at least 8 characters long

Register With Nonmatching Password And Password Confirmation
    Set Username  kalle
    Set Password  kalle123
    Set Confirmation Password  kalle132
    Submit Registration
    Registration Should Fail With Message  Given passwords do not match

*** Keywords ***
Go To Register Page
    Go To  ${REGISTER URL}

Set Confirmation Password
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Submit Registration
    Click Button  Register

Registration Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

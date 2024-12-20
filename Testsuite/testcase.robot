*** Settings ***
Resource    ../Resources/keywork.robot

*** Test Cases ***
Login 
    [Template]    Login To Website
    $data
    
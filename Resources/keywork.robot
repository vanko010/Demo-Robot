*** Settings ***
Library    ../Library/cus_lib.py
Library    JSONLibrary

*** Variables ***
${file_path}    ../Resources/data.json
*** Keywords ***
Open Browser
    [Arguments]    ${url}
    Get Url    ${url}

Login To Website
    [Arguments]    ${data}
    ${dataFile}=    Load JSON Data    ${file_path}
    FOR    ${data}    IN    @{dataFile}
        Log    Running test: ${data['url']}
        Get Url    ${data['url']}
        Sleep    3
        Login    ${data['username']}    ${data['password']}    ${data['xuser']}    ${data['xpass']}    ${data['xlogin']}
        Sleep    3
        Run Keyword And Continue On Failure    Verify URL        ${data['expected_url']}
        Clear Session
    END
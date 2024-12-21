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
    [Arguments]    ${case}
    ${dataFile}=    Load JSON Data    ${file_path}
    FOR    ${case}    IN    @{dataFile['Login']}
        Log    Running test: ${case['name']}
        Log    Description: ${case['description']}
        Get Url    ${case['data']['url']}
        Sleep    3
        Login    ${case['data']['username']}    ${case['data']['password']}    ${case['data']['xuser']}    ${case['data']['xpass']}    ${case['data']['xlogin']}
        Sleep    3
        Run Keyword And Continue On Failure    Verify URL        ${case['data']['expected_url']}
        Clear Session
    END
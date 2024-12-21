*** Settings ***
Resource    ../Resources/keywork.robot
Library    Dialogs

*** Variables ***
${file_path}    ../Resources/data.json

*** Test Cases ***
Check Header
    ${dataFile}=    Load JSON Data    ${file_path}
    FOR    ${data}    IN    @{dataFile['Header-PA']}
    Log    Running Test: ${data['name']}
    Log    Description: ${data['description']}
    Open Browser    ${data['data']['url']}
    ${check}=    Check Element is Displayed    //img[@title='Year-end deal']
    Log    Check Value ${check}
    IF    ${check} == True
            Click    //button[@id='close_slide']
    END
    Click Element    ${data['data']['locator_menu']}    ${data['data']['locator_item']}    ${data['data']['expected_url']}
    END


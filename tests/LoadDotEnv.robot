*** Settings ***
Resource    ../base.resource

*** Test Cases ***
Load Dot Env

    Log To Console    URL: %{url=${None}}
    Log To Console    USER: %{user=${None}}
    Log To Console    PASSWORD: %{password=${None}}
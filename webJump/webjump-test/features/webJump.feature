#encoding: utf-8
Feature: Disponibilizar cenarios para testes para futuros analistas de qualidade
    Como um potencial qa
    Gostaria de ter um site que disponibilizade botoes para automacao
    Para que consiga fazer a automacao e entregar um teste com qualidade

Scenario: Buttons in Buttons
Given I access webjump url
When I click in buttons in Buttons
Then I dont should see buttons in session Buttons 

Scenario: Buttons in IFRAME Buttons
Given I access webjump url
When I click in buttons in Iframe Buttons
Then I dont should see buttons in session Iframe

Scenario: Validate field and image WebDriver
Given I access webjump url
When I field and click buttons
Then I should see Selenium Webdriver logo
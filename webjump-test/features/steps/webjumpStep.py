# -*- coding: utf-8 -*-
import time
import unittest

"""Função que realiza o acesso na url base, seguida da tela respectiva"""

@given(u'I access webjump url')
def access_calculator_url(context):
    context.browser.visit('/testqa/')

"""Metódo de click nos botoes localizados na area Buttons"""

@when(u'I click in buttons in Buttons')
def click_buttons_in_buttonssession(context):
    context.webjumppage.click_buttons_on_session()
"""Metódo que verifica se os botões One, Three e Four estão visiveis"""

@then(u'I dont should see buttons in session Buttons')
def verify_elements_visable(context):
    assert (False == context.webjumppage.verify_elements_visable())

@when(u'I click in buttons in Iframe Buttons')
def click_buttons_in_iframesession(context):
	context.webjumppage.click_buttons_on_iframe()

@then(u'I dont should see buttons in session Iframe')
def verify_elements_visable_iframe(context):
	assert (False == context.webjumppage.verify_elements_visable_iframe())

@when(u'I field and click buttons')
def field_and_check_buttons(context):
	context.webjumppage.field_values("Joaozinho Teste")

@then(u'I should see Selenium Webdriver logo')
def verify_logo_webdriver(context):
	assert (True == context.webjumppage.verify_logo_webdriver())

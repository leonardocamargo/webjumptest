# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


"""Classe criada para armazenar todos os elementos que são utilizados da pagina"""

class WebJumpLocators(object):
	ONE_BUTTON = (By.ID,'btn_one')
	TWO_BUTTON = (By.ID,'btn_two')
	FOUR_BUTTON = (By.ID, 'btn_link')
	ONE_BUTTON_IFRAME = (By.CSS_SELECTOR, '.col-sm-12 #btn_one')
	TWO_BUTTON_IFRAME = (By.CSS_SELECTOR,'.col-sm-12 #btn_two')
	FOUR_BUTTON_IFRAME = (By.CSS_SELECTOR, '.col-sm-12 #btn_link')
	IFRAME = (By.XPATH, '//*[@id="iframe_panel_body"]/iframe')
	YOUR_FIRST_NAME = (By.ID, 'first_name')
	CHECK_OPTION_THREE = (By.ID, 'opt_three')
	WEBDRIVER_LOGO = (By.CSS_SELECTOR,'#panel_body_three > img:nth-child(4)')


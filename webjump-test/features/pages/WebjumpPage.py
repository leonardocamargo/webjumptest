# -*- coding: utf-8 -*-
from browser import Browser
from selenium import webdriver
from pages.locators import *
import select
from selenium.webdriver.support.select import Select
import time


"""Classe que tem como intuito realizar todas as operações pertinente ao mapeamento e execução de cenarios
Os metódos estão definidos de acordo com as operações que foram descritas no cenário"""


class WebJumpPage(Browser):
    

    """Função click na sessao Buttons"""
    def click_buttons_on_session(self):
        self.get_button_one().click()
        self.get_button_two().click()
        self.get_button_four().click()

    def click_buttons_on_iframe(self):
        self.get_button_one_iframe().click()
        self.get_button_two_iframe().click()
        self.get_button_four_iframe().click()
    
    def get_button_one_iframe(self):
        self.switch_to(*WebJumpLocators.IFRAME)
        return self.find_element(*WebJumpLocators.ONE_BUTTON_IFRAME)

    def get_button_two_iframe(self):
        return self.find_element(*WebJumpLocators.TWO_BUTTON_IFRAME)

    def get_button_four_iframe(self):
        return self.find_element(*WebJumpLocators.FOUR_BUTTON_IFRAME) 

    def get_button_one(self):
        return self.find_element(*WebJumpLocators.ONE_BUTTON)

    def get_button_two(self):
        return self.find_element(*WebJumpLocators.TWO_BUTTON)

    def get_button_four(self):
        return self.find_element(*WebJumpLocators.FOUR_BUTTON)

    def get_field_firstname(self):
        return self.find_element(*WebJumpLocators.YOUR_FIRST_NAME)

    def get_check_optionthree(self):
        return self.find_element(*WebJumpLocators.CHECK_OPTION_THREE)

    def field_values(self,name):
        self.get_field_firstname().send_keys(name)
        self.get_button_one().click()
        self.get_check_optionthree().click()


    """Foi tentada a funcao is_displayed e em js para validar o display:none mas não obtive êxito"""
    def verify_elements_visable(self):
        if (self.find_element(*WebJumpLocators.ONE_BUTTON).is_selected() and self.find_element(*WebJumpLocators.TWO_BUTTON).is_selected() and self.find_element(*WebJumpLocators.FOUR_BUTTON).is_selected()):
            return True
        return False

    def verify_elements_visable_iframe(self):
        if (self.find_element(*WebJumpLocators.ONE_BUTTON_IFRAME).is_selected() and self.find_element(*WebJumpLocators.TWO_BUTTON_IFRAME).is_selected() and self.find_element(*WebJumpLocators.FOUR_BUTTON_IFRAME).is_selected()):
            return True
        return False

    def verify_logo_webdriver(self):
        return self.find_element(*WebJumpLocators.WEBDRIVER_LOGO).is_displayed()
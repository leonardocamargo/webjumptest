# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

"""Classe utilizada para instanciar o webdriver e também definir metodos que são
utilizados, busca de elementos, fechar a instancia do browser
"""
class Browser(object):

    chrome_options = Options()   
    chrome_options.add_argument("--headless")

    base_url = 'https://webjump-user.github.io'

    # driver = webdriver.Chrome(chrome_options=chrome_options)
    driver = webdriver.Chrome()

    def close(self):
        """fechar instancia criada pelo webdriver"""
        self.driver.quit()

    def visit(self, location=''):
        url = self.base_url + location
        self.driver.get(url)
        delay = 3 # segundos
        try:
            myElem = WebDriverWait(self.driver, delay).until(EC.presence_of_element_located((By.ID, 'col_title')))
            print ("Page is ready!")
        except TimeoutException:
            print ("Scenario Exiting")
            self.close()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def switch_to(self, *locator):
        return self.driver.switch_to.frame(self.find_element(*locator))

    def switch_todefault(self):
        return self.driver.switch_to.default_content() 
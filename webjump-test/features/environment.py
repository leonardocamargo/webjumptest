 # -*- coding: utf-8 -*-
from browser import Browser
from selenium import webdriver
import http.server
import socketserver
import threading
from pages.WebjumpPage import WebJumpPage


"""Utilizado para realizar todas as funções antes de começar os testes"""

def before_all(context):
  # inicializa browser
  context.browser = Browser()
  context.webjumppage = WebJumpPage()


"""Utilizado para realizar funções após a execução dos testes"""

def after_all(context):
  context.browser.close()

# -*- coding: utf_8 -*-
__author__ = 'lyh'
__date__ = '2018/1/10 17:31'

from selenium import webdriver
from time import sleep


def execute_script():
    browser = webdriver.Chrome()
    browser.get('https://www.oschina.net/blog')
    for i in range(200):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;')
        sleep(1)
    browser.quit()

execute_script()
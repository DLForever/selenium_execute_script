# -*- coding: utf_8 -*-
__author__ = 'lyh'
__date__ = '2018/1/10 17:31'

from selenium import webdriver
from time import sleep


def execute_script():
    chrome_opt = webdriver.ChromeOptions()
    #无图浏览
    prefs = {'profile.managed_default_content_settings.images': 2}
    chrome_opt.add_experimental_option('prefs', prefs)
    browser = webdriver.Chrome(chrome_options=chrome_opt)
    browser.get('https://www.oschina.net/blog')
    for i in range(200):
        #屏幕下拉
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;')
        sleep(1)
    browser.quit()

execute_script()

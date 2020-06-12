import os
from selenium import webdriver

def initialize_Chrome_WebDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--incognito")
    return webdriver.Chrome('chrome_driver/chromedriver_win32.exe', options = options)

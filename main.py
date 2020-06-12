#
from src.initialize import *
from src.speed_test import Test_Beater

webdriver = initialize_Chrome_WebDriver()

beater = Test()
beater.start_test(webdriver)

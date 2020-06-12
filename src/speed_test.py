#
import time
from selenium.common.exceptions import *
from selenium.webdriver.common.keys import Keys

class Test():
    def __init__(self):
        self.base_url = 'https://www.livechat.com/typing-speed-test/#/'

    def start_test(self, browser):
        browser.get(self.base_url)
        try:
            time.sleep(2)
            input_writer = browser.find_element_by_id('test-input')
            input_writer.clear()
            base = browser.find_element_by_id('app')

            t_end = time.time() + 59
            while time.time() < t_end:
                next_text = base.find_element_by_xpath("./div[@class='app']/div[2]/div/span/div[2]/span/div/div[2]/div/span[1]").text
                print(next_text)
                input_writer.send_keys(next_text)
                input_writer.send_keys(Keys.SPACE)

        except NoSuchElementException as e:
            print(e)

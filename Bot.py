from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
import time
import random
import json

class Bot:

    def __init__(self, proxy_adress, creditentials_file):
        self.proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': proxy_adress,
            'ftpProxy': proxy_adress,
            'sslProxy': proxy_adress,
            'noProxy': ''
        })
        self.driver = webdriver.Firefox(proxy=self.proxy)
        creds = json.loads( open(creditentials_file).read() )
        self.connect(creds['username'], creds['password'])

    def connect(self, username, password):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        self.driver.find_element_by_css_selector('[name="username"]').send_keys(username)
        self.driver.find_element_by_css_selector('[name="password"]').send_keys(password)
        self.driver.find_element_by_xpath('//div[contains(text(),"Log In")]').click()
        time.sleep(2)

    def browse_hashtag(self, hashtag):
        self.driver.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
        time.sleep(2)
        i = 0
        for el in self.driver.find_elements_by_css_selector('.v1Nh3'):
            i += 1
            el.click()
            time.sleep(1)
            self.driver.find_element_by_css_selector('.dCJp8').click()
            time.sleep(.5)
            el = self.driver.find_element_by_css_selector('.oW_lN')
            self.driver.execute_script("arguments[0].click();", el)
            try:
                self.driver.find_element_by_xpath('//button[contains(text(),"Cancel")]').click()
            except:
                pass
            time.sleep(2)
            self.driver.find_element_by_css_selector('.ckWGn').click()
            time.sleep(1 + random.random() * 5)
            if (i > 9):
                return 0

    def browse_suggested(self):
        self.driver.get("https://www.instagram.com/explore/people/suggested/")
        time.sleep(2)
        for i in range(5):
            for el in self.driver.find_elements_by_css_selector("._0mzm-"):
                self.driver.execute_script("arguments[0].click();", el)
                time.sleep(.5 + random.random() * 0.5)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(3)

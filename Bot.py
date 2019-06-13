from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium import webdriver
import datetime
import time
import random
import json
import os

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
        self.creds = json.loads( open(creditentials_file).read() )
        self.connect(self.creds['username'], self.creds['password'])

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
        last_index = 0
        while (i < 130):
            for l, el in enumerate(self.driver.find_elements_by_css_selector('.v1Nh3')):
                if (l < last_index):
                    break
                last_index+=1
                el.click()
                time.sleep(.5)
                try:
                    self.driver.find_element_by_css_selector('[aria-label="Like"]').click()
                    time.sleep(.5)
                    el = self.driver.find_element_by_xpath('//button[contains(@class, "oW_lN")  and not(contains(@class, "_8A5w5"))]')
                    self.driver.execute_script("arguments[0].click();", el)
                    time.sleep(1)
                    i += 1
                except:
                    pass
                try:
                    self.driver.find_element_by_xpath('//button[contains(text(),"Cancel")]').click()
                except:
                    pass
                self.driver.find_element_by_css_selector('.ckWGn').click()
                time.sleep(random.random() * 1)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        if (i > 130):
            self.save_stats()
            return i

    def browse_suggested(self):
        self.driver.get("https://www.instagram.com/explore/people/suggested/")
        self.driver.refresh()
        time.sleep(2)
        i = 0
        for el in self.driver.find_elements_by_css_selector("._0mzm-"):
            self.driver.execute_script("arguments[0].click();", el)
            i+=1
            time.sleep(.5 + random.random() * 0.5)
        self.save_stats()
        return i

    def get_date(self):
        now = datetime.datetime.now()
        return now.strftime("%d/%m/%Y %H:%M")

    def save_stats(self):
        self.driver.get("https://www.instagram.com/{}/".format(self.creds['username']))
        time.sleep(1)
        followers = int(self.driver.find_elements_by_css_selector(".g47SY")[1].text.replace(",", ""))
        followed = int(self.driver.find_elements_by_css_selector(".g47SY")[2].text.replace(",", ""))
        if (not os.path.isfile('stats.json')):
            with open('stats.json', 'w+') as file:
                file.write('[]')
        else:
            history = json.loads(open('stats.json').read())
            history.append({
                "date": self.get_date(),
                "followed": followed,
                "followers": followers
            })
            with open('stats.json', 'w+') as file:
                file.write(json.dumps(history))

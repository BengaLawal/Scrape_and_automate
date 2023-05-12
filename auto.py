from soup import Soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# fill the data from make_soup() - into googleform

FIREFOX_DRIVER_PATH = "/home/gbenga/Desktop/python/Progress/geckodriver-v0.31.0-linux64/geckodriver"

class FillForm(Soup):
    def __init__(self, form_link, property24_url):
        super().__init__()
        self.s = Service(FIREFOX_DRIVER_PATH)
        self.driver = webdriver.Firefox(service=self.s)
        self.make_soup(property24_url=property24_url)
        self.countdown = len(self.data)
        self.form_link = form_link

    def fill_form(self):
        """
        Automate the process of filling in google form
        """
        self.driver.get(url=self.form_link)

        for i in range(len(self.data)):
            price_answer = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/'
                                                              'div/div/div[2]/div/div[1]/div/div[1]/input')
            price_answer.send_keys(self.data[i][0])
            time.sleep(2)

            location_answer = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]'
                                                                 '/div/div/div[2]/div/div[1]/div/div[1]/input')
            location_answer.send_keys(self.data[i][1])
            time.sleep(2)

            link_answer = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/'
                                                             'div/div/div[2]/div/div[1]/div/div[1]/input')
            link_answer.send_keys(self.data[i][2])
            time.sleep(2)

            submit_button = self.driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/'
                                                               'div[1]/div/span/span')
            submit_button.click()
            time.sleep(4)

            # submit another response
            another_response = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
            another_response.click()
            time.sleep(4)

            self.countdown -= 1
            print(self.countdown)

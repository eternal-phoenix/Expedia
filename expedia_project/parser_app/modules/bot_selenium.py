import os
import pickle
import load_django
from parser_app import models
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

from time import sleep
from django.utils import timezone

HOME_PAGE = 'https://www.expedia.com/'
URL = r'https://www.expedia.com/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from%3AWashington+%28DCA+-+Ronald+Reagan+Washington+National%29%2Cto%3AKathmandu+%28KTM+-+Tribhuvan+Intl.%29%2Cdeparture%3A7%2F13%2F2023TANYT&options=cabinclass%3Aeconomy&leg2=from%3AKathmandu+%28KTM+-+Tribhuvan+Intl.%29%2Cto%3AWashington+%28DCA+-+Ronald+Reagan+Washington+National%29%2Cdeparture%3A7%2F14%2F2023TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY&fromDate=7%2F13%2F2023&toDate=7%2F14%2F2023&d1=2023-07-13&d2=2023-07-14'


class SeleniumBot():

    def __init__(self) -> None:

        self.DEBUG = False
        self.service = Service(ChromeDriverManager().install())
        self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--no-sandbox')
        self.chrome_options.add_argument('--enable-javascript')
        self.chrome_options.add_argument("--disable-dev-shm-usage")
        self.chrome_options.add_argument('--disable-gpu')
        self.chrome_options.add_argument('--disable-blink-features=AutomationControlled')

        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)
        self.driver.maximize_window()


    def get_data(self) -> None:
        items = self.driver.find_elements(by=By.XPATH, value='//div[@data-test-id="intersection-observer"]')
        for item in items:
            try:
                price = item.find_element(by=By.XPATH, value='.//span[@class="uitk-lockup-price"]').text
                time = item.find_element(by=By.XPATH, value='.//div[@data-test-id="arrival-time"]').text
                print(f'\n---time:{time}---price:{price}')
                yield time, price
            except NoSuchElementException:
                continue
            

    
    def perform_search(self, flying_from: str, flying_to: str) -> None:
        self.driver.get(HOME_PAGE)

        # select flights
        self.driver.find_element(by=By.XPATH, value='//span[@class="uitk-tab-text"][contains(text(), "Flights")]').click()
        sleep(5)
        # enter origin
        self.driver.find_element(by=By.XPATH, value='//button[@aria-label="Leaving from"]').click()
        sleep(10)
        try:
            input_from = self.driver.find_element(by=By.ID, value='location-field-leg1-origin')
        except NoSuchElementException:
            try:
                input_from = self.driver.find_element(by=By.XPATH, value='//*[@id="location-field-leg1-origin"]')
            except NoSuchElementException:
                try:
                    input_from = self.driver.find_element(by=By.XPATH, value='//*[@data-stid="location-field-leg1-origin-menu-input"]')
                except NoSuchElementException:
                    input_from = self.driver.find_element(by=By.XPATH, value='//section[@data-testid="popover-sheet"]//input')
        input_from.clear()
        input_from.send_keys(flying_from)
        sleep(5)
        self.driver.find_elements(by=By.XPATH, value='//div[@class="uitk-action-list-item-content"]//button')[0].click()
        # enter destination
        self.driver.find_element(by=By.XPATH, value='//button[@aria-label="Going to"]').click()
        sleep(10)
        try:
            input_to = self.driver.find_element(by=By.ID, value='location-field-leg1-destination')
        except NoSuchElementException:
            try:
                input_to = self.driver.find_element(by=By.XPATH, value='//*[@id="location-field-leg1-destination"]')
            except NoSuchElementException:
                try:
                    input_to = self.driver.find_element(by=By.XPATH, value='//*[@data-stid="location-field-leg1-destination-menu-input"]')
                except NoSuchElementException:
                    input_to = self.driver.find_element(by=By.XPATH, value='//section[@data-testid="popover-sheet"]//input')
        input_to.clear()
        input_to.send_keys(flying_to)
        sleep(5)
        self.driver.find_elements(by=By.XPATH, value='//div[@class="uitk-action-list-item-content"]//button')[0].click()
        # search results
        self.driver.find_element(by=By.XPATH, value='//button[@data-testid="submit-button"]').click()
        sleep(15)
        

    def kill_driver(self) -> None:
        self.driver.close()
        self.driver.quit()


def run_bot():
    bot = SeleniumBot()
    for from_obj in models.FlyingFrom.objects.filter(status=True):
        for to_obj in models.FlyingTo.objects.filter(status=True):
            bot.perform_search(flying_from=from_obj.name, flying_to=to_obj.name)
            for time, price in bot.get_data():
                models.AviaTicketsInfo.objects.create(
                    date=timezone.now(), 
                    flying_from=from_obj.name, 
                    flying_to=to_obj.name, 
                    time=time, 
                    price=price, 
                )


if __name__ == '__main__':
    run_bot()
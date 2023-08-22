import requests 
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent
from pprint import pprint


url = r'https://www.expedia.com/Flights-Search?flight-type=on&mode=search&trip=roundtrip&leg1=from%3AWashington+%28DCA+-+Ronald+Reagan+Washington+National%29%2Cto%3AKathmandu+%28KTM+-+Tribhuvan+Intl.%29%2Cdeparture%3A7%2F13%2F2023TANYT&options=cabinclass%3Aeconomy&leg2=from%3AKathmandu+%28KTM+-+Tribhuvan+Intl.%29%2Cto%3AWashington+%28DCA+-+Ronald+Reagan+Washington+National%29%2Cdeparture%3A7%2F14%2F2023TANYT&passengers=children%3A0%2Cadults%3A1%2Cseniors%3A0%2Cinfantinlap%3AY&fromDate=7%2F13%2F2023&toDate=7%2F14%2F2023&d1=2023-07-13&d2=2023-07-14'
ua = FakeUserAgent()
headers = {
    'User-Agent': ua.chrome,
}

# res = requests.get(url=url, headers=headers)
# soup = BeautifulSoup(res.text, 'lxml')

# prices = soup.find('div', attrs={'class':'uitk-layout-flex-item uitk-layout-flex-item-flex-shrink-0'})
# pprint(prices.text)


print(ord('a'), ord('z'))

        # self.wait.until(EC.element_to_be_clickable((By.XPATH, '//span[@class="uitk-tab-text"][contains(text(), "Flights")]'))).click()

        # # select leaving from
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Leaving from"]'))).click()
        # input_from = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="location-field-leg1-origin"]')))
        # input_from.clear()
        # input_from.send_keys('fr')
        # self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="uitk-action-list-item-content"]//button')))[0].click()

        # # select going to
        # self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@aria-label="Going to"]'))).click()
        # input_to = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="location-field-leg1-destination"]')))
        # input_to.clear()
        # input_to.send_keys('to')
        # self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="uitk-action-list-item-content"]//button')))[0].click()
        





    # def get_directions(self) -> None:
    #     letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    #     self.driver.get(HOME_PAGE)
    #     self.driver.find_element(by=By.XPATH, value='//span[@class="uitk-tab-text"][contains(text(), "Flights")]').click()
    #     sleep(5)
    #     self.driver.find_element(by=By.XPATH, value='//button[@aria-label="Leaving from"]').click()
    #     sleep(10)
    #     input_field = self.driver.find_element(by=By.XPATH, value='//*[@id="location-field-leg1-origin"]')
    #     directions = set()
    #     for char in letters:
    #         for second_char in letters:
    #             input_field.clear()
    #             input_field.send_keys(f'{char}{second_char}')
    #             sleep(2)
    #             airports = {item.text for item in self.driver.find_elements(by=By.XPATH, value='//li[@data-stid="location-field-leg1-origin-result-item"]//div[@class="uitk-layout-flex"]//div[@class="truncate"]')}
    #             directions.update(airports)
    #     print(sorted(directions))





            # bot.get_directions()


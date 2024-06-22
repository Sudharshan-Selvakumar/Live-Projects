from time import sleep
from selenium.webdriver.common.by import By

class searching_buses:
    xpath_from_city = "//input[@id='src']"
    xpath_to_city = "//input[@id='dest']"
    # xpath_date = "//text[@class='dateText']"
    xpath_search = "//button[text()='SEARCH BUSES']"

    def __init__(self, driver):
        self.driver = driver

    def from_city(self, fromcitykeyword):
        self.driver.find_element(By.XPATH, self.xpath_from_city).send_keys(fromcitykeyword)
        sleep(3)

    def to_city(self, tocitykeyword):
        self.driver.find_element(By.XPATH, self.xpath_to_city).send_keys(tocitykeyword)
        sleep(5)

    # def date_select(self):
    #     self.driver.find_element(By.XPATH, self.xpath_date).click()
    #     sleep(5)
    def search_click(self):
        self.driver.find_element(By.XPATH, self.xpath_search).click()
        sleep(5)
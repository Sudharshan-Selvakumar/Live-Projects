from time import sleep
from selenium.webdriver.common.by import By

class searching_buses:
    xpath_from_city = "//input[@id='src']"
    xpath_to_city = "//input[@id='dest']"
    class_date = "labelCalendarContainer"
    id_search = "search_button"

    def __init__(self, driver):
        self.driver = driver

    def from_city(self, fromcitykeyword):
        self.driver.find_element(By.XPATH, self.xpath_from_city).send_keys(fromcitykeyword)

    def to_city(self, tocitykeyword):
        self.driver.find_element(By.XPATH, self.xpath_to_city).send_keys(tocitykeyword)

    def date_select(self):
        self.driver.find_element(By.CLASS_NAME, self.class_date).click()
        sleep(5)
    def click_search(self):
        self.driver.find_element(By.ID, self.id_search).click()
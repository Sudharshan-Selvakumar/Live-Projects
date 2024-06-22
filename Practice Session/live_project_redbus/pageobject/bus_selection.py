from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class selecting_buses:
    xpath_depttime = "//li[@class='checkbox']/label[@title='After 6 pm']"
    xpath_bustype = "//label[text()='NONAC']"
    xpath_singleseat = "//label[@title='Single Seats']"
    xpath_arrtime = '//li [@class="checkbox"]/label[@title="6 am to 12 pm"]'
    xpath_amenities = "//li[@value='7']/span[text()='Charging Point']"
    xpath_fare = "//span[text()='Fare']"
    xpath_sblt_bus = "//div[text()='(SBLT) Shri Bhagiyalakshimi Travels (MAARA)']"
    xpath_scrollforbt = '//label[@title="Single Seats"]'
    xpath_scrollforsa = '//div[text()="ARRIVAL TIME"]'
    xpath_scrollforat = '//div[text()="BOARDING POINT"]'
    xpath_mainpage = '//div[@class="search"]'
    xpath_viewseat = "//div[text()='(SBLT) Shri Bhagiyalakshimi Travels (MAARA)']/ancestor::li[@id='19034081']/div/div[2]/div[text()='View Seats']"
    xpath_scrolltolayout = "//div[text()='Upper Deck']"

    def __init__(self, driver):
        self.driver = driver

    def departure(self):
        self.driver.find_element(By.XPATH, self.xpath_depttime).click()
        sleep(5)

    def bustypes(self):
        action_obj = ActionChains(self.driver)
        action_obj.scroll_to_element(self.driver.find_element(By.XPATH, self.xpath_scrollforbt)).perform()
        self.driver.find_element(By.XPATH, self.xpath_bustype).click()
        sleep(5)
    def seattype(self):
        action_obj = ActionChains(self.driver)
        action_obj.scroll_to_element(self.driver.find_element(By.XPATH, self.xpath_scrollforsa)).perform()
        self.driver.find_element(By.XPATH, self.xpath_singleseat).click()
        sleep(5)
    def arrival(self):
        action_obj = ActionChains(self.driver)
        action_obj.scroll_to_element(self.driver.find_element(By.XPATH, self.xpath_scrollforat)).perform()
        self.driver.find_element(By.XPATH, self.xpath_arrtime).click()
        sleep(5)
    def needed_amenities(self):
        self.driver.find_element(By.XPATH, self.xpath_amenities).click()
        sleep(5)
    def sort_fare(self):
        self.driver.find_element(By.XPATH, self.xpath_fare).click()
        sleep(5)
    def fav_bus(self):
        action_obj = ActionChains(self.driver)
        action_obj.scroll_to_element(self.driver.find_element(By.XPATH, self.xpath_sblt_bus)).perform()
        sleep(3)
        self.driver.find_element(By.XPATH, self.xpath_viewseat).click()
        sleep(3)
import os
from time import sleep
import os
from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


service_obj = Service(r"E:\selenium\drivers\chromedriver.exe")
###download preference
location=os.getcwd()
print(location)

preference={"download.default_directory":location}
ch_op = webdriver.ChromeOptions()
ch_op.add_experimental_option("prefs", preference)
ch_op.add_argument("--headless")
driver = webdriver.Chrome(service=service_obj, options=ch_op)

driver.get("https://admin-demo.nopcommerce.com/")
driver.maximize_window()
driver.implicitly_wait(10)

####login
sleep(5)
driver.find_element(By.XPATH, "//button[@type='submit']").click()
print(driver.title)
###using select menu
sleep(5)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/a/p[contains(text(),'Catalog')]").click()
sleep(3)
driver.find_element(By.XPATH, "//ul[@role='menu']/li/ul/li/a/p[text()=' Products']").click()

####download file
driver.find_element(By.NAME, "download-catalog-pdf").click()
print(driver.title)
sleep(20)
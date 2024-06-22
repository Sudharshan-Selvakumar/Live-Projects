from time import sleep

from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://tod.amazon.com/test_runs/574659549585-us-west-2-1d341a27-c199-4f86-8926-76214549d35e-1713903750?referer=pipelines")
driver.maximize_window()
driver.implicitly_wait(20)
# driver.find_element(By.XPATH,"//div[@id='stage-name-Gamma']/div/div[7]/div/a[@class='expand-indicator']").click()
# sleep(5)
# driver.find_element(By.XPATH,"//a[@href='https://tod.amazon.com/test_runs/574659549585-us-west-2-1d341a27-c199-4f86-8926-76214549d35e-1713903750?referer=pipelines']").click()
sleep(100)

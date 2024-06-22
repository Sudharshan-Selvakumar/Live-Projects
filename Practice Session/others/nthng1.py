from selenium.webdriver.common.by import By


class Login:
    email_id = "email"
    password_id = "pass"
    login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def SetEmail(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def SetPassword(self, pswd):
        self.driver.find_element(By.ID, self.password_id).send_keys(pswd)

    def SetLogin(self):
        self.driver.find_element(By.XPATH, self.login_xpath).click()

#testcase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import sys
sys.path.append("/")
from Hybrid_Framework.PageObject.gm_login import Login
ss = (r"C:\Users\ssudharv\PycharmProjects\Practice Session\Hybrid_Framework\Snaps")

class Test_Login_1:
    def test_login_title(self, common_data):
        # service_obj = Service(r"C:\Users\ssudharv\selenium\drivers\chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)
        # driver.get("https://www.facebook.com/")
        driver = common_data

        if driver.title == "youtube – log in or sign up":
            assert True
        else:
            driver.save_screenshot(ss+"\\"+"snap_1.png")
            assert False

    def test_login_inputs(self, common_data):
        # service_obj = Service(r"C:\Users\ssudharv\selenium\drivers\chromedriver.exe")
        # driver = webdriver.Chrome(service=service_obj)
        # driver.get("https://www.facebook.com/")
        # driver.implicitly_wait(10)
        driver = common_data
        login_obj = Login(driver)
        login_obj.SetEmail("9944331699")
        login_obj.SetPassword("7200100700")
        login_obj.SetLogin()
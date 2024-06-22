import pytest
from selenium import webdriver
import sys


@pytest.fixture()
def launch_browser(request):
    browser = request.config.getoption("--browser")
    if browser=="chrome":
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"C:\Users\ssudharv\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser=="edge":
        from selenium.webdriver.edge.service import Service
        service_obj = Service(r"C:\Users\ssudharv\selenium\drivers\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
    elif browser=="firefox":
        from selenium.webdriver.firefox.service import Service
        service_obj = Service(r"C:\Users\ssudharv\selenium\drivers\geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj)
    else:
        from selenium.webdriver.chrome.service import Service
        service_obj = Service(r"C:\Users\ssudharv\selenium\drivers\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield driver
        driver.quit()

def pytest_addoption(parser):
        parser.addoption("--browser")

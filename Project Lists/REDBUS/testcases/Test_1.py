import sys
sys.path.append(r"C:\Users\ssudharv\PycharmProjects\Project Lists")
from REDBUS.pageobject.travel_details import searching_buses
from REDBUS.utilities.ReadConfig import ReadProperty
from REDBUS.utilities.CustomLogger import customlog
ss = r"C:\Users\ssudharv\PycharmProjects\Project Lists\REDBUS\screenshots"

class Test_001:
    log = customlog()
    def test_verify_title(self, launch_browser):
        self.log.info("Testcase_1::Verify Title Page")
        driver = launch_browser
        driver.get(ReadProperty.geturl1())
        title = driver.title
        if "Book Bus Tickets Online, Easy & Secure Booking" in title:
            self.log.info("Testcase_1::Correct Website")
            driver.save_screenshot(ss+"\\"+"Testcase_1 Correct Website.png")
            assert True
        else:
            self.log.error("Testcase_1::Wrong Website")
            driver.save_screenshot(ss+"\\"+"Testcase_1 Wrong Website.png")
            assert False

    def test_travel_details(self, launch_browser):
        driver = launch_browser
        driver.get(ReadProperty.geturl1())
        details_obj = searching_buses(driver)
        details_obj.from_city(ReadProperty.getfromcity1())
        details_obj.to_city(ReadProperty.gettocity3())
        # details_obj.date_select()
        details_obj.search_click()
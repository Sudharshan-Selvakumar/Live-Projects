import sys
sys.path.append(r"C:\Users\ssudharv\PycharmProjects\Practice Session")
from live_project_redbus.pageobject.travel_details import searching_buses
from live_project_redbus.utilities.ReadConfig import ReadProperty

ss = r"C:\Users\ssudharv\PycharmProjects\Practice Session\live_project_redbus\screenshots"

class Test_001:
    def test_verify_title(self, launch_browser):
        driver = launch_browser
        driver.get(ReadProperty.geturl1())
        title = driver.title
        if "Book Bus Tickets Online, Easy & Secure Booking" in title:
            assert True
        else:
            driver.save_screenshot(ss + "\\" + "redbuswebsite.png")
            assert False

    def test_travel_details(self, launch_browser):
        driver = launch_browser
        driver.get(ReadProperty.geturl1())
        driver.maximize_window()
        driver.implicitly_wait(5)
        details_obj = searching_buses(driver)
        details_obj.from_city(ReadProperty.getfromcity1())
        details_obj.to_city(ReadProperty.gettocity3())
        details_obj.date_select()
        details_obj.click_search()
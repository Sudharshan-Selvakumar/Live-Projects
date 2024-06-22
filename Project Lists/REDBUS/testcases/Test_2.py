import sys
sys.path.append(r"C:\Users\ssudharv\PycharmProjects\Project Lists")
from REDBUS.pageobject.bus_selection import selecting_buses
from REDBUS.utilities.CustomLogger import customlog
ss = r"C:\Users\ssudharv\PycharmProjects\Practice Session\live_project_redbus\screenshots"

class Test_002:
    log=customlog()
    def test_verify_buseslist(self, launch_browser):
        self.log.info("Testcase_2::Verify Bus List Page")
        driver = launch_browser
        driver.get("https://www.redbus.in/bus-tickets/chennai-to-aruppukottai?fromCityName=Chennai&fromCityId=123&srcCountry=IND&toCityName=Aruppukottai&toCityId=954&destCountry=IND&onward=1-Jun-2024&opId=0&busType=Any")
        title = driver.title
        if "Chennai to Aruppukottai Bus Online" in title:
            self.log.info("Testcase_2::Correct Website")
            driver.save_screenshot(ss+"\\"+"Testcase_2 Correct Website.png")
            assert True
        else:
            self.log.error("Testcase_2::Wrong Website")
            driver.save_screenshot(ss+"\\"+"Testcase_2 Wrong Website.png")
            assert False


    def test_bus_selection(self, launch_browser):
        driver = launch_browser
        driver.get("https://www.redbus.in/bus-tickets/chennai-to-aruppukottai?fromCityName=Chennai&fromCityId=123&srcCountry=IND&toCityName=Aruppukottai&toCityId=954&destCountry=IND&onward=1-Jun-2024&opId=0&busType=Any")
        driver.maximize_window()
        driver.implicitly_wait(5)
        selection_obj=selecting_buses(driver)
        selection_obj.departure()
        selection_obj.bustypes()
        selection_obj.seattype()
        selection_obj.arrival()
        selection_obj.needed_amenities()
        selection_obj.sort_fare()
        selection_obj.fav_bus()
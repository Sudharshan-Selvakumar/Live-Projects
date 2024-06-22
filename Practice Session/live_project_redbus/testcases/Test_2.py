import sys
sys.path.append(r"C:\Users\ssudharv\PycharmProjects\Practice Session")
from live_project_redbus.pageobject.bus_selection import selecting_buses
ss = r"C:\Users\ssudharv\PycharmProjects\Practice Session\live_project_redbus\screenshots"

class Test_002:
    def test_verify_buseslist(self, launch_browser):
        driver = launch_browser
        driver.get("https://www.redbus.in/bus-tickets/chennai-to-aruppukottai?fromCityName=Chennai&fromCityId=123&srcCountry=IND&toCityName=Aruppukottai&toCityId=954&destCountry=IND&onward=1-Jun-2024&opId=0&busType=Any")
        title = driver.title
        if "Chennai to Aruppukottai Bus Online" in title:
            assert True
        else:
            driver.save_screenshot(ss+"\\"+"buslisttitlepage.png")
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
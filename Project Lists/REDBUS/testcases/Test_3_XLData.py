import sys
import pytest

sys.path.append(r"C:\Users\ssudharv\PycharmProjects\Project Lists")
from REDBUS.pageobject.travel_details import searching_buses
from REDBUS.utilities.CustomLogger import customlog
from REDBUS.testdatas.Load_XLData import *
ss = r"C:\Users\ssudharv\PycharmProjects\Project Lists\REDBUS\screenshots"

class Test_001_XLData:
    xlpath = r"C:\Users\ssudharv\PycharmProjects\Project Lists\REDBUS\testdatas\redbus.xlsx"
    sheet = "Sheet1"
    data = load_data_from_xl(xlpath, sheet)
    @pytest.mark.parametrize("fromcity, tocity", data)
    def test_travel_details_XLData(self, launch_browser, fromcity, tocity):
        driver = launch_browser
        driver.get("https://www.redbus.in/")
        details_obj = searching_buses(driver)
        details_obj.from_city(fromcity)
        details_obj.to_city(tocity)
        # details_obj.date_select()
        details_obj.search_click()
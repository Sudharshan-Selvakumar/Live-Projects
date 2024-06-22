from REDBUS.utilities.XlUtility import *

def load_data_from_xl(xlpath, sheet):
    no_row = getrow(xlpath, sheet)
    no_column = getcolumn(xlpath, sheet)
    data_list = []
    for r in range(2, no_row+1):
        temp_list = []
        for c in range(1, no_column+1):
            temp_list.append(readdata(xlpath, sheet, r, c))
        data_list.append(tuple(temp_list))
    return data_list
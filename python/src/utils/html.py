from . import selenium_info as driver_info

def changeVal(id, val):
    id = str(id)
    val = str(val)
    # string = ""

    # print(string)
    driver_info.driver.execute_script("$('"+id+"', '"+val+"')")
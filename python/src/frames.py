import os

import utils.selenium_info as driver_info
from utils.time import setStartTime, setStartYear, addSecond, updateTime
from utils.image import greenscreen, screenshot

def getScreenshots():
    index = 0

    setStartTime(int(input("Starting hour: ")), int(input("Starting minute: ")))
    setStartYear(int(input("Starting year: ")), int(input("Starting month: ")), int(input("Starting day: ")))
    amount_of_seconds = int(input("Put your time in minutes: ")) * 60
    while amount_of_seconds - index > 0:
        # Save the file as the value of the index
        temp_cache_file = os.path.join(driver_info.cache_path, str(index) + '.png')
        addSecond()
        updateTime()

        screenshot(temp_cache_file)
        # greenscreen(temp_cache_file)

        index += 1

    driver_info.driver.quit()
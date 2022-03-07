# Initiate the window 
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

import os

def init():
    global driver                       # Allow other files to see the driver 
    global save_path
    global cache_path
    global html_file

    save_path = os.path.join(os.getcwd(), 'output')
    cache_path = os.path.join(save_path, "cache")
    html_file = os.path.join(os.getcwd(), 'top-right.html')

    # driver = webdriver.Firefox()        # Initiate the browser

    options = webdriver.FirefoxOptions()
    options.add_argument("--headless")

    driver = webdriver.Firefox(options=options)

    driver.get(html_file)               # Set the file to the driver

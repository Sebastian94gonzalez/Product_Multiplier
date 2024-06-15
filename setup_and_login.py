from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)
from selenium.webdriver.support.ui import WebDriverWait
import simulate_input as input
import time
# import main
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def driver_setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)    

    # Makes driver wait 10 seconds before throwing an exception
    driver.implicitly_wait(10)

    # create action chain object
    action = ActionChains(driver)

    ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
    wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    return driver, action, wait
    
def login(driver, action, wait):
    # Username
    time.sleep(5)
    input.slow_type(driver.find_element('xpath', '//*[@id="ap_email"]'), os.getenv('EMAIL'))

    # Password
    input.slow_type(driver.find_element('xpath', '//*[@id="ap_password"]'), os.getenv('PASSWORD'))

    # Sign in button
    input.element_click(driver, action, wait, '//*[@id="signInSubmit"]')



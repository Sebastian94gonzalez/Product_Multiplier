
from data_processing import data
import simulate_input as input
import setup_and_login as snl
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
import time
import random


# class main:
# VARS:
first_attempt = True
temp_row = 0
# create_file_path = "C:/Users/Administrator/Desktop/Product_Multiplier/export.xlsx"
# data.create_dataframe(create_file_path)
titles_table_path = "C:/Users/Administrator/Desktop/Product_Multiplier/Titles_table.csv"

driver, action, wait = snl.driver_setup()

url = "https://merch.amazon.com/resource/productor-products"
driver.get(url)

input.element_click(driver, action, wait, '//*[@id="header-links"]/a[2]')
# driver.maximize_window()

snl.login(driver, action, wait)
# Tab: Manage
time.sleep(5)
input.element_click(driver, action, wait, '//*[@id="nav-container"]/div/ul/li[3]/a')


while True:
    
    design_name, row, temp_row = data.next_title(titles_table_path, first_attempt, temp_row)
    first_attempt = False

    # Designs tab
    # //*[@id="tab-designs"]/a

    # Search bar
    input.slow_type(driver.find_element('xpath','//*[@id="search-bar"]'), design_name)

    # Submit
    input.element_click(driver, action, wait, '//*[@id="search-button"]')
    time.sleep(10)
    
    try:
        tag = driver.find_element(By.TAG_NAME, 'tr')
        # print(tag.get_attribute("outerHTML"))
        # print('Something went wrong' in tag.get_attribute("outerHTML"))
        while 'Something went wrong' in tag.get_attribute("outerHTML"):
            print('RETRY')
            # Re-Submit
            input.element_click(driver, action, wait, '//*[@id="search-button"]')
            time.sleep(10)
            tag = driver.find_element(By.TAG_NAME, 'tr')
            # print(tag.get_attribute("outerHTML"))
            # print('Something went wrong' in tag.get_attribute("outerHTML"))
    except: 
        pass
    
    processing_flag = False
    tags = driver.find_elements(By.ID, 'listing-title-with-asin')
    for count in range(1, len(tags)):
        tag = driver.find_element(By.XPATH, '/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/items-table/table/tr['+ str(count) +']/td[2]')
        # print(tag.get_attribute("outerHTML"))
        print('Looking for titles count: ' + str(count))
        if design_name in tag.get_attribute("outerHTML"):
            status = driver.find_elements(By.ID, 'status-column')
            
            # print('Auto-uploaded' in status[count - 1].get_attribute("outerHTML") or 'Live' in status[count - 1].get_attribute("outerHTML"))
            # print(status[count - 1].get_attribute("outerHTML"))
            if 'Processing' in status[count - 1].get_attribute("outerHTML") or 'Translating' in status[count - 1].get_attribute("outerHTML"):
                row += 1
                processing_flag = True
                print('Selecting new title. This design is being processed or translated')
                break
            elif 'Auto-uploaded' in status[count - 1].get_attribute("outerHTML") or 'Live' in status[count - 1].get_attribute("outerHTML"):
                print('Found title in row: ' + str(count - 1))
                # Edit buttton
                input.element_click(driver, action, wait, '/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/items-table/table/tr['+ str(count) +']/td[8]/div/button')
                # element_click(driver, action, wait, '/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[3]/items-table/table/tr['+ str(count) +']/td[8]/div/div/i[1]')
                input.element_click(driver, action, wait, '/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/items-table/table/tr['+ str(count) +']/td[8]/div/div/i[1]')
                # element_click(driver, action, wait, '/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/items-table/table/tr[1]/td[8]/div/div/i[1]
                break

    if processing_flag:
        continue

    input.close_tab(driver)

    # Select products
    time.sleep(15)    
    input.element_click(driver, action, wait, '//*[@id="select-marketplace-button"]')
    # Product selector
    input.product_selector(driver, action, wait,)

    # Continue
    input.element_click(driver, action, wait, '/html/body/ngb-modal-window/div/div/ng-component/div[3]/button')

    # Translation
    input.element_click(driver, action, wait, '/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/product-config-editor/translation-options/div/div[1]/label/span[2]')
    # .get_attribute('value') !=  #   Validate there is no 'gift' word need to account for caps, no caps, variations etc

    # Publish
    input.element_click(driver, action, wait, '//*[@id="submit-button"]')

    # Confirm Publish
    input.element_click(driver, action, wait, '/html/body/ngb-modal-window/div/div/ng-component/div[2]/div[2]/button[2]')

    # View Manage Page
    input.element_click(driver, action, wait, '//*[@id="redirect-manage"]')
    # X out of window /html/body/ngb-modal-window/div/div/ng-component/div[1]/button/span

    data.complete_round(temp_row, titles_table_path)

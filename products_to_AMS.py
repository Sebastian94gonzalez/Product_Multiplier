import setup_and_login as snl
import simulate_input as input
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (ElementNotVisibleException, ElementNotSelectableException)


# VARS:
asins_path = "C:/Users/Administrator/Desktop/Product_Multiplier/asins_IT.csv"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)    

# Makes driver wait 10 seconds before throwing an exception
driver.implicitly_wait(10)

# create action chain object
action = ActionChains(driver)

ignore_list = [ElementNotVisibleException, ElementNotSelectableException]
wait = WebDriverWait(driver, timeout=10, poll_frequency=1, ignored_exceptions=ignore_list)
    # return driver, action, wait

url = "https://merch.amazon.com/resource/productor-products"
driver.get(url)
input.element_click(driver, action, wait, '//*[@id="header-links"]/a[2]')
# driver.maximize_window()
snl.login(driver, action, wait)
# Tab: Manage
time.sleep(5)
input.element_click(driver, action, wait, '//*[@id="nav-container"]/div/ul/li[3]/a')

# Tab: Advertise
input.element_click(driver, action, wait, '//*[@id="nav-container"]/div/ul/li[5]/a')

# Advertise on Amazon.com
# # US
# input.element_click(driver, action, wait,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/div[1]/table/tbody/tr[2]/td/span[2]/a')
# # GB
# input.element_click(driver, action, wait,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/div[1]/table/tbody/tr[3]/td/span[2]/a')
# # DE
# input.element_click(driver, action, wait,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/div[1]/table/tbody/tr[4]/td/span[2]/a')
# # FR
# input.element_click(driver, action, wait,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/div[1]/table/tbody/tr[5]/td/span[2]/a')
# IT
input.element_click(driver, action, wait,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/div[1]/table/tbody/tr[6]/td/span[2]/a')
# # SP
# input.element_click(driver, action, wait,'/html/body/div[1]/div/app-root/div/div[2]/ng-component/div/div[2]/div[1]/table/tbody/tr[7]/td/span[2]/a')

input.close_tab(driver)
snl.login(driver, action, wait)
# All Campaign
input.element_click(driver, action, wait,'//*[@id="CAMPAIGNS"]/div/div[2]/div[1]/div/div/div[3]/div')

# All Ad group
time.sleep(10)
input.element_click(driver, action, wait,'/html/body/div[1]/div[5]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div[2]/div[2]/div/div[2]/div/div/a')
# input.element_click(driver, action, wait,'//*[@id="A08425175UG4YUME4ZO7"]')
# input.element_click(driver, action, wait,'//*[@id="A097472828BGOS5GC56PU"]')

# Add products to advertise
input.element_click(driver, action, wait,'//*[@id="AD_GROUP_ADS"]/div[2]/div/div[1]/span/button')

# Tab: Enter list
time.sleep(10)
input.element_click(driver, action, wait,'//*[@id="AACChromePortal"]/div/div/div/div[2]/div/div/div[1]/div[1]/div/nav/ul/li[2]/button')
# //*[@id="AACChromePortal"]/div/div/div/div[2]/div/div/div[1]/div[1]/div/nav/ul/li[1]/button
# //*[@id="AACChromePortal"]/div/div/div/div[2]/div/div/div[1]/div[1]/div/nav/ul/li[2]/button
# //*[@id="AACChromePortal"]/div/div/div/div[2]/div/div/div[1]/div[1]/div/nav/ul/li[3]/button

# ASINs text box
input.element_click(driver, action, wait,'//*[@id="UCM-SP-APP:AD_GROUP_ADS:ups:ups-product-list-input"]')

def submit():
    input.element_click(driver, action, wait,'')

csv_df = pd.read_csv(asins_path, header=None)

print(len(csv_df.index))
print(len(csv_df.index) // 998)

start = 0
# finish = 998
finish = 100

# for count in range(2, (len(csv_df.index) // 998) + 2):
for count in range(2, (len(csv_df.index) // 100) + 2):
    print('Start: ' + str(start))
    print('Finish: ' + str(finish))
    print('Length: ' + str(len(csv_df[start:finish])))

    asins_df = csv_df[start:finish]
    print(asins_df)
    string = ' '.join(map(str,asins_df[0]))
    driver.find_element('xpath','//*[@id="UCM-SP-APP:AD_GROUP_ADS:ups:ups-product-list-input"]').send_keys(string)

    # Add
    input.element_click(driver, action, wait,'//*[@id="AACChromePortal"]/div/div/div/div[2]/div/div/div[1]/div[2]/div[2]/button')
    
    
    # for row in asins_df.index:
    #     driver.find_element('xpath','//*[@id="UCM-SP-APP:AD_GROUP_ADS:ups:ups-product-asins_df-input"]').send_keys(asins_df[0][row] + ' ')
        # print(asins_df[0][row])
        

    start = finish 
    # finish = 998 * count
    finish = 100 * count


time.sleep(1)
# Add products to advertise
input.element_click(driver, action, wait,'//*[@id="AACChromePortal"]/div/div/div/div[3]/button[2]')

time.sleep(90000)
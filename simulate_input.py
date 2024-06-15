from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def close_tab(driver):
    # Close first tab and switch to newly opened tab
    time.sleep(2)
    driver.close()
    time.sleep(2)
    driver.switch_to.window(driver.window_handles[0])

# Slow typing function
def slow_type(pageElem, pageInput):
    pageElem.clear()
    # time.sleep(3)
    for letter in pageInput:
        # time.sleep(float(random.uniform(.008, .015)))
        # time.sleep(float(random.uniform(.1, .19)))
        pageElem.send_keys(letter)

# Wait for element to load
def element_click(driver, action, wait, xpath):
    # time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
    # element = driver.find_element('xpath',xpath)
    action.move_to_element(driver.find_element('xpath',xpath)).click().perform()
    # return element

def product_selector(driver, action, wait):
    time.sleep(5)   # Checking if function not waiting for load of element.
    # PopSockets grip (ES)
    # element_click(driver, action, wait,'/html/body/ngb-modal-window/div/div/ng-component/div[2]/div/div/table/tbody/tr[12]/td[7]/flowcheckbox/span/i')
    for country in range(2,9):
        # Standard t-shirt
        element_click(driver, action, wait,'/html/body/ngb-modal-window/div/div/ng-component/div[2]/div/div/table/tbody/tr[2]/td[' + str(country) + ']/flowcheckbox/span/i')
        # element_click(driver, action, wait,'/html/body/ngb-modal-window/div/div/ng-component/div[2]/div/div/table/tbody/tr[3]/td[' + str(country) + ']/flowcheckbox/span/i')
        # pass
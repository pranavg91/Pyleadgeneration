import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_lead():
    driver = webdriver.Chrome()
    driver.get("https://psquickit2-dev-ed.develop.my.salesforce.com/")

    time.sleep(10)
    #
    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.send_keys("pranav.hitmantoto@psquickit.com")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("7Iron-hide")
    submit_button = driver.find_element(By.ID, "Login")
    submit_button.click()
    #
    # time.sleep(20)
    #
    # assert "psquickit2" in driver.page_source
    # driver.maximize_window()
    # driver.find_element(By.XPATH, "//div[@class='slds-icon-waffle']/..//div[@class='slds-icon-waffle']").click()
    #
    # time.sleep(10)
    #
    # actions = ActionChains(driver)
    #
    # driver.find_element(By.XPATH,"//div[@class='slds-r6']//following::input[@id='input-113']").send_keys("Leads")
    # time.sleep(10)
    # actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    #
    # time.sleep(10)
    #
    # # click to new button
    #
    # driver.find_element(By.XPATH,"//div[@role='group']//preceding::button[normalize-space()='New']").click()
    # time.sleep(10)
    # driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("jindal")
    # time.sleep(10)
    # driver.find_element(By.XPATH,"//input[@name='Company']").send_keys("JND")
    # time.sleep(10)
    #
    # driver.find_element(By.XPATH,"//button[@name='SaveEdit']").click()
    # driver.implicitly_wait(50)
    #
    driver.get("https://psquickit2-dev-ed.develop.lightning.force.com/lightning/r/Lead/00QdM0000023eJ7UAI/view")

    time.sleep(56)

    matchStateType = driver.find_element(By.XPATH,
                                         "//div[@class='runtime_sales_pathassistantPathAssistant']//a[@title='Converted']")
    driver.execute_script("arguments[0].click();", matchStateType)
    #

    stateType =driver.find_element(By.XPATH,"//button[@class ='slds-button slds-button--brand slds-path__mark-complete stepAction active uiButton']")
    driver.execute_script("arguments[0].click();",stateType)
    # driver.find_element(By.XPAH,"//button[@class='slds-button slds-button--brand slds-path__mark-complete stepAction current uiButton']").click()

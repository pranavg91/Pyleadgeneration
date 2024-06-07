import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_account():
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

    time.sleep(10)
    app_launcher =driver.find_element(By.XPATH,"//div[@class ='slds-icon-waffle']")
    driver.execute_script("arguments[0].click();",app_launcher)
    time.sleep(20)

    driver.find_element(By.XPATH,"//*[@placeholder ='Search apps and items...']").send_keys("accounts")
    actions =ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(30)
    record = driver.find_element(By.XPATH,"//tbody/tr[3]/td[2]/span[1]/div[1]/../../..//span[@class='slds-grid slds-grid--align-spread forceInlineEditCell']")

    print(record.text)

    assert "JND" in record.text
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_lead():
    driver = webdriver.Chrome()
    driver.get("https://psquickit2-dev-ed.develop.my.salesforce.com/")

    time.sleep(10)

    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.send_keys("pranav.hitmantoto@psquickit.com")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("7Iron-hide")
    submit_button = driver.find_element(By.ID, "Login")
    submit_button.click()

    time.sleep(20)

    assert "psquickit2" in driver.page_source
    driver.maximize_window()
    driver.find_element(By.XPATH, "//div[@class='slds-icon-waffle']/..//div[@class='slds-icon-waffle']").click()

    time.sleep(10)
    actions = ActionChains(driver)
    actions.send_keys("Leads").click().perform()
    time.sleep(30)

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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

    time.sleep(30)
    actions = ActionChains(driver)

    driver.find_element(By.XPATH,"//div[@class='slds-r6']//following::input[@id='input-113']").send_keys("Leads")
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()

    time.sleep(30)

    # click to new button

    driver.find_element(By.XPATH,"//button[@class='slds-button slds-button_neutral slds-button_last toListViewButton']//preceding::button[normalize-space()='New']").click()
    time.sleep(20)



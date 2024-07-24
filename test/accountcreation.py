import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def test_accountcreation():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://psquickit2-dev-ed.develop.my.salesforce.com/")
    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.send_keys("pranav.hitmantoto@psquickit.com")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("7Iron-hide")
    submit_button = driver.find_element(By.ID, "Login")
    submit_button.click()
    time.sleep(15)
    driver.find_element(By.XPATH, "//button[@title='App Launcher']").click()
    time.sleep(10)

    actions = ActionChains(driver)
    driver.find_element(By.XPATH,
                        "//div[@class='slds-r6']//following::input[@placeholder='Search apps and items...']").send_keys(
        "Accounts")
    time.sleep(10)
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(20)
    # New button click

    newclick = driver.find_element(By.XPATH, "//a[@title='New']")
    newclick.click()

    time.sleep(20)

    # Enter account name

    # inputField = driver.find_element(By.XPATH, "//input[@name='Name']")
    # driver.execute_script("arguments[0].setAttribute('value','" + "testing" + "')", inputField)
    driver.find_element(By.XPATH, "//input[@name='Phone']//preceding::input[@name='Name']").send_keys("Testing")
    # Click save button
    time.sleep(10)
    driver.find_element(By.XPATH,"//button[normalize-space()='Save & New']//following::button[@name='SaveEdit']").click()
    # driver.execute_script("arguments[0],click();",save_edit)
    #
    time.sleep(10)

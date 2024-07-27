from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def test_accountupdate():
    driver = webdriver.Chrome()
    driver.get("https://psquickit2-dev-ed.develop.my.salesforce.com/")
    driver.get("https://psquickit2-dev-ed.develop.my.salesforce.com/")
    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.send_keys("pranav.hitmantoto@psquickit.com")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("7Iron-hide")
    submit_button = driver.find_element(By.ID, "Login")
    submit_button.click()
    time.sleep(15)
    driver.get("https://psquickit2-dev-ed.develop.lightning.force.com/lightning/r/Account/001dM00000KW6TjQAL/view")
    time.sleep(7)

    # Navigate to detail page of account.
    # driver.find_element(By.XPATH,"//a[@id='relatedListsTab__item']//following::a[normalize-space()='Details']").click()
    driver.find_element(By.XPATH,
                        "//a[@data-tab-value='relatedListsTab']//following::a[@data-tab-value='detailTab']").click()
    time.sleep(10)
    edit = driver.find_element(By.XPATH,
                               "//span[contains(text(),'Account Name')]//following::span[contains(text(),'Edit Account Name')]")
    driver.execute_script("arguments[0].click();", edit)
    time.sleep(10)
    actions = ActionChains(driver)
    field= driver.find_element(By.XPATH, "//input[@name='Name']")
    field.clear()
    time.sleep(10)
    actions.send_keys("Testing update22").perform()
    time.sleep(10)
    # click to save button
    driver.find_element(By.XPATH,"//*[@name='SaveEdit']").click()
    time.sleep(10)


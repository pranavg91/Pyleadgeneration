import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_lead():
    driver = webdriver.Chrome()
    driver.get("https://psquickit2-dev-ed.develop.my.salesforce.com/")

    time.sleep(30)

    username = driver.find_element(By.XPATH, "//input[@id='username']")
    username.send_keys("pranav.hitmantoto@psquickit.com")
    password = driver.find_element(By.XPATH, "//input[@id='password']")
    password.send_keys("7Iron-hide")
    submit_button = driver.find_element(By.ID, "Login")
    submit_button.click()

    time.sleep(30)

    assert "psquickit2" in driver.page_source

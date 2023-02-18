import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

driver.maximize_window()
time.sleep(2)
element = driver.find_element(By.ID, "user-name")
element.send_keys("standard_user")
time.sleep(2)
elementp = driver.find_element(By.ID, "password")
elementp.send_keys("secret_sauce")
time.sleep(2)
login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()
time.sleep(5)

driver.quit()

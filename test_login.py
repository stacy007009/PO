from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("Test started")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://the-internet.herokuapp.com/login")

print("Page opened")

# enter username
driver.find_element(By.ID, "username").send_keys("tomsmith")

# enter password
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")

# click login
driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

time.sleep(2)

# check result
message = driver.find_element(By.ID, "flash").text

if "You logged into a secure area!" in message:
    print("TEST PASSED ")
else:
    print("TEST FAILED ")

time.sleep(5)

driver.quit()

print("Test finished")
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/text-box")


userName = driver.find_element (By.ID, "userName")
userName.send_keys ("Anna Rubenchik")
email_box = driver.find_element (By.ID, "userEmail")
email_box.send_keys ("annarubqa@gmail.com")
currentAddress = driver.find_element (By.ID, "currentAddress")
currentAddress.send_keys ("Mahal 89 street, Tel Aviv city.")
permanentAddress = driver.find_element (By.ID, "permanentAddress")
permanentAddress.send_keys ("Mahal 89 street, Tel Aviv city.")
submit = driver.find_element (By.ID, "submit")

submit.click()

# full name assertions :
assert_userName = driver.find_element (By.ID, "name").text
assert "Anna Rubenchik" in assert_userName, "Full name is incorrect"

assert_email_box = driver.find_element (By.ID, "email").text
assert "annarubqa@gmail.com" in assert_email_box, "User Email is incorrect" 

output = driver.find_element (By.ID, "output")
assert_currentAddress = output.find_element (By.ID, "currentAddress").text
assert "Mahal 89 street, Tel Aviv city." in assert_currentAddress, "User Address is incorrect" 

assert_permanentAddress = output.find_element (By.ID, "permanentAddress").text
assert "Mahal 89 street, Tel Aviv city." in assert_permanentAddress, "User permanent address is incorrect"

time.sleep(2)

driver.quit()
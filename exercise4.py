from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/webtables")

addNewRecordButton = driver.find_element (By.ID, "addNewRecordButton")
addNewRecordButton.click()
firstName = driver.find_element (By.ID, "firstName")
firstName.send_keys ("Anna")
lastName = driver.find_element (By.ID, "lastName")
lastName.send_keys ("Rubenchik")
userEmail = driver.find_element (By.ID, "userEmail")
userEmail.send_keys ("annarubqa@gmail.com")
age = driver.find_element (By.ID, "age")
age.send_keys ("35")
salary = driver.find_element (By.ID, "salary")
salary.send_keys ("35000")
department = driver.find_element (By.ID, "department")
department.send_keys ("Automation")

print("First Name Field: " + firstName.get_attribute("value"))
print("last Name Field: " + lastName.get_attribute("value"))
print("Email Field: " + userEmail.get_attribute("value"))
print("age Field: " + age.get_attribute("value"))
print("salary Field: " + salary.get_attribute("value"))
print("department Field: " + department.get_attribute("value"))

driver.save_screenshot("1_before_submit.png")

submit = driver.find_element (By.ID, "submit")
submit.click()

time.sleep(1)

driver.save_screenshot("2_after_submit.png")

time.sleep(3)

driver.quit()
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
permanentAddress.send_keys ("")
submit = driver.find_element (By.ID, "submit")

submit.click()

print("Name Field: " + userName.get_attribute("value"))
print("Email Field: " + email_box.get_attribute("value"))
print("Current Address: " + currentAddress.get_attribute("value"))
print("Permanent Address: " + permanentAddress.get_attribute("value"))

driver.save_screenshot("final_form_screenshot.png")


time.sleep(2)

driver.quit()







# permanentAddress.send_keys (Keys.ENTER)
# submit.send_keys ("demosite")



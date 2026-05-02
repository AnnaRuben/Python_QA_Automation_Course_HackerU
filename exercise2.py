from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://bank-api--ahimalka89.replit.app/")

deposit_amount = 50000
deposit = driver.find_element(By.XPATH, "//input[@type = 'number']")
deposit.send_keys(deposit_amount)

button = driver.find_element (By.XPATH, "//button[text()= 'Confirm Deposit']")
button.click()

print(f"💲 Deposit of ${deposit_amount} submitted successfully.")

button = driver.find_element (By.XPATH, "//button[text()= 'Withdraw']")
button.click()


time.sleep(1)

withdraw_amount = 5000
withdraw = driver.find_element(By.XPATH, "//input[@type = 'number']")
withdraw.send_keys(withdraw_amount)

button = driver.find_element (By.XPATH, "//button[text()= 'Confirm Withdrawal']")
button.click()

print(f"💲 Withdrawal of ${withdraw_amount} submitted successfully.")

time.sleep(2)

assert_Recent_Activity = driver.find_element (By.XPATH, "//div[contains(@class, 'custom-scrollbar')]").text

driver.save_screenshot ("deposit_withdraw.png")

assert "5,000" in assert_Recent_Activity 

assert "50,000" in assert_Recent_Activity
print("💲 Data verification passed: Transactions appear correctly in Recent Activity!")

time.sleep(2)

driver.quit()

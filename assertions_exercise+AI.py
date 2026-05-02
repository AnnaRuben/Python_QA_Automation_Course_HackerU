from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/radio-button")

# --- בדיקת כפתור Yes ---
yes_label = driver.find_element(By.XPATH, "//label[@for='yesRadio']")
yes_label.click()

time.sleep(1)

success_text = driver.find_element(By.CLASS_NAME, "text-success").text
print(f"✅ Option selected on screen: {success_text}")

assert "Yes" in success_text
print("✅ Data verification passed: The text 'Yes' appears correctly after clicking!")

driver.save_screenshot("assertions_exercise+AI_Yes.png")

time.sleep(1)

# --- בדיקת כפתור Impressive ---
impressive_label = driver.find_element(By.XPATH, "//label[@for='impressiveRadio']")
impressive_label.click()

time.sleep(1)

# לוקחים שוב את הטקסט העדכני שהשתנה אחרי הלחיצה השנייה
success_text = driver.find_element(By.CLASS_NAME, "text-success").text
print(f"✅ Option selected on screen: {success_text}")

assert "Impressive" in success_text
print("✅ Data verification passed: The text 'Impressive' appears correctly after clicking!")

# צילום מסך של המצב הסופי לאחר שתי הלחיצות
driver.save_screenshot("assertions_exercise+AI_Impressive.png")

time.sleep(2)
driver.quit()
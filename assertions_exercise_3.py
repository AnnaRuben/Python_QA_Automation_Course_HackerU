from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/register")
dynamic_number = int(time.time())

# # Registration with Register button :
# # נשתול את המספר בתוך כתובת המייל בעזרת f-string
my_email = f"annarubqa+{dynamic_number}@gmail.com"

# # נשלח את המייל הדינאמי לשדה
email_input = driver.find_element(By.ID, "email")
email_input.send_keys(my_email)

name_field = driver.find_element (By.ID, "name")
name_field.send_keys ("Anna Rubenchik")

password_input = driver.find_element (By.ID, "password")
password_input.send_keys ("Ana1983ana@@")

confirmPassword = driver.find_element (By.ID, "confirmPassword")
confirmPassword.send_keys ("Ana1983ana@@")

register_submit = driver.find_element (By.XPATH, "//button[text()= 'Register']")
# # במקום register_submit.click()
driver.execute_script("arguments[0].click();", register_submit)

# # assert :

successful_login_text = driver.find_element(By.XPATH, "//b[text()='User account created successfully']").text
print(f"✅ {successful_login_text}")

assert "User account created successfully" in successful_login_text
print("✅ Registration verification passed: The text 'User account created successfully' appears correctly after clicking!")

driver.save_screenshot ("Registration with Register button.png")

time.sleep(2)

driver.quit()

#######################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/register")

# # # Registration with Google button :

# # 1. לחיצה על כפתור ההרשמה של גוגל
register_with_google_button = driver.find_element(By.XPATH, "//a[text()='Register with Google']")
driver.execute_script("arguments[0].click();", register_with_google_button)

time.sleep(3)

# # 2. מאתרים את שדה האימייל הריק של גוגל לפי ה-ID שלו
google_email_input = driver.find_element(By.ID, "identifierId")

# # מקלידים את המייל שלך פנימה
google_email_input.send_keys("annarubqa@gmail.com")

# # לחיצה על כפתור הבא/Next של גוגל לפי ID קשיח
continue_button = driver.find_element(By.ID, "identifierNext")
continue_button.click()

# # logout_button = driver.find_element (By.XPATH, "//button[text()= 'logout']")
# # logout_button.click()

time.sleep(2)

driver.save_screenshot ("Registration with Google button.png")

time.sleep(2)

driver.quit()

# # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/register")

# # # # Registration with LinkedIn button :

# # # # 1. לחיצה על כפתור ההרשמה של גוגל (החלפנו את button בתגית <a>)
register_with_linkedin_button = driver.find_element(By.XPATH, "//a[text()='Register with LinkedIn']")
driver.execute_script("arguments[0].click();", register_with_linkedin_button)

time.sleep(2)

driver.save_screenshot ("Registration with LinkedIn button.png")

time.sleep(2)

driver.quit()

# # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/login")

# # # # Login with Login button :

my_email = "annarubqa@gmail.com"
email_input = driver.find_element (By.ID, "email")
email_input.send_keys (my_email)

password_input = driver.find_element (By.ID, "password")
password_input.send_keys ("Ana1983ana@@")

login_submit = driver.find_element (By.XPATH, "//button[text()= 'Login']")
# # # # במקום login_submit.click()
driver.execute_script("arguments[0].click();", login_submit)

time.sleep(2)

driver.save_screenshot ("Login with Login button.png")

time.sleep(2)

driver.quit()

# # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/login")

# # # # Login with Google button :

# # # # 1. לחיצה על כפתור ההרשמה של גוגל (החלפנו את button בתגית <a>)
login_with_google_button = driver.find_element(By.XPATH, "//a[text()='Login with Google']")
driver.execute_script("arguments[0].click();", login_with_google_button)

time.sleep(3)

# # 2. מאתרים את שדה האימייל הריק של גוגל לפי ה-ID שלו
google_email_input = driver.find_element(By.ID, "identifierId")

# # מקלידים את המייל שלך פנימה
google_email_input.send_keys("annarubqa@gmail.com")

# # לחיצה על כפתור הבא/Next של גוגל לפי ID קשיח
continue_button = driver.find_element(By.ID, "identifierNext")
continue_button.click()

# # logout_button = driver.find_element (By.XPATH, "//button[text()= 'logout']")
# # logout_button.click()

time.sleep(2)

driver.save_screenshot ("Login with Google button.png")

time.sleep(2)

driver.quit()

# # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/login")

# # # Login with LinkedIn button :

# # # 1. לחיצה על כפתור ההרשמה של גוגל (החלפנו את button בתגית <a>)
login_with_linkedin_button = driver.find_element(By.XPATH, "//a[text()='Login with LinkedIn ']")
driver.execute_script("arguments[0].click();", login_with_linkedin_button)

time.sleep(2)

driver.save_screenshot ("Login with LinkedIn button.png")

time.sleep(2)

driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/register")
dynamic_number = int(time.time())


my_email = f"annarubqa+{dynamic_number}@gmail.com"

def email_input(driver, email):
    driver.find_element(By.ID, "email").send_keys(email)



def name_field (driver, name): 
    driver.find_element (By.ID, "name").send_keys (name)



def password_input (driver, password):
    driver.find_element (By.ID, "password").send_keys (password)



def confirm_Password (driver, confirmPassword): 
    driver.find_element (By.ID, "confirmPassword").send_keys (confirmPassword)



def click_register(driver):
    # 1. מאתרים את הכפתור ב-DOM ושומרים אותו למשתנה פנימי של הפונקציה
    register_button = driver.find_element(By.XPATH, "//button[text()= 'Register']")
    
    # 2. מבצעים את הלחיצה בעזרת JS ישירות על המשתנה שיצרנו
    driver.execute_script("arguments[0].click();", register_button)

# הקריאה (ההפעלה) של הפונקציה:



# # assert :

def verify_registration(driver):
    # 1. מאתרים את האלמנט, שולפים את הטקסט שלו (.text) ושומרים אותו בתוך משתנה מקומי
    text = driver.find_element(By.XPATH, "//b[text()='User account created successfully']").text
    print(f"✅ {text}")

    # 2. מבצעים את ה-Assert בתוך הפונקציה, מול המשתנה ששמרנו הרגע
    assert "User account created successfully" in text
    print("✅ Registration verification passed: The text 'User account created successfully' appears correctly after clicking!")

# 3. הקריאה (ההפעלה) של הפונקציה



def save_screenshot(driver, screenshot_name): 
    driver.save_screenshot (screenshot_name)



email_input(driver, my_email)
name_field (driver, "Anna")
password_input (driver, "Ana1983ana@@")
confirm_Password(driver, "Ana1983ana@@")
click_register(driver)
verify_registration(driver)
save_screenshot (driver, "Registration with Register button.png")


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

# # # # Registration with Google button :

# # # 1. לחיצה על כפתור ההרשמה של גוגל
def click_register(driver):
    register_with_google_button = driver.find_element(By.XPATH, "//a[text()='Register with Google']")
    driver.execute_script("arguments[0].click();", register_with_google_button)

time.sleep(3)



# # # 2. מאתרים את שדה האימייל הריק של גוגל לפי ה-ID שלו
def google_email_input (driver, email):
    driver.find_element(By.ID, "identifierId").send_keys(email)



# # # לחיצה על כפתור הבא/Next של גוגל לפי ID קשיח
def button_click (driver, continue_button):
    driver.find_element(By.ID, continue_button).click()


# # # logout_button = driver.find_element (By.XPATH, "//button[text()= 'logout']")
# # # logout_button.click()


time.sleep(2)


def save_screenshot (driver, screenshot_name):
    driver.save_screenshot (screenshot_name)


click_register(driver)
google_email_input (driver, "annarubqa@gmail.com")
button_click (driver, "identifierNext")
save_screenshot (driver, "Registration with Google button.png")


time.sleep(2)

driver.quit()

# # # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/register")

# # # # # Registration with LinkedIn button :

# # # # # 1. לחיצה על כפתור ההרשמה של גוגל (החלפנו את button בתגית <a>)
def registration_button (driver): 
    register_with_linkedin_button = driver.find_element(By.XPATH, "//a[text()='Register with LinkedIn']")
    driver.execute_script("arguments[0].click();", register_with_linkedin_button)



time.sleep(2)

def save_screenshot(driver, screenshot_name): 
    driver.save_screenshot (screenshot_name)



registration_button (driver)
save_screenshot(driver, "Registration with LinkedIn button.png")

time.sleep(2)

driver.quit()

# # # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/login")

# # # # # Login with Login button :

my_email = "annarubqa@gmail.com"
def email_input (driver, email): 
    driver.find_element (By.ID, "email").send_keys (email)



def insert_password(driver, password_input):
    driver.find_element (By.ID, "password").send_keys(password_input)



def click_login_button(driver):
    login_submit = driver.find_element (By.XPATH, "//button[text()= 'Login']")
# # # # # במקום login_submit.click()
    driver.execute_script("arguments[0].click();", login_submit)


time.sleep(2)


def execute_screenshot(driver, screenshot_name):
    driver.save_screenshot (screenshot_name)


email_input (driver, my_email)
insert_password(driver,"Ana1983ana@@")
click_login_button(driver)
time.sleep(2)    
execute_screenshot(driver, "Login with Login button.png")

time.sleep(2)

driver.quit()

# # # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/login")

# # # # # Login with Google button :

# # # # # 1. לחיצה על כפתור ההרשמה של גוגל (החלפנו את button בתגית <a>)
def click_login_button(driver):
    login_with_google_button = driver.find_element(By.XPATH, "//a[text()='Login with Google']")
    driver.execute_script("arguments[0].click();", login_with_google_button)


# time.sleep(3)

# # # 2. מאתרים את שדה האימייל הריק של גוגל לפי ה-ID שלו
def insert_email(driver, my_google):
    driver.find_element(By.ID, "identifierId").send_keys(my_google)



# # # מקלידים את המייל שלך פנימה

# # # לחיצה על כפתור הבא/Next של גוגל לפי ID קשיח
def click_button(driver, continue_button):
    driver.find_element(By.ID, continue_button).click()




# # # logout_button = driver.find_element (By.XPATH, "//button[text()= 'logout']")
# # # logout_button.click()

time.sleep(2)

def execute_screenshot(driver, screenshot_name): 
    driver.save_screenshot (screenshot_name)



click_login_button(driver)
insert_email(driver, "annarubqa@gmail.com")
click_button(driver, "identifierNext")
time.sleep(2)
execute_screenshot(driver, "Login with Google button.png")

    
time.sleep(2)

driver.quit()

# # # #####################################################################################################################################

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(90)
driver.get("https://practice.expandtesting.com/notes/app/login")

# # # # Login with LinkedIn button :

# # # # 1. לחיצה על כפתור ההרשמה של גוגל (החלפנו את button בתגית <a>)
def click_login (driver):
    login_with_linkedin_button = driver.find_element(By.XPATH, "//a[text()='Login with LinkedIn ']")
    driver.execute_script("arguments[0].click();", login_with_linkedin_button)

time.sleep(2)

def execute_screenshot(driver, screenshot_name): 
    driver.save_screenshot (screenshot_name)



click_login (driver)
time.sleep(2)
execute_screenshot(driver, "44444444_Login with LinkedIn button.png")

    
time.sleep(2)

driver.quit()

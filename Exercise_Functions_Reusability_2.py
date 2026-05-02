from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://demoqa.com/text-box")

def insert_username(driver, userName):
    driver.find_element (By.ID, "userName").send_keys (userName)



def insert_email(driver, email_box):
    driver.find_element (By.ID, "userEmail").send_keys (email_box)


def insert_current_address (driver, currentAddress):
    driver.find_element (By.ID, "currentAddress").send_keys (currentAddress)



def insert_permanent_address (driver, permanentAddress):
    driver.find_element (By.ID, "permanentAddress").send_keys (permanentAddress)



def click_submit_button (driver, submit):
    driver.find_element (By.ID, submit).click()


# assertions :

# full name assertions :
def verify_username (driver):
    text = driver.find_element (By.ID, "name").text
    print(f"✅ {text}")

    assert "Anna Rubenchik" in text
    print("✅ User full name created")


def verify_user_email(driver):
    text = driver.find_element (By.ID, "email").text
    print(f"✅ {text}")

    assert "annarubqa@gmail.com" in text
    print ("✅ User Email created")


def verify_current_address(output_element):
    # החיפוש מתבצע בתוך האלמנט שקיבלנו, ולא בכל הדף
    text = output_element.find_element(By.ID, "currentAddress").text
    print(f"✅ {text}")

    assert "Mahal 89 street, Tel Aviv city." in text 
    print("✅ User current address created")

def verify_permanent_address(output_element):
    text = output_element.find_element(By.ID, "permanentAddress").text
    print(f"✅ {text}")

    assert "Mahal 89 street, Tel Aviv city." in text 
    # תיקנתי פה את ההדפסה למשפט הצלחה הגיוני
    print("✅ User permanent address created")



insert_username(driver, "Anna Rubenchik")
insert_email(driver, "annarubqa@gmail.com")
insert_current_address (driver, "Mahal 89 street, Tel Aviv city.")
insert_permanent_address (driver, "Mahal 89 street, Tel Aviv city.")
click_submit_button (driver, "submit")
verify_username (driver)
verify_user_email(driver)

# אחרי הלחיצה על Submit (כשהתוצאות מופיעות על המסך):

# א. מגדירים את המשתנה ומאתרים את כל בלוק התוצאות מה-DOM
output_box = driver.find_element(By.ID, "output")

# ב. קוראים לפונקציות ומעבירים אליהן את המשתנה שיצרנו הרגע
verify_current_address(output_box)
verify_permanent_address(output_box)


time.sleep(2)

driver.quit()
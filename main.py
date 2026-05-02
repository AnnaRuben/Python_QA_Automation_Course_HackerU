from selenium import webdriver
# import time

# 1. אתחול מופע של דפדפן
driver = webdriver.Chrome()

# 2. פעולה: ניווט לכתובת
driver.get("https://www.google.com")

print(driver.title)

driver.quit()

# 3. השהייה קצרה כדי שתוכלי לראות את הדפדפן פתוח
# time.sleep(10)
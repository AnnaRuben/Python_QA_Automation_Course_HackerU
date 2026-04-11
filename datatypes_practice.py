#browser_name = "Chrome"

#max_retries = 3

#is_test_passed = True
########################
#browser_name = "Chrome"
#print(browser_name)

#max_retries = 3
#print(max_retries)

#is_test_passed = True
#print(is_test_passed)
#######################
#page_title = "Welcome to our store"
#error_message = 'Invalid password'

#status_code = 200
#items_in_cart = 5

#product_price = 49.99
#load_time_seconds = 1.5

#is_button_enabled = True
#is_error_displayed = False

#page_title = "Welcome to our store"
#print(type(page_title))

#status_code = 200
#print(type(status_code))

#product_price = 49.99
#print(type(product_price))

#is_button_enabled = True
#print(type(is_button_enabled))
##################################
#item_price_from_ui = "50"

#shipping_cost = 10

#real_price = int(item_price_from_ui)

#total_cost = real_price + shipping_cost

#print(total_cost)
#########################################
#item_price_from_ui = "19.99"

#real_price = float(item_price_from_ui)

#shipping_cost = 10

#total_cost = real_price + shipping_cost

#print(total_cost)
#########################################
#price_from_ui = "$50"

#price_from_ui.replace("$", "") 

#print(price_from_ui)

#price_from_ui = price_from_ui.replace("$", "")

#print(price_from_ui)
###################################################
#total_price = 100 + 20
#print(total_price)

#discounted_price = 50 - 15
#print(discounted_price)

#tax = 100 * 0.17
#print(tax)

#price_per_item = 100 / 4
#print(price_per_item)

#print(1+2)
##############################

# --- תרגיל מסכם: טסט עגלת קניות ---

# 1. יצירת משתנה (Variables & Data Types)
# צרי משתנה בשם product_name שיחזיק את המחרוזת (String) "Laptop"
# כתבי את הקוד שלך כאן מתחת:

# 2. צרי משתנה בשם is_in_stock שיחזיק את הערך הבוליאני של אמת (True) - זכרי אות ראשונה גדולה!
# כתבי את הקוד שלך כאן מתחת:

# 3. המרת טיפוסים (Casting) של מספר שלם
# הנה נתון (כמות) ששלפנו מה-UI של האתר והגיע כטקסט:

# צרי משתנה חדש בשם real_quantity, ותבצעי עליו המרה (Casting) של ui_quantity למספר שלם.
# כתבי את הקוד שלך כאן מתחת:

# 4. השתנות (Mutability) 
# הנה מחיר ששלפנו מה-UI והגיע כטקסט עם סימן של דולר:

# בגלל שסטרינג הוא Immutable, השתמשי בפקודת הניקוי replace("$", "") על המשתנה ui_price, 
# ותדאגי *לדרוס* את התווית המקורית כדי לשמור את האובייקט הנקי שנוצר!
# כתבי את הקוד שלך כאן מתחת:

# 5. המרה למספר עשרוני (Casting)
# צרי משתנה חדש בשם final_price, ותבצעי בו המרה (Casting) של ui_price הנקי למספר עשרוני.
# כתבי את הקוד שלך כאן מתחת:

# 6. בדיקת סוג נתון (type) והדפסה (print)
# כדי להוכיח שההמרות הצליחו, הדפיסי למסך את סוג הנתון (type) של המשתנה real_quantity
# כתבי את הקוד שלך כאן מתחת:

# 7. הדפיסי למסך את סוג הנתון (type) של המשתנה final_price
# כתבי את הקוד שלך כאן מתחת:

#product_name = "Laptop"
#is_in_stock = True
#ui_quantity = "3"
#real_quantity = int(ui_quantity)
#ui_price = "$120.50"
#ui_price = ui_price.replace("$", "")
#final_price = float(ui_price)
#print(type(real_quantity))
#print(type(final_price))
####################################################

# --- תרגיל רמה 2: טסט למערכת הזמנת טיסות ---

# חלק 1: יצירת משתנים
# 1. צרי משתנה בשם is_direct_flight ושימי בו ערך בוליאני שאומר "שקר" (שימי לב לאותיות!).
# כתבי את הקוד שלך כאן מתחת:

# חלק 2: חשיבה עצמאית על Casting
# שלפנו מהאתר כמות של כרטיסי טיסה שהלקוח בחר:

# 2. צרי משתנה בשם real_tickets, ותעשי המרה (Casting) ל-ui_tickets. 
# האתגר: תחליטי לבד לאיזה סוג נתון ממירים כמות של אנשים (int או float?), ותכתבי את הפקודה הנכונה.
# כתבי את הקוד שלך כאן מתחת:

# חלק 3: אתגר הדיבאג (איתור שגיאות) - Mutability
# מפתח ג'וניור בצוות ניסה לנקות את המחיר ולהמיר אותו, אבל הקוד שלו יקרוס כשירוץ!
# הנה הקוד השגוי שלו:
# ui_price = "$499.99"
# ui_price.replace("$", "")
# final_price = float(ui_price)

# 3. הראי לג'וניור איך עושים את זה נכון! כתבי מחדש את שלושת השורות האלו 
# כך שהדולר באמת ינוקה מהמשתנה (תזכרי מה קורה כשהאובייקט הוא Immutable) וההמרות יעבדו.
# כתבי את הקוד המתוקן שלך כאן מתחת:

# חלק 4: הוכחה
# 4. הדפיסי למסך את סוג הנתון (type) של המשתנה real_tickets
# כתבי את הקוד שלך כאן מתחת:

# 5. הדפיסי למסך את סוג הנתון (type) של המשתנה final_price 
# כתבי את הקוד שלך כאן מתחת:

is_direct_flight = False
ui_tickets = "5"
real_tickets = int(ui_tickets)
ui_price = "$499.99"
ui_price = ui_price.replace("$","")
final_price = float(ui_price)
print(type(real_tickets))
print(type(final_price))
#################################################################

# --- תרגיל רמה 3 (Boss Level): טסט לפיצ'ר "סיכום תיק חכם" ---

# חלק 1: סוגי נתונים והמרה מתוך ה-UI
# המערכת סרקה את התיק הרפואי והחזירה את הגיל של המטופלת כטקסט:

# 1. צרי משתנה בשם real_age, ותמירי אליו את הגיל בצורה נכונה. 
# (עלייך להחליט לבד איזה סוג נתון מתאים לגיל, ולכתוב את ההמרה המתאימה).
# כתבי את הקוד שלך כאן מתחת:

# 2. צרי משתנה בשם is_summary_ready ושימי בו ערך בוליאני שאומר "אמת".
# כתבי את הקוד שלך כאן מתחת:

# חלק 2: המלכודת של ראיונות העבודה (Mutability)
# שלפנו מהמערכת את עלות הטיפול הכוללת. היא מגיעה כטקסט עם סמל של שקלים:

# הפעם, במקום לדרוס את התווית, מתכנת אחר בצוות כתב קוד שמנקה את הסמל 
# ושומר את התוצאה בתוך משתנה *חדש* לגמרי:

# ומיד לאחר מכן ביצע המרה תקינה כדי שנוכל לבדוק את המחיר:

# 3. אתגר חשיבה (לענות מהראש בלבד, בלי קורסור!):
# המראיין מסתכל עלייך ושואל: "אם נכתוב עכשיו את הפקודה print(ui_total_cost), מה בדיוק יודפס על המסך?"
# תכתבי לי כאן למטה בהערה (עם #) מה יודפס, ותסבירי במשפט אחד *למה* זה מה שיודפס 
# תוך שימוש בחומר שלמדנו על Immutable.
# התשובה שלך:

# חלק 3: ייעול קוד והבנת הזיכרון (DRY)
# בסוף הטסט, אנחנו צריכים להדפיס למסך את סוג הנתון (type) של הגיל כדי לוודא שלא איבדנו אותו.
# מפתח מתחיל כתב את שתי השורות האלו כדי להדפיס את זה:
# age_for_print = int(ui_patient_age)
# print(type(age_for_print))

# 4. בהסתמך על מה שכבר עשית בשאלה 1 למעלה, איך היית כותבת את זה עכשיו 
# בשורת קוד אחת בלבד, נקייה ובלי כפילויות של המרות?
# כתבי את הקוד המתוקן שלך כאן מתחת:

ui_patient_age = "42"
real_age = int(ui_patient_age)
is_summary_ready = True
ui_total_cost = "₪1250.50"
clean_cost = ui_total_cost.replace("₪", "")
final_cost = float(clean_cost)
print(ui_total_cost)


















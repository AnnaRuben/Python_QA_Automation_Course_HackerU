# def say_hello():
#     print("hello")
    
# say_hello()






# def print_my_name():
#     print("Anna")
# print_my_name()


# def my_fav_country():
#     print("USA")
# my_fav_country()


# def my_web_project_and_my_mobile_project():
#     print("Shufersal_Online_and_Rami_Levi")
# my_web_project_and_my_mobile_project()







# def say_hello(name):
#     print("hello", name)
# say_hello("David")




# def say_hello(name):
#     print("hello my name is :", name)
# say_hello("Anna")





# def say_hello(name):
#     print("hello my name is :", name)
# say_hello(3)





# def say_hello(patient_id):
#     print("patient id is :", patient_id)
# say_hello(306116485)




# def say_goodby(patient_name):
#     print("im so sorry ,but we need to say goodby", patient_name)
# say_goodby("Anna")



# def check_patient_id(patient_id):
#     print("check_patient_id", patient_id)
# check_patient_id(306116485)
# check_patient_id(306116486)
# check_patient_id(306116487)




# def check_patient_id(patient_id):
#     print("check_patient_id", patient_id)
# check_patient_id(306116485, 306116486, 306116487)



# # 1. הגדרת המפעל (הפונקציה)
# def check_patient_ids(patients_list):
#     # הלולאה עוברת על הקופסה הגדולה ומוציאה כל פעם תעודת זהות אחת
#     for patient_id in patients_list:
#         print("check_patient_id", patient_id)

# # 2. הפעלת המפעל ושליחת הנתונים
# check_patient_ids([306116485, 306116486, 306116487])






# def say_goodby(patient_name):
#     print("im so sorry ,but we need to say goodby", patient_name)

# say_goodby("Anna")
# say_goodby("Moshe")
# say_goodby("Rachel")




# def say_hello(first_name, last_name, phone_number):
#     print("hello", first_name, "your last name", last_name, "and your phone number is", phone_number)
# say_hello("david", "smith", "0502345592")



# def customer_details(first_name, last_name, phone_number):
#     print("customer_details: first_name", first_name, "last name:", last_name, "phone_number:", phone_number)
# customer_details("david,", "smith,", "0502345592.")




# def add_two_numbers(a,b):
#     print(a+b)
# add_two_numbers(3,4)


# def say_hello(first_name, last_name):
#     print("hello", first_name, "your last name", last_name)
# say_hello("Anna", "Rubenchik")





# def minus_number(a,b):
#     print(a-b)
# minus_number(4,3)





# def multiply_float(a,b,c):
#     print(a*b*c)
# multiply_float(1.1, 2.2, 3.3)



# Write a program that:
# 1. Has a list of student grades:
# student_grades = [95, 70, 82, 60, 48, 100, 73]
# 2. Create a function called check_grade(grade)
# that:
# If grade ≥ 90 → print "Excellent"
# If grade ≥ 70 and < 90 → print "Good"
# If grade ≥ 60 and < 70 → print "Pass"
# Else → print "Fail“
# 3. Use a for loop to go through all grades and
# call the function for each one.

# student_grades = [95, 70, 82, 60, 48, 100, 73]
# check_grade(grade)



# student_grades = [95, 70, 82, 60, 48, 100, 73]
# def check_grade(grade):
#     if grade >= 90:
#         print("Excellent")
#     elif grade >= 70 and grade <= 90: 
#         print("Good") 
#     elif grade >= 60 and grade <= 70: 
#         print ("Pass")
#     else:
#         print("Fail")

# for i in student_grades:
#     check_grade(i)




# def check_grade(grade):
#     if grade >= 90:
#         print("Excellent")
#     elif grade >= 70 and grade < 90:
#         print("Good")
#     elif grade >= 60 and grade < 70:
#         print("Pass")
#     else:
#         print("Fail")






# def check_grade(grade):
#     print("grade", check_grade)
# check_grade ([95, 70, 82, 60, 48, 100, 73])







# def check_grade(grade):
#     # הלולאה עוברת על כל ציון בתוך הרשימה
#     for student_grade in grade:
#         print(f"Grade: {student_grade}")
        
#         # כל התנאים מוזחים פנימה כדי שיתבצעו *בתוך* הלולאה
#         # ואנחנו בודקים את המשתנה הבודד 'student_grade'
#         if student_grade >= 90:
#             print ("Excellent")
#         elif student_grade >= 70 and student_grade < 90:
#             print ("Good")
#         elif student_grade >= 60 and student_grade < 70:
#             print ("Pass")
#         else:
#             print("Fail")
#         print("---") # קו מפריד כדי שיהיה נוח לקרוא בטרמינל

# check_grade([95, 70, 82, 60, 48, 100, 73])





# # 1. הגדרת המפעל (הפונקציה)
# def check_patient_ids(patients_list):
#     # הלולאה עוברת על הקופסה הגדולה ומוציאה כל פעם תעודת זהות אחת
#     for patient_id in patients_list:
#         print("check_patient_id", patient_id)

# # 2. הפעלת המפעל ושליחת הנתונים
# check_patient_ids([306116485, 306116486, 306116487])





# # 1. הנתונים שלנו (Test Data)
# student_grades = [95, 70, 82, 60, 48, 100, 73]

# # 2. מכונת הבדיקה שלנו שתדע לבדוק ציון אחד בכל פעם (The Test Case)
# def check_grade(grade):
#     if grade >= 90:
#         print("Excellent")
#     elif grade >= 70 and grade < 90:
#         print("Good")
#     elif grade >= 60 and grade < 70:
#         print("Pass")
#     else:
#         print("Fail")

# # # 3. מריץ הבדיקות האוטומטי - שולף ציון ושולח למכונה, שולף ציון ושולח למכונה...
# for current_grade in student_grades:
#     check_grade(current_grade)






# Check numbers above or below 50
# numbers = [12, 55, 76, 44, 3, 99, 61]
# Create a function that:
# If number > 50 → print "Bigger than 50"
# If number = 50 print "Equal to 50"
# Else → print "Smaller than 50"
# Use a for loop to go through the list and call the function for each number



# numbers = [12, 55, 76, 44, 3, 99, 61]
# def check_number(number):
#     if number>50:
#         print("Bigger than 50")
#     elif number==50:
#         print("Equal to 50")
#     else:
#         print("Smaller than 50")

# for i in numbers:
#     check_number(i)






# Four siblings: Sunny, Mary, Katy, and John were arguing about who is the oldest.
# Here’s what they said:
# •Sunny is older than Mary
# •John is younger than Katy
# •Mary is older than John
# •Katy is NOT the oldest
# Your Task
# Use the clues to determine the order from oldest → youngest, put them inside a list in the correct order, and then use a function + for loop to print them.


# # 1. יוצרים את הרשימה לפי הסדר מהמבוגר לצעיר
# siblings = ["Sunny", "Katy", "Mary", "John"]

# # 2. מגדירים פונקציה שמקבלת רשימה
# def show_oldest_to_youngest(names_list):
#     # 3. לולאת for שעוברת על כל שם ומדפיסה
#     for name in names_list:
#         print(name)

# # קוראים לפונקציה (Call) עם הרשימה שלנו
# show_oldest_to_youngest(siblings)







# def get_discount_price(price):
#     return price * 0.9  # מחזיר את המחיר אחרי 10% הנחה

# # עכשיו אני יכול לשמור את התוצאה במשתנה ולהשתמש בה בטסט
# final_price = get_discount_price(200)
# if final_price < 250:
#     print("Test Passed: Discount applied correctly")





# def open_browser(browser_type="Chrome"): # הגדרנו ברירת מחדל
#     print(f"Opening {browser_type} browser...")

# open_browser()           # יפתח כרום אוטומטית
# open_browser("Firefox")  # יפתח פיירפוקס כי ביקשנו במיוחד






















# .1כתבו פונקציה שנקראת print_my_name() 
# בתוכה, הכניסו פקודת print שמדפיסה את השם שלכם.
# .2 כתבו פונקציה שתדפיס מדינה בעולם שהייתם רוצים לטוס אליה.
# 3. כתבו פונקציה שתדפיס את השם של אפליקציית ה  web –וה-  mobile מהפרויקטים שלכם.

# def print_my_name():
#     print("My name is Anna")

# print_my_name()

# def my_fav_country():
#     print("I loveeeee USA")

# my_fav_country()

# def my_web_and_mobile_projects():
#     print("my web and mobile projects are Shufersal and Rami levi")

# my_web_and_mobile_projects()







# def add_first_name_to_last_name(first_name, last_name):
#     print(f"Hello {first_name} {last_name}")

# add_first_name_to_last_name("Anna", "Rubenchik")

# def minus_number(a, b):
#     print(a-b)

# minus_number(2, 1)

# def multiply_function(a, b, c):
#     print(a*b*c)

# multiply_function(1.1, 2.2, 3.3)








# Write a program that:

#     1. Has a list of student grades:

#     student_grades = [95, 70, 82, 60, 48, 100, 73]

#     2. Create a function called check_grade(grade)

# that:

#     If grade ≥ 90 → print "Excellent"

#     If grade ≥ 70 and < 90 → print "Good"

#     If grade ≥ 60 and < 70 → print "Pass"

#     Else → print "Fail“

#     3. Use a for loop to go through all grades and

#     call the function for each one.

# student_grades = [95, 70, 82, 60, 48, 100, 73]

# def check_grade(grade):
#     if grade >= 90:
#         print("Excellent")
#     elif grade >= 70 and grade < 90:
#         print("Good")
#     elif grade >= 60 and grade < 70:
#          print ("Pass")
#     else:
#         print("Fail")
    
# for i in student_grades:
#     check_grade (i)









# Check numbers above or below 50

# numbers = [12, 55, 76, 44, 3, 99, 61]

# Create a function that:

# If number > 50 → print "Bigger than 50"

# If number = 50 print "Equal to 50"

# Else → print "Smaller than 50"

# Use a for loop to go through the list and call the function for each number

# numbers = [12, 55, 76, 44, 3, 99, 61]
# def above_or_below (number):
#     if number > 50:
#         print("Bigger than 50")
#     elif number == 50:
#         print("Equal to 50")
#     else:
#         print("Smaller than 50")

# for i in numbers:
#     above_or_below (i) 








# Four siblings: Sunny, Mary, Katy, and John were arguing about who is the oldest.

# Here’s what they said:

# •Sunny is older than Mary

# •John is younger than Katy

# •Mary is older than John

# •Katy is NOT the oldest

# Your Task

# Use the clues to determine the order from oldest → youngest, put them inside a list in the correct order, and then use a function + for loop to print them.

# siblings = ["Sunny", "Katy", "Mary", "John"]
# def from_oldest_to_youngest(sibling):
#     print(sibling)

# for i in siblings:
#         from_oldest_to_youngest (i)






    


















    





























































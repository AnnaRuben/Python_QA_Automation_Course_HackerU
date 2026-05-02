# class dog:

#     def bark(self):
#         print("woof!")

# dog1 = dog()
# dog1.bark()





# class dog:

#     def bark(self):
#         print("woof!")

#     def pet_me(self):
#         print("Pet your dog")

# dog1 = dog()
# dog1.bark()
# dog1.pet_me()







# class WildAnimal:
#         def sound(self):
#             print("Animal makes a sound")
#         def eat(self):
#             print("Animal is eating")

# WildAnimal1 = WildAnimal()
# WildAnimal1.sound()
# WildAnimal1.eat()






# Instructions:

# 1.Create a class called Phone.

# 2.Add two methods:

# • call() → prints: "Calling..."

# • hang_up() → prints: "Call ended"

# 3.Create an object and call both methods.

# class Phone:
#     def call(self):
#         print("Calling...")
#     def hang_up(self):
#         print("Call ended")

# Phone1=Phone()
# Phone1.call()
# Phone1.hang_up()







# Instructions:
# 1.Create a class named Calculator.
# 2. Add three methods:
# • add(self, num1, num2) → prints the result of addition.
# • subtract(self, num1, num2) → prints the result of subtraction
# • multiply(self, num1, num2) → prints the result of multiplication
# 3. Create one object of the class.
# 4. Use the object to call all three methods with numbers of your choice.


# class Calculator:

#         def add(self, num1, num2):
#             print(num1+num2) 
#         def multiply(self, num1, num2):
#             print(num1*num2)

# Calculator1=Calculator()
# Calculator1.add(1, 2)
# Calculator1.multiply(1, 2)








# Instructions:

# 1.Create a class called BankActions.

# 2.Inside the class, create three methods:

# •deposit(amount) → prints: "You deposited: X"

# •withdraw(amount) → prints: "You withdrew: X"

# •check_balance(balance) → prints: "Your balance is: X"

# 3.Create one object of the class.

# 4.Call all three methods using different numbers.

# class BankActions:
#         def deposit(self, amount):
#             print("You deposited:", amount)
#         def withdraw(self, amount):
#             print("You withdrew:", amount)
#         def check_balance(self, balance):
#             print("Your balance is:", balance)

# BankActions1=BankActions()
# BankActions1.deposit(1000)
# BankActions1.withdraw(100)
# BankActions1.check_balance(900)








# Create a class called Student.

# 1. Inside the class, write an __init__ method that receives:

# • name

# • age

# 2. Store these values as attributes.

# 3. Add a method called introduce() that prints:

# Hi, my name is <name> and I am <age> years old

# 4. Create two different Student objects with different names and ages.

# 5. Call the introduce() method for both objects.



# class Student:
#     def __init__(self, name, age):
#         self.name=name
#         self.age=age
#     def introduce(self):
#         print(f"Hi, my name is {self.name} and I am {self.age} years old")


# girl1=Student("Anna", 35)
# boy2=Student("Ohad", 50)
# girl1.introduce()
# boy2.introduce()






# Instructions:
# Create a class called Student.
# Inside the class:
# 1. Create an __init__ method that receives:
# • name
# • grade (number)
# 2. Create a method called check_status():
# • If grade is 60 or higher → print:
# "NAME passed the course"
# • Otherwise → print:
# "NAME failed the course"
# Create two students with different grades and call check_status() for each one.


# class Student:
#     def __init__(self, name, grade):
#         self.name=name
#         self.grade=grade
#     def check_status(self):
#         if self.grade >=60:
#             print(f"{self.name} passed the course")
#         else:
#             print(f"{self.name} failed the course")

# girl1=Student("Anna", 100)
# boy2=Student("Ohad", 50)
# girl1.check_status()
# boy2.check_status()







# Create a class BankAccount
# • __init__(balance)
# • deposit(deposit_amount) → adds to balance
# • withdraw(withdraw_amount) → use “if” if not enough money
# • show_balance()
# Create one object and call all methods.
# •
# Make sure balance keeps updating when necessary

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit (self, deposit_amount):
#         self.balance = self.balance + deposit_amount
#         print(self.balance)

#     def withdraw (self, withdraw_amount):
        
#         if withdraw_amount > self.balance:
#             print("Not enough money")
#         else:
#             self.balance = self.balance - withdraw_amount
#             print("Money trancefered ssucceful")

# user1 = BankAccount(1000)
# user1.deposit(100)






















# class Dog:

#     def bark(self):
#         print("Woof!")

#     def wiggle(self):
#         print("dog wiggles")

# dog1 = Dog()
# dog1.bark()

# dog2 = Dog()
# dog2.wiggle()
# dog2.bark()






# Instructions:

# 1.Create a class called WildAnimal.

# 2.Inside it, create two methods:

# • sound() → prints: "Animal makes a sound"

# • eat() → prints: "Animal is eating"

# 3.Create an object and call both methods.

# class WildAnimal:

#     def sound(self):
#         print("Animal makes a sound")
#     def eat(self):
#         print("Animal is eating")

# WildAnimal = WildAnimal()
# WildAnimal.sound()
# WildAnimal.eat()





# Instructions:

# 1.Create a class called Phone.

# 2.Add two methods:

# • call() → prints: "Calling..."

# • hang_up() → prints: "Call ended"

# 3.Create an object and call both methods.

# class Phone:
#     def call(self):
#         print("Calling...")

#     def hang_up(self):
#         print("Call ended")

# my_phone = Phone()
# my_phone.call()
# my_phone.hang_up()






# Instructions:

# 1.Create a class named Calculator.

# 2. Add three methods:

# • add(self, num1, num2) → prints the result of addition.

# • subtract(self, num1, num2) → prints the result of subtraction

# • multiply(self, num1, num2) → prints the result of multiplication

# 3. Create one object of the class.

# 4. Use the object to call all three methods with numbers of your choice.

# class Calculator:

#     def add(self, num1, num2):
#         print(num1 + num2)
#     def subtract(self, num1, num2):
#         print(num1 - num2)
#     def multiply(self, num1, num2):
#         print(num1 * num2)

# addition = Calculator()
# addition.add(1, 2)
# addition.subtract(2, 1)
# addition.multiply(1, 2)





# Instructions:

# 1.Create a class called BankActions.

# 2.Inside the class, create three methods:

# •deposit(amount) → prints: "You deposited: X"

# •withdraw(amount) → prints: "You withdrew: X"

# •check_balance(balance) → prints: "Your balance is: X"

# 3.Create one object of the class.

# 4.Call all three methods using different numbers.

# class BankActions:
#     def deposit(self, amount):
#         print("You deposited:", amount)
#     def withdraw(self, amount):
#         print("You withdrew:", amount)
#     def check_balance(self, balance):
#         print("Your balance is:", balance)

# account_status = BankActions()
# account_status.deposit(1000)
# account_status.withdraw(100)
# account_status.check_balance(900) 







# Create a class called Student.

# 1. Inside the class, write an __init__ method that receives:

# • name

# • age

# 2. Store these values as attributes.

# 3. Add a method called introduce() that prints:

# Hi, my name is <name> and I am <age> years old

# 4. Create two different Student objects with different names and ages.

# 5. Call the introduce() method for both objects.

# class Student:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def introduce(self):
#         print(f"Hi, my name is {self.name} and I am {self.age} years old")

# girl1 = Student ("Anna" , 35)
# boy2 = Student ("Moshe" , 47)
# girl1.introduce()
# boy2.introduce()








# Instructions:

# Create a class called Student.

# Inside the class:

# 1. Create an __init__ method that receives:

# • name

# • grade (number)

# 2. Create a method called check_status():

# • If grade is 60 or higher → print:

# "NAME passed the course"

# • Otherwise → print:

# "NAME failed the course"

# Create two students with different grades and call check_status() for each one.

# class Student:
#     def __init__(self, name, grade):
#         self.name = name
#         self.grade = grade

#     def check_status(self):
#         if self.grade >= 60:
#             print(f"{self.name} passed the course", self.grade)
#         else:
#             print(f"{self.name} failed the course", self.grade)

# girl1 = Student("Anna", 100)
# boy2 = Student("Ohad", 50)
# girl1.check_status()
# boy2.check_status()






# Create a class BankAccount

# • __init__(balance)

# • deposit(deposit_amount) → adds to balance

# • withdraw(withdraw_amount) → use “if” if not enough money

# • show_balance()

# Create one object and call all methods.

# •

# Make sure balance keeps updating when necessary

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, deposit_amount):
#         self.balance = self.balance + deposit_amount

#     def withdraw(self, withdraw_amount):
#         if withdraw_amount > self.balance:
#             print("not enough money")
#         else:
#             self.balance = self.balance - withdraw_amount

#     def show_balance(self):
#         print("Your balance is:", self.balance)

# user1 = BankAccount(1000)
# user1.deposit(100)
# user1.withdraw(100)
# user1.show_balance()








# Instructions:

# 1. Create a class called GameCharacter

# 2. The class should have:

# • __init__(name, hp)

# • take_damage(amount)

# • heal(amount)

# 3.take_damage:

# • Reduces HP

# • Prints the new HP

# 4. heal:

# • Increases HP

# • Prints the new HP

# 5. Create one character

# 6. Call the methods in this order:

# • Take damage

# • Heal

# • Take damage again

# class GameCharacter:
#     def __init__(self, name, hp) :
#         self.name = name
#         self.hp = hp

#     def take_damage(self, amount):
#         self.hp = self.hp - amount 
#         print(f"{self.name} your new HP is:", self.hp)  

#     def heal(self, amount):
#         self.hp =  self.hp + amount
#         print(f"{self.name} your new HP is:", self.hp)

# one_character = GameCharacter("Anna", 1000)
# one_character.take_damage(100)
# one_character.heal(100)
# one_character.take_damage(10)












 

 

















    









      
























 

































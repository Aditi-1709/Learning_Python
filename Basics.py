
# DAY 1 :)

# Print statement syntax and it is case-sensitive.
print("Hello World")  # String in quotes
print(30+20)  # numbers not in quotes

# Variable declaration
name = "John"
age = "28"
print("Hello my name is" + name + ".I am " + age + "years old.")

# Have User Inputs
name = input("Enter is your name:")
age = input("Enter your Age:")
print("Hello my name is " + name + " and I am " + age + " years old.")

# Entering 2 numbers and printing them together
num1 = input("Enter a number :")
num2 = input("Enter a number :")
print(num1, num2)

# Concatenating 2 strings
string1 = "20"
string2 = "30"
print(string1+string2)

# Adding 2 numbers
num1 = 20
num2 = 30
print(num1+num2)

# Taking 2 number inputs and adding them
num1 = int(input("Enter a number :"))
num2 = int(input("Enter a number :"))
print(num1+num2)

# DATA TYPES :-
# Strings
# int, float (decimal) - numbers

# Math Operators
# Add +
# Subtract -
# Division /
# Multiply *
# Exponent **
# Modulo / Remainder %
# Float Division (getting whole no in division) //

# Tip Calculator App
food_amount = float(input("Enter food amount $: "))
tip_percentage = float(input("Enter your tip percentage %: ")) / 100
tip_amount = food_amount * tip_percentage

total = food_amount + tip_amount
print("\n")
print("-----------------------------------------------")
print(f'🌮 Food Amount : ${food_amount}')
print(f'💵 Tip Amount : ${tip_amount}')
print("\n")
print(f'🤑 Total Amount : ${total}')
print("-----------------------------------------------")

# If I want to print '$' sign in front of the total money I've convert total from float to str
# print('$' + str(total))  # type conversion

# Type Conversion Methods
# anything to int - int()
# anything to str - str()
# anything to float - float()

# BOOLEAN
# TRUE / FALSE

# Baby Weather App

weather = 'rain'

if weather == 'rainy' or 'Rainy':
    print('Take your Umbrella ☔')

elif weather == 'cloudy' or 'Cloudy':
    print("⛅")

else:
    print("Take your sunglasses 😎")

# Comparison Operators ( ==, < , >, <= , >= )

#Exercises: Level 1
"""
1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.

2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.

3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3
"""

#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:
user_age = int(input("Enter your age:"))
for_underage = 18 - user_age

if user_age >= 18:
  print("You are old enough to learn to drive.")
else:
  print(f"You need {for_underage} more years to learn to drive.")

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age = int(input("Enter my age:"))
your_age = int(input("Enter your age:"))
# age difference
age_difference = abs(my_age - your_age)
#check if it is a year or years older 
unit = "years" if age_difference > 1 else "year"

if my_age == your_age:
  print("We're the same age")

if my_age > your_age:
  print(f"I'm {age_difference} {unit} older than you")

if my_age < your_age:
  print(f"You're {age_difference} {unit} older than me")

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
first_num = int(float(input("Enter 1st number:")))
second_num = int(float(input("Enter 2nd number:")))
nums = first_num - second_num

if nums == 0:
  print(f"{first_num} is equal to {second_num}")
if nums > 0:
  print(f"{first_num} is greater than {second_num}")
if nums < 0:
  print(f"{first_num} is less than {second_num}")

#Exercises: Level 2
"""
1. Write a code which gives grade to students according to theirs scores:
80-100, A
70-89, B
60-69, C
50-59, D
0-49, F
2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
3. The following list contains some fruits:
```sh
fruits = ['banana', 'orange', 'mango', 'lemon']
```
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
"""

#1. Write a code which gives grade to students according to theirs scores:
student_grade = int(input("Enter my grade:"))

if 80 <= student_grade <= 100:
  print("A")
if 70 <= student_grade <= 89:
  print("B")
if 60 <= student_grade <= 69:
  print("C")
if 50 <= student_grade <= 59:
  print("D")
if 0 <= student_grade <= 49:
  print("F")

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. 
# December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
month = input("Enter the month:").strip().capitalize()

#Seasons
autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]
summer = ["June", "July" , "August"]

if month in autumn:
  print("Autumn")
  exit()

if month in winter:
  print("winter")
  exit()

if month in spring:
  print("spring")
  exit()

if month in summer:
  print("summer")
  exit()

print("This is not a month or you misspelled it")

#3. The following list contains some fruits:
fruits = ["banana", "orange", "mango", "lemon"]
"""
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
If the fruit exists print('That fruit already exist in the list')
"""
fruit = input("Enter the fruit:").strip().lower()

if fruit not in fruits:
  print(fruits.append(fruit))
else:
  print("That fruit already exist in the list")

#Exercises: Level 3
"""
1. Here we have a person dictionary. Feel free to modify it!
        person={
    'first_name': 'Fracis Leo',
    'last_name': 'Marcos',
    'age': 69,
    'country': 'Biringan',
    'is_marred': True,
    'skills': ['Scammer', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, 
 print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:(skip)
"""
#1. 1. Here we have a person dictionary. Feel free to modify it!
person={
    'first_name': 'Fracis Leo',
    'last_name': 'Marcos',
    'age': 69,
    'country': 'Biringan',
    'is_marred': True,
    'skills': ['Scammer', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if 'skills' key exists and print the middle skill
if "skills" in person:
    skills = person["skills"]
    middle_index = len(skills) // 2
    print(f"Middle skill: {skills[middle_index]}")
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# Check if the person has 'Python' skill
if "skills" in person and "Python" in person["skills"]:
    print("Python skill found.")
else:
    print("Python skill NOT found.")
#If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, 
#print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
#else print('unknown title') - for more accurate results more conditions can be nested!
skills = person["skills"]

# Frontend developer -> EXACTLY JavaScript + React
if set(skills) == {"JavaScript", "React"}:
    print("He is a front end developer")
    exit()

# Backend developer -> MUST have Node + Python + MongoDB
if {"Node", "Python", "MongoDB"}.issubset(skills):
    print("He is a backend developer")
    exit()

# Fullstack developer -> MUST have React + Node + MongoDB
if {"React", "Node", "MongoDB"}.issubset(skills):
    print("He is a fullstack developer")
    exit()

# If none matched
print("unknown title")

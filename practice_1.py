# Python Basics for Beginners - Variable Types and Examples
# This file contains examples for teaching basic Python concepts

print("=" * 50)
print("WELCOME TO PYTHON BASICS!")
print("=" * 50)

# =============================================================================
# LESSON 1: BASIC VARIABLE TYPES
# =============================================================================

print("\n📚 LESSON 1: BASIC VARIABLE TYPES")
print("-" * 40)

# 1. STRINGS - Text data
print("\n🔤 STRINGS (Text Data):")
print("-" * 20)

# Creating strings
student_name = "Alice"
course_name = "Python Programming"
greeting = "Hello, World!"

print(f"Student name: {student_name}")
print(f"Course: {course_name}")
print(f"Greeting: {greeting}")

# String operations
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name  # Concatenation
print(f"Full name: {full_name}")

# String methods
message = "hello world"
print(f"Original: {message}")
print(f"Uppercase: {message.upper()}")
print(f"Capitalize: {message.capitalize()}")
print(f"Length: {len(message)} characters")

# 2. NUMBERS - Integer and Float
print("\n🔢 NUMBERS:")
print("-" * 15)

# Integers (whole numbers)
age = 20
number_of_students = 25
temperature = -5

print(f"Age: {age}")
print(f"Number of students: {number_of_students}")
print(f"Temperature: {temperature}°C")

# Floats (decimal numbers)
height = 5.6
price = 19.99
pi = 3.14159

print(f"Height: {height} feet")
print(f"Price: ${price}")
print(f"Pi: {pi}")

# Math operations
a = 10
b = 3
print(f"\nMath Operations:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} ** {b} = {a ** b}")  # Power
print(f"{a} % {b} = {a % b}")   # Remainder

# 3. BOOLEANS - True/False values
print("\n✅ BOOLEANS (True/False):")
print("-" * 25)

is_student = True
is_graduated = False
has_homework = True

print(f"Is student: {is_student}")
print(f"Is graduated: {is_graduated}")
print(f"Has homework: {has_homework}")

# Boolean operations
print(f"\nBoolean Operations:")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")

# =============================================================================
# LESSON 2: DATA STRUCTURES
# =============================================================================

print("\n\n📚 LESSON 2: DATA STRUCTURES")
print("-" * 40)

# 1. LISTS - Ordered collections
print("\n📋 LISTS (Ordered Collections):")
print("-" * 30)

# Creating lists
fruits = ["apple", "banana", "orange", "grape"]
grades = [85, 92, 78, 96, 88]
mixed_list = ["Alice", 20, True, 3.5]

print(f"Fruits: {fruits}")
print(f"Grades: {grades}")
print(f"Mixed list: {mixed_list}")

# List operations
print(f"\nList Operations:")
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")
print(f"Number of fruits: {len(fruits)}")

# Adding items
fruits.append("strawberry")
print(f"After adding strawberry: {fruits}")

# Removing items
fruits.remove("banana")
print(f"After removing banana: {fruits}")

# 2. DICTIONARIES - Key-value pairs
print("\n📖 DICTIONARIES (Key-Value Pairs):")
print("-" * 35)

# Creating dictionaries
student_info = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

course_grades = {
    "Math": 95,
    "Science": 87,
    "English": 92
}

print(f"Student info: {student_info}")
print(f"Course grades: {course_grades}")

# Accessing dictionary values
print(f"\nDictionary Access:")
print(f"Student name: {student_info['name']}")
print(f"Math grade: {course_grades['Math']}")

# Adding new items
student_info["email"] = "alice@school.com"
print(f"After adding email: {student_info}")

# 3. TUPLES - Immutable ordered collections
print("\n📦 TUPLES (Immutable Collections):")
print("-" * 35)

# Creating tuples
coordinates = (10, 20)
colors = ("red", "green", "blue")
student_data = ("Bob", 19, "Computer Science")

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Student data: {student_data}")

# Tuple operations
print(f"\nTuple Operations:")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"Number of colors: {len(colors)}")

# =============================================================================
# LESSON 3: USER INPUT AND INTERACTION
# =============================================================================

print("\n\n📚 LESSON 3: USER INPUT AND INTERACTION")
print("-" * 45)

print("\n💬 USER INPUT EXAMPLES:")
print("-" * 25)

# Note: In a real class, you would uncomment these lines
# name = input("What's your name? ")
# age = input("How old are you? ")
# favorite_color = input("What's your favorite color? ")

# For demonstration purposes, we'll use example values
name = "Student"
age = "18"
favorite_color = "blue"

print(f"Hello, {name}!")
print(f"You are {age} years old.")
print(f"Your favorite color is {favorite_color}.")

# Converting input types
age_number = int(age)  # Convert string to integer
print(f"Next year you'll be {age_number + 1} years old.")

# =============================================================================
# LESSON 4: CONTROL FLOW (IF/ELSE STATEMENTS)
# =============================================================================

print("\n\n📚 LESSON 4: CONTROL FLOW")
print("-" * 35)

print("\n🔀 IF/ELSE STATEMENTS:")
print("-" * 25)

# Basic if/else
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}")
print(f"Grade: {grade}")

# Multiple conditions
temperature = 75
is_sunny = True

if temperature > 80 and is_sunny:
    weather_advice = "Perfect day for swimming!"
elif temperature > 60 and is_sunny:
    weather_advice = "Great day for a walk!"
elif temperature < 50:
    weather_advice = "Stay warm inside!"
else:
    weather_advice = "Check the weather before going out."

print(f"\nTemperature: {temperature}°F")
print(f"Is sunny: {is_sunny}")
print(f"Advice: {weather_advice}")

# =============================================================================
# LESSON 5: LOOPS
# =============================================================================

print("\n\n📚 LESSON 5: LOOPS")
print("-" * 25)

print("\n🔄 FOR LOOPS:")
print("-" * 15)

# For loop with lists
fruits = ["apple", "banana", "orange"]
print("Fruits in the basket:")
for fruit in fruits:
    print(f"  - {fruit}")

# For loop with range
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(f"  {i}")

# For loop with dictionaries
student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
print("\nStudent grades:")
for student, grade in student_grades.items():
    print(f"  {student}: {grade}")

print("\n🔄 WHILE LOOPS:")
print("-" * 15)

# While loop example
count = 1
print("Counting with while loop:")
while count <= 3:
    print(f"  Count: {count}")
    count += 1

# =============================================================================
# LESSON 6: FUNCTIONS
# =============================================================================

print("\n\n📚 LESSON 6: FUNCTIONS")
print("-" * 30)

print("\n🔧 BASIC FUNCTIONS:")
print("-" * 20)

# Simple function
def greet(name):
    return f"Hello, {name}! Welcome to Python!"

# Function with multiple parameters
def calculate_area(length, width):
    area = length * width
    return area

# Function with default parameters
def introduce(name, age=18, city="Unknown"):
    return f"Hi, I'm {name}, {age} years old, from {city}."

# Using functions
print(greet("Alice"))
print(f"Area of rectangle: {calculate_area(5, 3)} square units")
print(introduce("Bob"))
print(introduce("Charlie", 20, "New York"))

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n\n🎯 PRACTICAL EXAMPLES")
print("-" * 30)

print("\n📊 STUDENT GRADE CALCULATOR:")
print("-" * 30)

def calculate_grade_average(grades):
    total = sum(grades)
    average = total / len(grades)
    return average

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Example usage
student_grades = [85, 92, 78, 96, 88]
average = calculate_grade_average(student_grades)
letter_grade = get_letter_grade(average)

print(f"Grades: {student_grades}")
print(f"Average: {average:.1f}")
print(f"Letter Grade: {letter_grade}")

print("\n🛒 SIMPLE SHOPPING CART:")
print("-" * 25)

def calculate_total(items):
    total = 0
    for item, price in items.items():
        total += price
    return total

def apply_discount(total, discount_percent):
    discount_amount = total * (discount_percent / 100)
    final_total = total - discount_amount
    return final_total, discount_amount

# Example shopping cart
cart = {
    "apple": 1.50,
    "banana": 0.75,
    "orange": 2.00,
    "bread": 3.50
}

subtotal = calculate_total(cart)
final_total, discount = apply_discount(subtotal, 10)

print(f"Shopping Cart: {cart}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount (10%): ${discount:.2f}")
print(f"Final Total: ${final_total:.2f}")

print("\n" + "=" * 50)
print("🎉 CONGRATULATIONS! You've learned Python basics!")
print("=" * 50)

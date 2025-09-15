# Python Control Flow - If/Else Statements and Loops
# Perfect for teaching beginners about decision making and repetition

print("=" * 60)
print("🔄 PYTHON CONTROL FLOW - DECISIONS AND LOOPS")
print("=" * 60)

print("\n🔍 What is Control Flow?")
print("Control flow is how your program makes decisions and repeats actions!")
print("It's like giving your program a brain to think and work.")

# =============================================================================
# IF/ELSE STATEMENTS - MAKING DECISIONS
# =============================================================================

print("\n\n🔀 IF/ELSE STATEMENTS - MAKING DECISIONS")
print("-" * 50)

print("\n💡 What are If/Else Statements?")
print("If/else statements help your program make decisions!")
print("Like: 'If it's raining, bring an umbrella. Otherwise, enjoy the sun!'")

# Basic if statement
print("\n🎯 Basic If Statement:")
print("Try running this code:")
print("age = 20")
print("if age >= 18:")
print("    print('You are an adult!')")

age = 20
if age >= 18:
    print("You are an adult!")

# If/else statement
print("\n🎯 If/Else Statement:")
print("Try running this code:")
print("temperature = 75")
print("if temperature > 80:")
print("    print('It\\'s hot! Wear shorts.')")
print("else:")
print("    print('It\\'s comfortable weather.')")

temperature = 75
if temperature > 80:
    print("It's hot! Wear shorts.")
else:
    print("It's comfortable weather.")

# If/elif/else statement
print("\n🎯 If/Elif/Else Statement:")
print("Try running this code:")
print("score = 85")
print("if score >= 90:")
print("    grade = 'A'")
print("elif score >= 80:")
print("    grade = 'B'")
print("elif score >= 70:")
print("    grade = 'C'")
print("elif score >= 60:")
print("    grade = 'D'")
print("else:")
print("    grade = 'F'")
print("print(f'Your grade is {grade}')")

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
print(f"Your grade is {grade}")

# Multiple conditions
print("\n🎯 Multiple Conditions:")
print("Try running this code:")
print("age = 20")
print("has_license = True")
print("if age >= 18 and has_license:")
print("    print('You can drive!')")
print("elif age >= 16:")
print("    print('You can get a learner\\'s permit.')")
print("else:")
print("    print('You\\'re too young to drive.')")

age = 20
has_license = True
if age >= 18 and has_license:
    print("You can drive!")
elif age >= 16:
    print("You can get a learner's permit.")
else:
    print("You're too young to drive.")

# =============================================================================
# COMPARISON OPERATORS
# =============================================================================

print("\n\n⚖️ COMPARISON OPERATORS")
print("-" * 30)

print("\n🔍 Comparison Operators:")
print("These help you compare values!")

a = 10
b = 5

print(f"\nLet's compare {a} and {b}:")
print(f"{a} == {b} (equal): {a == b}")
print(f"{a} != {b} (not equal): {a != b}")
print(f"{a} > {b} (greater than): {a > b}")
print(f"{a} < {b} (less than): {a < b}")
print(f"{a} >= {b} (greater or equal): {a >= b}")
print(f"{a} <= {b} (less or equal): {a <= b}")

# String comparisons
print("\n🔤 String Comparisons:")
name1 = "Alice"
name2 = "Bob"
print(f"'{name1}' == '{name2}': {name1 == name2}")
print(f"'{name1}' < '{name2}': {name1 < name2}")  # Alphabetical order

# =============================================================================
# LOGICAL OPERATORS
# =============================================================================

print("\n\n🧠 LOGICAL OPERATORS")
print("-" * 25)

print("\n💡 Logical Operators:")
print("These help you combine conditions!")

is_student = True
has_homework = False
is_weekend = True

print(f"\nis_student = {is_student}")
print(f"has_homework = {has_homework}")
print(f"is_weekend = {is_weekend}")

print(f"\nLogical Operations:")
print(f"is_student and has_homework: {is_student and has_homework}")
print(f"is_student or has_homework: {is_student or has_homework}")
print(f"not has_homework: {not has_homework}")
print(f"is_student and not has_homework: {is_student and not has_homework}")

# =============================================================================
# FOR LOOPS - REPEATING ACTIONS
# =============================================================================

print("\n\n🔄 FOR LOOPS - REPEATING ACTIONS")
print("-" * 40)

print("\n💡 What are For Loops?")
print("For loops repeat actions for each item in a list!")
print("Like: 'For each fruit in my basket, eat it!'")

# For loop with lists
print("\n🎯 For Loop with Lists:")
print("Try running this code:")
print("fruits = ['apple', 'banana', 'orange']")
print("for fruit in fruits:")
print("    print(f'I like {fruit}!')")

fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"I like {fruit}!")

# For loop with range
print("\n🎯 For Loop with Range:")
print("Try running this code:")
print("for i in range(5):")
print("    print(f'Count: {i}')")

for i in range(5):
    print(f"Count: {i}")

# For loop with range(start, stop)
print("\n🎯 For Loop with Range(start, stop):")
print("Try running this code:")
print("for i in range(1, 6):")
print("    print(f'Number: {i}')")

for i in range(1, 6):
    print(f"Number: {i}")

# For loop with range(start, stop, step)
print("\n🎯 For Loop with Range(start, stop, step):")
print("Try running this code:")
print("for i in range(0, 10, 2):")
print("    print(f'Even number: {i}')")

for i in range(0, 10, 2):
    print(f"Even number: {i}")

# For loop with dictionaries
print("\n🎯 For Loop with Dictionaries:")
print("Try running this code:")
print("student_grades = {'Alice': 95, 'Bob': 87, 'Charlie': 92}")
print("for student, grade in student_grades.items():")
print("    print(f'{student} got {grade}')")

student_grades = {"Alice": 95, "Bob": 87, "Charlie": 92}
for student, grade in student_grades.items():
    print(f"{student} got {grade}")

# =============================================================================
# WHILE LOOPS - REPEATING UNTIL CONDITION IS FALSE
# =============================================================================

print("\n\n🔄 WHILE LOOPS - REPEATING UNTIL CONDITION IS FALSE")
print("-" * 60)

print("\n💡 What are While Loops?")
print("While loops repeat actions as long as a condition is true!")
print("Like: 'While I'm hungry, keep eating!'")

# Basic while loop
print("\n🎯 Basic While Loop:")
print("Try running this code:")
print("count = 1")
print("while count <= 3:")
print("    print(f'Count: {count}')")
print("    count += 1")

count = 1
while count <= 3:
    print(f"Count: {count}")
    count += 1

# While loop with user input
print("\n🎯 While Loop with User Input:")
print("Try running this code:")
print("password = 'secret123'")
print("attempts = 0")
print("while attempts < 3:")
print("    guess = input('Enter password: ')")
print("    if guess == password:")
print("        print('Access granted!')")
print("        break")
print("    else:")
print("        print('Wrong password!')")
print("        attempts += 1")

# Simulated password check
password = "secret123"
attempts = 0
while attempts < 3:
    guess = "secret123"  # This would be: guess = input('Enter password: ')
    if guess == password:
        print("Access granted!")
        break
    else:
        print("Wrong password!")
        attempts += 1

# =============================================================================
# BREAK AND CONTINUE
# =============================================================================

print("\n\n⏹️ BREAK AND CONTINUE")
print("-" * 25)

print("\n💡 Break and Continue:")
print("Break: Stop the loop completely")
print("Continue: Skip to the next iteration")

# Break example
print("\n🎯 Break Example:")
print("Try running this code:")
print("for i in range(10):")
print("    if i == 5:")
print("        print('Found 5! Stopping.')")
print("        break")
print("    print(f'Number: {i}')")

for i in range(10):
    if i == 5:
        print("Found 5! Stopping.")
        break
    print(f"Number: {i}")

# Continue example
print("\n🎯 Continue Example:")
print("Try running this code:")
print("for i in range(5):")
print("    if i == 2:")
print("        print('Skipping 2!')")
print("        continue")
print("    print(f'Number: {i}')")

for i in range(5):
    if i == 2:
        print("Skipping 2!")
        continue
    print(f"Number: {i}")

# =============================================================================
# NESTED LOOPS
# =============================================================================

print("\n\n🔄 NESTED LOOPS")
print("-" * 20)

print("\n💡 Nested Loops:")
print("Loops inside other loops!")
print("Like: 'For each row, for each column, print a star!'")

# Nested for loops
print("\n🎯 Nested For Loops:")
print("Try running this code:")
print("for row in range(3):")
print("    for col in range(3):")
print("        print(f'({row}, {col})', end=' ')")
print("    print()  # New line after each row")

for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end=" ")
    print()  # New line after each row

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n\n🎯 PRACTICAL EXAMPLES")
print("-" * 30)

print("\n📊 Grade Calculator with Loops:")
print("Try running this code:")

def grade_calculator():
    subjects = ["Math", "Science", "English", "History"]
    grades = []
    
    for subject in subjects:
        grade = int(input(f"Enter {subject} grade: "))
        grades.append(grade)
    
    average = sum(grades) / len(grades)
    print(f"Your average grade is: {average:.1f}")
    
    if average >= 90:
        print("Excellent work! 🎉")
    elif average >= 80:
        print("Good job! 👍")
    elif average >= 70:
        print("Keep trying! 💪")
    else:
        print("You can do better! 📚")

print("\n🎮 Number Guessing Game:")
print("Try running this code:")

def number_guessing_game():
    import random
    secret_number = random.randint(1, 10)
    attempts = 0
    
    print("I'm thinking of a number between 1 and 10...")
    
    while True:
        guess = int(input("Guess the number: "))
        attempts += 1
        
        if guess == secret_number:
            print(f"🎉 Correct! You guessed it in {attempts} attempts!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

print("\n🛒 Shopping List Manager:")
print("Try running this code:")

def shopping_list_manager():
    shopping_list = []
    
    print("Shopping List Manager")
    print("Type 'done' when finished adding items")
    
    while True:
        item = input("Add item to list: ")
        if item.lower() == "done":
            break
        shopping_list.append(item)
        print(f"Added: {item}")
    
    print("\nYour shopping list:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")

# =============================================================================
# EXERCISES FOR STUDENTS
# =============================================================================

print("\n\n📚 EXERCISES FOR STUDENTS")
print("-" * 35)

print("\n🎯 Exercise 1: Weather Advisor")
print("Ask the user for temperature and weather condition.")
print("Give advice based on the conditions!")

print("\n🎯 Exercise 2: Multiplication Table")
print("Ask for a number and print its multiplication table from 1 to 10.")

print("\n🎯 Exercise 3: Password Checker")
print("Ask for a password and check if it meets requirements:")
print("- At least 8 characters")
print("- Contains uppercase and lowercase letters")
print("- Contains at least one number")

print("\n🎯 Exercise 4: Dice Rolling Game")
print("Roll two dice and keep rolling until you get doubles!")
print("Count how many rolls it takes.")

print("\n🎯 Exercise 5: Word Counter")
print("Ask the user to enter a sentence.")
print("Count how many words, vowels, and consonants it has.")

# =============================================================================
# TEACHING TIPS
# =============================================================================

print("\n\n💡 TEACHING TIPS")
print("-" * 20)

print("\n✅ Tips for Teaching Control Flow:")
print("1. Start with simple if statements")
print("2. Use real-world examples students can relate to")
print("3. Show the difference between if/elif/else")
print("4. Practice with comparison operators")
print("5. Introduce loops with simple counting")
print("6. Show how to avoid infinite loops")
print("7. Use break and continue carefully")

print("\n⚠️ Common Mistakes:")
print("1. Forgetting colons after if/else/for/while")
print("2. Incorrect indentation")
print("3. Using = instead of == for comparison")
print("4. Creating infinite while loops")
print("5. Forgetting to update loop variables")

print("\n🎯 Fun Project Ideas:")
print("1. Interactive quiz game")
print("2. Number guessing game")
print("3. Simple calculator")
print("4. Weather advisor")
print("5. Password strength checker")
print("6. Dice rolling game")
print("7. Word counter and analyzer")

print("\n" + "=" * 60)
print("🎉 Great job learning about control flow!")
print("Remember: if/else for decisions, loops for repetition!")
print("Practice makes perfect! 🚀")
print("=" * 60)

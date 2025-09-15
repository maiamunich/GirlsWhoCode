# Python User Input and Interaction Examples
# Perfect for teaching beginners how to make interactive programs

print("=" * 60)
print("💬 PYTHON USER INPUT AND INTERACTION")
print("=" * 60)

print("\n🔍 What is User Input?")
print("User input lets your program ask questions and get answers from people!")
print("It makes your programs interactive and personal.")

# =============================================================================
# BASIC INPUT FUNCTION
# =============================================================================

print("\n📝 BASIC INPUT FUNCTION")
print("-" * 30)

print("\n💡 The input() function:")
print("Use input() to ask the user a question")
print("The program waits for the user to type and press Enter")

# Example 1: Simple name input
print("\n🎯 Example 1: Getting a Name")
print("Try running this code:")
print("name = input('What is your name? ')")
print("print(f'Hello, {name}!')")

# For demonstration, we'll simulate the input
name = "Alice"  # This would be: name = input('What is your name? ')
print(f"Hello, {name}!")

# Example 2: Getting age
print("\n🎯 Example 2: Getting Age")
print("Try running this code:")
print("age = input('How old are you? ')")
print("print(f'You are {age} years old.')")

age = "20"  # This would be: age = input('How old are you? ')
print(f"You are {age} years old.")

# =============================================================================
# CONVERTING INPUT TYPES
# =============================================================================

print("\n\n🔄 CONVERTING INPUT TYPES")
print("-" * 35)

print("\n⚠️ Important: input() always returns a STRING!")
print("Even if someone types a number, it comes as text.")
print("You need to convert it to a number to do math!")

print("\n📊 Converting String to Number:")
print("Try running this code:")
print("age_text = input('Enter your age: ')")
print("age_number = int(age_text)  # Convert to integer")
print("print(f'Next year you will be {age_number + 1} years old.')")

age_text = "20"  # This would be: age_text = input('Enter your age: ')
age_number = int(age_text)  # Convert to integer
print(f"Next year you will be {age_number + 1} years old.")

print("\n💰 Converting to Float (Decimal Numbers):")
print("Try running this code:")
print("price_text = input('Enter a price: $')")
print("price_number = float(price_text)  # Convert to float")
print("print(f'With tax (10%): ${price_number * 1.1:.2f}')")

price_text = "19.99"  # This would be: price_text = input('Enter a price: $')
price_number = float(price_text)  # Convert to float
print(f"With tax (10%): ${price_number * 1.1:.2f}")

# =============================================================================
# MULTIPLE INPUTS
# =============================================================================

print("\n\n📋 MULTIPLE INPUTS")
print("-" * 25)

print("\n🎯 Getting Multiple Pieces of Information:")
print("You can ask for several things in one program!")

print("\nExample: Personal Information Form")
print("Try running this code:")
print("first_name = input('First name: ')")
print("last_name = input('Last name: ')")
print("age = int(input('Age: '))")
print("favorite_color = input('Favorite color: ')")
print("print(f'Hello {first_name} {last_name}!')")
print("print(f'You are {age} years old and love {favorite_color}!')")

# Simulated inputs
first_name = "Alice"
last_name = "Smith"
age = 20
favorite_color = "blue"

print(f"Hello {first_name} {last_name}!")
print(f"You are {age} years old and love {favorite_color}!")

# =============================================================================
# INPUT VALIDATION
# =============================================================================

print("\n\n✅ INPUT VALIDATION")
print("-" * 25)

print("\n🛡️ What is Input Validation?")
print("Making sure the user enters valid information!")
print("For example, checking if a number is actually a number.")

print("\n🎯 Example: Safe Number Input")
print("Try running this code:")
print("while True:")
print("    try:")
print("        age = int(input('Enter your age (number): '))")
print("        break")
print("    except ValueError:")
print("        print('Please enter a valid number!')")
print("print(f'Your age is {age}')")

# Simulated validation
age = 25  # This would go through the validation loop
print(f"Your age is {age}")

# =============================================================================
# INTERACTIVE PROGRAMS
# =============================================================================

print("\n\n🎮 INTERACTIVE PROGRAMS")
print("-" * 30)

print("\n🎯 Example 1: Simple Calculator")
print("Try running this code:")

def simple_calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Choose an operation (1-4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Cannot divide by zero!")
    else:
        print("Invalid choice!")

print("\n🎯 Example 2: Quiz Program")
print("Try running this code:")

def simple_quiz():
    questions = [
        ("What is 2 + 2?", "4"),
        ("What color is the sky?", "blue"),
        ("How many days in a week?", "7")
    ]
    
    score = 0
    total = len(questions)
    
    for question, answer in questions:
        user_answer = input(f"{question} ")
        if user_answer.lower() == answer.lower():
            print("Correct! 🎉")
            score += 1
        else:
            print(f"Wrong! The answer is {answer}")
    
    print(f"\nQuiz Complete!")
    print(f"Score: {score}/{total}")
    percentage = (score / total) * 100
    print(f"Percentage: {percentage:.1f}%")

print("\n🎯 Example 3: Personal Greeting")
print("Try running this code:")

def personal_greeting():
    name = input("What's your name? ")
    age = int(input("How old are you? "))
    favorite_food = input("What's your favorite food? ")
    
    print(f"\nNice to meet you, {name}!")
    print(f"You are {age} years old.")
    print(f"I love {favorite_food} too!")
    
    if age >= 18:
        print("You are an adult!")
    else:
        print("You are still young!")
    
    print(f"Have a great day, {name}! 👋")

# =============================================================================
# PRACTICAL EXERCISES FOR STUDENTS
# =============================================================================

print("\n\n📚 PRACTICAL EXERCISES FOR STUDENTS")
print("-" * 45)

print("\n🎯 Exercise 1: Mad Libs Game")
print("Create a program that asks for:")
print("- A noun")
print("- A verb")
print("- An adjective")
print("- A place")
print("Then create a funny story using their answers!")

print("\n🎯 Exercise 2: Grade Calculator")
print("Ask the user for:")
print("- Their name")
print("- Three test scores")
print("Calculate and display their average grade!")

print("\n🎯 Exercise 3: Shopping List")
print("Ask the user to enter items for their shopping list.")
print("Keep asking until they type 'done'.")
print("Then display their complete shopping list!")

print("\n🎯 Exercise 4: Number Guessing Game")
print("Ask the user to guess a number between 1 and 10.")
print("Tell them if they're too high, too low, or correct!")
print("Keep track of how many guesses they make.")

# =============================================================================
# TIPS FOR TEACHING INPUT
# =============================================================================

print("\n\n💡 TIPS FOR TEACHING INPUT")
print("-" * 35)

print("\n✅ Teaching Tips:")
print("1. Start with simple input() examples")
print("2. Show that input() always returns a string")
print("3. Demonstrate type conversion (int(), float())")
print("4. Practice with real examples students can relate to")
print("5. Show error handling with try/except")
print("6. Build up to interactive programs gradually")

print("\n⚠️ Common Mistakes Students Make:")
print("1. Forgetting that input() returns a string")
print("2. Not converting strings to numbers for math")
print("3. Not handling invalid input")
print("4. Forgetting to use input() in their code")

print("\n🎯 Fun Project Ideas:")
print("1. Personal information form")
print("2. Simple calculator")
print("3. Quiz game")
print("4. Mad Libs story generator")
print("5. Shopping list manager")
print("6. Number guessing game")
print("7. Simple chat bot")

print("\n" + "=" * 60)
print("🎉 Great job learning about user input!")
print("Remember: input() gets text, convert to numbers for math!")
print("Make your programs interactive and fun! 🚀")
print("=" * 60)

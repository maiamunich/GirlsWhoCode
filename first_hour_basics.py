# Girls Who Code - First Hour Python Basics
# Perfect for complete beginners - just the essentials!

print("=" * 50)
print("👩‍💻 GIRLS WHO CODE - YOUR FIRST HOUR!")
print("=" * 50)

print("\n🎉 Welcome to coding! Let's learn Python together!")
print("Today we'll learn the basics in just one hour!")

# =============================================================================
# PART 1: WHAT IS A VARIABLE? (10 minutes)
# =============================================================================

print("\n\n📝 PART 1: WHAT IS A VARIABLE?")
print("-" * 35)

print("\n💡 Think of a variable like a labeled box!")
print("You put something inside and give it a name.")

# Simple variables
print("\n🔤 Let's create some variables:")

# String (text)
my_name = "Sarah"
my_favorite_color = "purple"
my_school = "Lincoln High School"

print(f"My name is {my_name}")
print(f"My favorite color is {my_favorite_color}")
print(f"I go to {my_school}")

# Numbers
print("\n🔢 Now let's use numbers:")

my_age = 16
my_grade = 10
my_height = 5.4  # feet

print(f"I am {my_age} years old")
print(f"I am in grade {my_grade}")
print(f"I am {my_height} feet tall")

# =============================================================================
# PART 2: PRINTING AND MESSAGES (10 minutes)
# =============================================================================

print("\n\n💬 PART 2: PRINTING AND MESSAGES")
print("-" * 40)

print("\n💡 The print() function shows messages on the screen!")
print("It's like writing on a piece of paper that everyone can see.")

# Basic printing
print("Hello, world!")
print("I am learning to code!")
print("This is so cool!")

# Printing variables
print(f"\nLet's print our variables:")
print(f"Hi! My name is {my_name} and I'm {my_age} years old!")

# Different ways to print
print("\nYou can print:")
print("- Regular text")
print("- Variables")
print("- Numbers")
print("- Anything you want!")

# =============================================================================
# PART 3: GETTING INPUT FROM USERS (15 minutes)
# =============================================================================

print("\n\n👂 PART 3: GETTING INPUT FROM USERS")
print("-" * 45)

print("\n💡 Now let's make our program interactive!")
print("We can ask questions and get answers!")

# Note: In a real class, uncomment these lines:
# print("\nLet's get to know each other!")
# your_name = input("What's your name? ")
# your_age = input("How old are you? ")
# your_favorite_food = input("What's your favorite food? ")

# For demonstration, we'll use example values:
your_name = "Alex"
your_age = "15"
your_favorite_food = "pizza"

print(f"\nNice to meet you, {your_name}!")
print(f"You are {your_age} years old.")
print(f"I love {your_favorite_food} too!")

# Converting text to numbers
print("\n🔢 Converting text to numbers:")
age_number = int(your_age)  # Convert string to integer
next_year_age = age_number + 1
print(f"Next year you'll be {next_year_age} years old!")

# =============================================================================
# PART 4: MAKING DECISIONS (15 minutes)
# =============================================================================

print("\n\n🤔 PART 4: MAKING DECISIONS")
print("-" * 35)

print("\n💡 Programs can make decisions!")
print("Like: 'If it's raining, bring an umbrella!'")

# Simple if statement
print("\n🎯 Let's make some decisions:")

weather = "sunny"
if weather == "sunny":
    print("☀️ It's sunny! Perfect day for a walk!")
else:
    print("🌧️ It's not sunny. Maybe stay inside!")

# Age-based decisions
print("\n🎂 Age-based decisions:")
age = 16
if age >= 16:
    print("🎉 You can get a driver's license!")
else:
    print("🚗 You're too young to drive.")

# Multiple conditions
print("\n🎨 Favorite color decisions:")
favorite_color = "blue"
if favorite_color == "blue":
    print("💙 Blue is a great color! Like the sky!")
elif favorite_color == "pink":
    print("💗 Pink is so pretty!")
elif favorite_color == "green":
    print("💚 Green is the color of nature!")
else:
    print(f"🌈 {favorite_color} is a beautiful color too!")

# =============================================================================
# PART 5: LISTS - COLLECTIONS OF THINGS (10 minutes)
# =============================================================================

print("\n\n📋 PART 5: LISTS - COLLECTIONS OF THINGS")
print("-" * 50)

print("\n💡 Lists are like shopping lists!")
print("You can put many things in one list.")

# Creating lists
print("\n🛍️ Let's make some lists:")

favorite_foods = ["pizza", "ice cream", "chocolate", "strawberries"]
print(f"My favorite foods: {favorite_foods}")

friends = ["Emma", "Sofia", "Maya", "Zoe"]
print(f"My friends: {friends}")

# Accessing list items
print("\n🎯 Getting items from lists:")
print(f"My #1 favorite food: {favorite_foods[0]}")
print(f"My #2 favorite food: {favorite_foods[1]}")
print(f"My best friend: {friends[0]}")

# Adding to lists
print("\n➕ Adding new items:")
favorite_foods.append("cookies")
print(f"After adding cookies: {favorite_foods}")

# List length
print(f"\n📊 I have {len(friends)} friends")
print(f"I have {len(favorite_foods)} favorite foods")

# =============================================================================
# FUN ACTIVITY: CREATE YOUR PROFILE (10 minutes)
# =============================================================================

print("\n\n🎨 FUN ACTIVITY: CREATE YOUR PROFILE")
print("-" * 45)

print("\n💡 Let's create a profile about yourself!")
print("We'll use everything we learned today!")

# Student profile
print("\n👤 STUDENT PROFILE")
print("-" * 20)

# In a real class, students would input their own information:
# student_name = input("Your name: ")
# student_age = int(input("Your age: "))
# student_school = input("Your school: ")
# student_hobby = input("Your hobby: ")

# For demonstration:
student_name = "Taylor"
student_age = 17
student_school = "Roosevelt High"
student_hobby = "dancing"

# Create profile
print(f"Name: {student_name}")
print(f"Age: {student_age}")
print(f"School: {student_school}")
print(f"Hobby: {student_hobby}")

# Age-based message
if student_age >= 16:
    print(f"🎉 {student_name} can drive!")
else:
    print(f"🚗 {student_name} is learning to drive!")

# Hobby-based message
if student_hobby == "dancing":
    print("💃 Dancing is so much fun!")
elif student_hobby == "reading":
    print("📚 Reading opens new worlds!")
elif student_hobby == "sports":
    print("⚽ Sports keep you healthy!")
else:
    print(f"🎨 {student_hobby} sounds awesome!")

# =============================================================================
# WHAT WE LEARNED TODAY
# =============================================================================

print("\n\n🎓 WHAT WE LEARNED TODAY")
print("-" * 30)

print("\n✅ Today you learned:")
print("1. 📝 Variables - storing information")
print("2. 💬 Printing - showing messages")
print("3. 👂 Input - getting information from users")
print("4. 🤔 If/else - making decisions")
print("5. 📋 Lists - organizing information")

print("\n🌟 You are now a programmer!")
print("You can:")
print("- Store information in variables")
print("- Show messages to users")
print("- Get input from people")
print("- Make decisions in your code")
print("- Organize data in lists")

# =============================================================================
# NEXT STEPS
# =============================================================================

print("\n\n🚀 NEXT STEPS")
print("-" * 20)

print("\n💡 What's next?")
print("1. 🔄 Practice with loops (repeating actions)")
print("2. 🔧 Learn functions (reusable code)")
print("3. 📊 Work with more data types")
print("4. 🎮 Build your first game!")
print("5. 🌐 Create a website!")

print("\n🎯 Keep coding!")
print("Every expert was once a beginner.")
print("You're doing amazing! 🌟")

print("\n" + "=" * 50)
print("🎉 CONGRATULATIONS!")
print("You completed your first hour of coding!")
print("Welcome to the Girls Who Code family! 👩‍💻")
print("=" * 50)

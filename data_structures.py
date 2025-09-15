# Python Data Structures - Lists, Dictionaries, and Tuples
# Perfect for teaching beginners about organizing data

print("=" * 60)
print("📚 PYTHON DATA STRUCTURES FOR BEGINNERS")
print("=" * 60)

# =============================================================================
# LISTS - Ordered Collections (Like a Shopping List)
# =============================================================================

print("\n📋 LISTS - Ordered Collections")
print("-" * 40)

print("\n🔍 What are Lists?")
print("Lists are like shopping lists - they keep items in order!")
print("You can add, remove, and change items in lists.")

# Creating lists
print("\n📝 Creating Lists:")
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["hello", 42, True, 3.14]

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")

# Accessing list items
print("\n🎯 Accessing List Items:")
print(f"First fruit: {fruits[0]}")  # Index 0 is first item
print(f"Second fruit: {fruits[1]}")  # Index 1 is second item
print(f"Last fruit: {fruits[-1]}")  # -1 means last item
print(f"Number of fruits: {len(fruits)}")

# Adding items to lists
print("\n➕ Adding Items:")
fruits.append("grape")  # Add to end
print(f"After adding grape: {fruits}")

fruits.insert(1, "strawberry")  # Add at specific position
print(f"After inserting strawberry at position 1: {fruits}")

# Removing items from lists
print("\n➖ Removing Items:")
fruits.remove("banana")  # Remove specific item
print(f"After removing banana: {fruits}")

last_fruit = fruits.pop()  # Remove and return last item
print(f"Removed: {last_fruit}")
print(f"Remaining fruits: {fruits}")

# List methods
print("\n🔧 Useful List Methods:")
scores = [85, 92, 78, 96, 88]
print(f"Original scores: {scores}")
print(f"Sorted scores: {sorted(scores)}")
print(f"Highest score: {max(scores)}")
print(f"Lowest score: {min(scores)}")
print(f"Sum of scores: {sum(scores)}")

# =============================================================================
# DICTIONARIES - Key-Value Pairs (Like a Phone Book)
# =============================================================================

print("\n\n📖 DICTIONARIES - Key-Value Pairs")
print("-" * 45)

print("\n🔍 What are Dictionaries?")
print("Dictionaries are like phone books - you look up a name (key)")
print("to find a phone number (value).")

# Creating dictionaries
print("\n📝 Creating Dictionaries:")
student_info = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "favorite_subject": "Math"
}

phone_book = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9012"
}

print(f"Student info: {student_info}")
print(f"Phone book: {phone_book}")

# Accessing dictionary values
print("\n🎯 Accessing Dictionary Values:")
print(f"Student name: {student_info['name']}")
print(f"Student age: {student_info['age']}")
print(f"Alice's phone: {phone_book['Alice']}")

# Adding and changing values
print("\n✏️ Adding and Changing Values:")
student_info["email"] = "alice@school.com"  # Add new key-value pair
student_info["age"] = 21  # Change existing value
print(f"Updated student info: {student_info}")

# Dictionary methods
print("\n🔧 Useful Dictionary Methods:")
print(f"All keys: {list(student_info.keys())}")
print(f"All values: {list(student_info.values())}")
print(f"All items: {list(student_info.items())}")

# Checking if key exists
if "email" in student_info:
    print("Student has an email address!")
else:
    print("Student doesn't have an email address.")

# =============================================================================
# TUPLES - Immutable Collections (Like Coordinates)
# =============================================================================

print("\n\n📦 TUPLES - Immutable Collections")
print("-" * 40)

print("\n🔍 What are Tuples?")
print("Tuples are like lists, but you CAN'T change them after creating.")
print("Perfect for things that shouldn't change, like coordinates!")

# Creating tuples
print("\n📝 Creating Tuples:")
coordinates = (10, 20)  # X and Y coordinates
colors = ("red", "green", "blue")  # Primary colors
student_data = ("Alice", 20, "Computer Science")  # Name, age, major

print(f"Coordinates: {coordinates}")
print(f"Colors: {colors}")
print(f"Student data: {student_data}")

# Accessing tuple items
print("\n🎯 Accessing Tuple Items:")
print(f"X coordinate: {coordinates[0]}")
print(f"Y coordinate: {coordinates[1]}")
print(f"First color: {colors[0]}")
print(f"Student name: {student_data[0]}")

# Tuple operations
print("\n🔧 Tuple Operations:")
print(f"Number of colors: {len(colors)}")
print(f"Is 'red' in colors? {'red' in colors}")
print(f"Number of times 'red' appears: {colors.count('red')}")

# Converting between types
print("\n🔄 Converting Between Types:")
fruits_list = ["apple", "banana", "orange"]
fruits_tuple = tuple(fruits_list)  # Convert list to tuple
fruits_back_to_list = list(fruits_tuple)  # Convert tuple back to list

print(f"Original list: {fruits_list}")
print(f"As tuple: {fruits_tuple}")
print(f"Back to list: {fruits_back_to_list}")

# =============================================================================
# PRACTICAL EXAMPLES
# =============================================================================

print("\n\n🎯 PRACTICAL EXAMPLES")
print("-" * 30)

print("\n📊 STUDENT GRADEBOOK:")
print("-" * 25)

# Using lists and dictionaries together
students = ["Alice", "Bob", "Charlie"]
grades = {
    "Alice": [85, 92, 78],
    "Bob": [90, 88, 95],
    "Charlie": [75, 82, 88]
}

print("Student Gradebook:")
for student in students:
    student_grades = grades[student]
    average = sum(student_grades) / len(student_grades)
    print(f"{student}: {student_grades} (Average: {average:.1f})")

print("\n🛒 SHOPPING CART:")
print("-" * 20)

# Shopping cart using dictionary
cart = {
    "apple": 1.50,
    "banana": 0.75,
    "orange": 2.00,
    "bread": 3.50
}

print("Shopping Cart:")
total = 0
for item, price in cart.items():
    print(f"{item}: ${price:.2f}")
    total += price

print(f"Total: ${total:.2f}")

print("\n🎮 GAME SCORES:")
print("-" * 18)

# Game scores using tuples for high scores
high_scores = [
    ("Alice", 1500),
    ("Bob", 1200),
    ("Charlie", 1100),
    ("Diana", 1000)
]

print("High Scores:")
for i, (player, score) in enumerate(high_scores, 1):
    print(f"{i}. {player}: {score} points")

print("\n" + "=" * 60)
print("🎉 Great job learning about data structures!")
print("Remember: Lists for changing data, Dictionaries for lookups,")
print("and Tuples for data that shouldn't change!")
print("=" * 60)

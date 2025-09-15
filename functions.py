# Python Functions - Reusable Code Blocks
# Perfect for teaching beginners about organizing and reusing code

print("=" * 60)
print("🔧 PYTHON FUNCTIONS - REUSABLE CODE BLOCKS")
print("=" * 60)

print("\n🔍 What are Functions?")
print("Functions are like recipes - you write them once and use them many times!")
print("They help you organize your code and avoid repetition.")

# =============================================================================
# BASIC FUNCTIONS
# =============================================================================

print("\n\n🔧 BASIC FUNCTIONS")
print("-" * 25)

print("\n💡 What is a Function?")
print("A function is a block of code that does something specific.")
print("You can call it whenever you need that action!")

# Simple function without parameters
print("\n🎯 Simple Function (No Parameters):")
print("Try running this code:")
print("def say_hello():")
print("    print('Hello, World!')")
print("    print('Welcome to Python!')")
print("")
print("# Call the function")
print("say_hello()")

def say_hello():
    print("Hello, World!")
    print("Welcome to Python!")

# Call the function
say_hello()

# Function with parameters
print("\n🎯 Function with Parameters:")
print("Try running this code:")
print("def greet_person(name):")
print("    print(f'Hello, {name}!')")
print("    print(f'Nice to meet you, {name}!')")
print("")
print("# Call the function with different names")
print("greet_person('Alice')")
print("greet_person('Bob')")

def greet_person(name):
    print(f"Hello, {name}!")
    print(f"Nice to meet you, {name}!")

# Call the function with different names
greet_person("Alice")
greet_person("Bob")

# Function with multiple parameters
print("\n🎯 Function with Multiple Parameters:")
print("Try running this code:")
print("def introduce(name, age, city):")
print("    print(f'Hi, I\\'m {name}.')")
print("    print(f'I\\'m {age} years old.')")
print("    print(f'I live in {city}.')")
print("")
print("# Call the function")
print("introduce('Charlie', 25, 'New York')")

def introduce(name, age, city):
    print(f"Hi, I'm {name}.")
    print(f"I'm {age} years old.")
    print(f"I live in {city}.")

# Call the function
introduce("Charlie", 25, "New York")

# =============================================================================
# FUNCTIONS WITH RETURN VALUES
# =============================================================================

print("\n\n📤 FUNCTIONS WITH RETURN VALUES")
print("-" * 40)

print("\n💡 Return Values:")
print("Functions can give you back a result!")
print("Like a calculator that gives you the answer.")

# Function that returns a value
print("\n🎯 Function with Return Value:")
print("Try running this code:")
print("def add_numbers(a, b):")
print("    result = a + b")
print("    return result")
print("")
print("# Use the function")
print("sum_result = add_numbers(5, 3)")
print("print(f'5 + 3 = {sum_result}')")

def add_numbers(a, b):
    result = a + b
    return result

# Use the function
sum_result = add_numbers(5, 3)
print(f"5 + 3 = {sum_result}")

# Multiple return values
print("\n🎯 Function with Multiple Return Values:")
print("Try running this code:")
print("def calculate_area_perimeter(length, width):")
print("    area = length * width")
print("    perimeter = 2 * (length + width)")
print("    return area, perimeter")
print("")
print("# Use the function")
print("area, perimeter = calculate_area_perimeter(5, 3)")
print("print(f'Area: {area} square units')")
print("print(f'Perimeter: {perimeter} units')")

def calculate_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Use the function
area, perimeter = calculate_area_perimeter(5, 3)
print(f"Area: {area} square units")
print(f"Perimeter: {perimeter} units")

# =============================================================================
# DEFAULT PARAMETERS
# =============================================================================

print("\n\n⚙️ DEFAULT PARAMETERS")
print("-" * 30)

print("\n💡 Default Parameters:")
print("You can give parameters default values!")
print("If someone doesn't provide a value, the default is used.")

# Function with default parameters
print("\n🎯 Function with Default Parameters:")
print("Try running this code:")
print("def greet_with_defaults(name, greeting='Hello', punctuation='!'):")
print("    return f'{greeting}, {name}{punctuation}'")
print("")
print("# Use with all parameters")
print("message1 = greet_with_defaults('Alice', 'Hi', '!!!')")
print("print(message1)")
print("")
print("# Use with some defaults")
print("message2 = greet_with_defaults('Bob', 'Good morning')")
print("print(message2)")
print("")
print("# Use with all defaults")
print("message3 = greet_with_defaults('Charlie')")
print("print(message3)")

def greet_with_defaults(name, greeting="Hello", punctuation="!"):
    return f"{greeting}, {name}{punctuation}"

# Use with all parameters
message1 = greet_with_defaults("Alice", "Hi", "!!!")
print(message1)

# Use with some defaults
message2 = greet_with_defaults("Bob", "Good morning")
print(message2)

# Use with all defaults
message3 = greet_with_defaults("Charlie")
print(message3)

# =============================================================================
# PRACTICAL FUNCTION EXAMPLES
# =============================================================================

print("\n\n🎯 PRACTICAL FUNCTION EXAMPLES")
print("-" * 40)

print("\n📊 Grade Calculator Function:")
print("Try running this code:")

def calculate_grade_average(grades):
    """Calculate the average of a list of grades."""
    if not grades:  # Check if list is empty
        return 0
    total = sum(grades)
    average = total / len(grades)
    return average

def get_letter_grade(average):
    """Convert numeric average to letter grade."""
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

# Use the functions
student_grades = [85, 92, 78, 96, 88]
average = calculate_grade_average(student_grades)
letter_grade = get_letter_grade(average)

print(f"Grades: {student_grades}")
print(f"Average: {average:.1f}")
print(f"Letter Grade: {letter_grade}")

print("\n🛒 Shopping Cart Functions:")
print("Try running this code:")

def calculate_total(items):
    """Calculate total cost of items."""
    total = 0
    for item, price in items.items():
        total += price
    return total

def apply_discount(total, discount_percent):
    """Apply discount to total."""
    discount_amount = total * (discount_percent / 100)
    final_total = total - discount_amount
    return final_total, discount_amount

def print_receipt(items, discount_percent=0):
    """Print a shopping receipt."""
    print("🛒 SHOPPING RECEIPT")
    print("-" * 20)
    
    for item, price in items.items():
        print(f"{item}: ${price:.2f}")
    
    subtotal = calculate_total(items)
    print(f"Subtotal: ${subtotal:.2f}")
    
    if discount_percent > 0:
        final_total, discount = apply_discount(subtotal, discount_percent)
        print(f"Discount ({discount_percent}%): ${discount:.2f}")
        print(f"Final Total: ${final_total:.2f}")
    else:
        print(f"Total: ${subtotal:.2f}")

# Use the functions
cart = {
    "apple": 1.50,
    "banana": 0.75,
    "orange": 2.00,
    "bread": 3.50
}

print_receipt(cart, 10)  # 10% discount

print("\n🎮 Game Functions:")
print("Try running this code:")

def roll_dice():
    """Simulate rolling a dice."""
    import random
    return random.randint(1, 6)

def play_dice_game():
    """Play a simple dice game."""
    print("🎲 Dice Game!")
    print("Roll two dice and see what you get!")
    
    dice1 = roll_dice()
    dice2 = roll_dice()
    total = dice1 + dice2
    
    print(f"Dice 1: {dice1}")
    print(f"Dice 2: {dice2}")
    print(f"Total: {total}")
    
    if total == 7:
        print("🎉 Lucky seven!")
    elif total >= 10:
        print("🔥 High roll!")
    elif total <= 4:
        print("😅 Low roll!")
    else:
        print("👍 Good roll!")

# Play the game
play_dice_game()

# =============================================================================
# FUNCTION SCOPE AND VARIABLES
# =============================================================================

print("\n\n🔍 FUNCTION SCOPE AND VARIABLES")
print("-" * 40)

print("\n💡 Variable Scope:")
print("Variables inside functions are separate from variables outside!")
print("This prevents functions from interfering with each other.")

# Global vs local variables
print("\n🎯 Global vs Local Variables:")
print("Try running this code:")

global_variable = "I'm global!"

def demonstrate_scope():
    local_variable = "I'm local!"
    print(f"Inside function - Global: {global_variable}")
    print(f"Inside function - Local: {local_variable}")

print(f"Outside function - Global: {global_variable}")
demonstrate_scope()
# print(local_variable)  # This would cause an error!

# =============================================================================
# DOCSTRINGS AND COMMENTS
# =============================================================================

print("\n\n📝 DOCSTRINGS AND COMMENTS")
print("-" * 35)

print("\n💡 Documenting Functions:")
print("Always document your functions so others (and you!) can understand them!")

def calculate_circle_area(radius):
    """
    Calculate the area of a circle.
    
    Parameters:
    radius (float): The radius of the circle
    
    Returns:
    float: The area of the circle
    """
    pi = 3.14159
    area = pi * radius * radius
    return area

# Use the documented function
circle_area = calculate_circle_area(5)
print(f"Area of circle with radius 5: {circle_area:.2f}")

# =============================================================================
# EXERCISES FOR STUDENTS
# =============================================================================

print("\n\n📚 EXERCISES FOR STUDENTS")
print("-" * 35)

print("\n🎯 Exercise 1: Temperature Converter")
print("Create functions to convert:")
print("- Celsius to Fahrenheit")
print("- Fahrenheit to Celsius")
print("- Both directions!")

print("\n🎯 Exercise 2: Word Counter")
print("Create a function that:")
print("- Takes a sentence as input")
print("- Returns the number of words")
print("- Returns the number of vowels")
print("- Returns the longest word")

print("\n🎯 Exercise 3: Simple Calculator")
print("Create functions for:")
print("- Addition")
print("- Subtraction")
print("- Multiplication")
print("- Division")
print("- A main function that uses all of them")

print("\n🎯 Exercise 4: Password Generator")
print("Create a function that generates a random password:")
print("- Takes length as parameter")
print("- Includes letters, numbers, and symbols")
print("- Returns a secure password")

print("\n🎯 Exercise 5: Student Grade Manager")
print("Create functions to:")
print("- Add a student's grades")
print("- Calculate average grade")
print("- Find the highest and lowest grades")
print("- Generate a grade report")

# =============================================================================
# TEACHING TIPS
# =============================================================================

print("\n\n💡 TEACHING TIPS")
print("-" * 20)

print("\n✅ Tips for Teaching Functions:")
print("1. Start with simple functions that print messages")
print("2. Show how functions avoid code repetition")
print("3. Explain parameters vs arguments clearly")
print("4. Demonstrate return values with simple math")
print("5. Show how to use functions together")
print("6. Emphasize the importance of documentation")
print("7. Practice with real-world examples")

print("\n⚠️ Common Mistakes:")
print("1. Forgetting to call the function (missing parentheses)")
print("2. Wrong number of parameters")
print("3. Not understanding return vs print")
print("4. Confusing local and global variables")
print("5. Forgetting to handle edge cases")

print("\n🎯 Fun Project Ideas:")
print("1. Interactive calculator")
print("2. Text-based adventure game")
print("3. Grade management system")
print("4. Simple banking system")
print("5. Recipe organizer")
print("6. Personal finance tracker")
print("7. Quiz game with scoring")

print("\n" + "=" * 60)
print("🎉 Great job learning about functions!")
print("Remember: Functions help you organize and reuse code!")
print("Practice writing functions for everything! 🚀")
print("=" * 60)

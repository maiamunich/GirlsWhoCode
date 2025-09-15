# Python Mini-Projects for Beginners
# Complete projects that combine all the concepts learned

print("=" * 60)
print("🎯 PYTHON MINI-PROJECTS FOR BEGINNERS")
print("=" * 60)

print("\n🔍 What are Mini-Projects?")
print("Mini-projects combine everything you've learned!")
print("They're like putting together puzzle pieces to make something cool!")

# =============================================================================
# PROJECT 1: PERSONAL INFORMATION MANAGER
# =============================================================================

print("\n\n📋 PROJECT 1: PERSONAL INFORMATION MANAGER")
print("-" * 50)

def personal_info_manager():
    """
    A program that collects and manages personal information.
    Combines: variables, input, functions, dictionaries, loops
    """
    print("👤 PERSONAL INFORMATION MANAGER")
    print("=" * 40)
    
    # Dictionary to store information
    personal_info = {}
    
    # Collect basic information
    print("\n📝 Let's collect your information:")
    personal_info["name"] = input("What's your full name? ")
    personal_info["age"] = int(input("How old are you? "))
    personal_info["city"] = input("What city do you live in? ")
    personal_info["email"] = input("What's your email address? ")
    
    # Collect hobbies
    print("\n🎨 What are your hobbies? (Type 'done' when finished)")
    hobbies = []
    while True:
        hobby = input("Enter a hobby: ")
        if hobby.lower() == "done":
            break
        hobbies.append(hobby)
    personal_info["hobbies"] = hobbies
    
    # Collect favorite subjects
    print("\n📚 What are your favorite school subjects? (Type 'done' when finished)")
    subjects = []
    while True:
        subject = input("Enter a subject: ")
        if subject.lower() == "done":
            break
        subjects.append(subject)
    personal_info["favorite_subjects"] = subjects
    
    # Display information
    print("\n" + "=" * 40)
    print("📊 YOUR PERSONAL INFORMATION")
    print("=" * 40)
    
    print(f"Name: {personal_info['name']}")
    print(f"Age: {personal_info['age']}")
    print(f"City: {personal_info['city']}")
    print(f"Email: {personal_info['email']}")
    
    print(f"\nHobbies ({len(personal_info['hobbies'])}):")
    for i, hobby in enumerate(personal_info['hobbies'], 1):
        print(f"  {i}. {hobby}")
    
    print(f"\nFavorite Subjects ({len(personal_info['favorite_subjects'])}):")
    for i, subject in enumerate(personal_info['favorite_subjects'], 1):
        print(f"  {i}. {subject}")
    
    # Age-based message
    if personal_info['age'] >= 18:
        print(f"\n🎉 {personal_info['name']}, you are an adult!")
    else:
        print(f"\n🌟 {personal_info['name']}, you are still young and learning!")

# =============================================================================
# PROJECT 2: INTERACTIVE QUIZ GAME
# =============================================================================

print("\n\n🎮 PROJECT 2: INTERACTIVE QUIZ GAME")
print("-" * 45)

def quiz_game():
    """
    An interactive quiz game with scoring.
    Combines: functions, lists, dictionaries, loops, if/else
    """
    print("🧠 INTERACTIVE QUIZ GAME")
    print("=" * 30)
    
    # Quiz questions and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Paris", "C) Berlin", "D) Madrid"],
            "correct": "B",
            "answer": "Paris"
        },
        {
            "question": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "correct": "B",
            "answer": "4"
        },
        {
            "question": "What color do you get when you mix red and blue?",
            "options": ["A) Green", "B) Yellow", "C) Purple", "D) Orange"],
            "correct": "C",
            "answer": "Purple"
        },
        {
            "question": "How many days are in a week?",
            "options": ["A) 5", "B) 6", "C) 7", "D) 8"],
            "correct": "C",
            "answer": "7"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "correct": "C",
            "answer": "Jupiter"
        }
    ]
    
    score = 0
    total_questions = len(questions)
    
    print(f"Welcome to the quiz! You have {total_questions} questions.")
    print("Choose the letter (A, B, C, or D) for your answer.\n")
    
    # Ask each question
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(f"  {option}")
        
        user_answer = input("Your answer (A/B/C/D): ").upper()
        
        if user_answer == q['correct']:
            print("✅ Correct! 🎉")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['correct']}) {q['answer']}")
        
        print("-" * 30)
    
    # Calculate and display results
    percentage = (score / total_questions) * 100
    
    print("\n" + "=" * 30)
    print("📊 QUIZ RESULTS")
    print("=" * 30)
    print(f"Score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.1f}%")
    
    if percentage >= 90:
        print("🌟 Excellent! You're a quiz master!")
    elif percentage >= 80:
        print("👍 Great job! You did very well!")
    elif percentage >= 70:
        print("👌 Good work! Keep studying!")
    elif percentage >= 60:
        print("📚 Not bad! Review the material!")
    else:
        print("💪 Keep trying! Practice makes perfect!")

# =============================================================================
# PROJECT 3: SIMPLE CALCULATOR
# =============================================================================

print("\n\n🧮 PROJECT 3: SIMPLE CALCULATOR")
print("-" * 40)

def simple_calculator():
    """
    A simple calculator with multiple operations.
    Combines: functions, loops, if/else, user input
    """
    print("🧮 SIMPLE CALCULATOR")
    print("=" * 25)
    
    def add(a, b):
        return a + b
    
    def subtract(a, b):
        return a - b
    
    def multiply(a, b):
        return a * b
    
    def divide(a, b):
        if b != 0:
            return a / b
        else:
            return "Error: Cannot divide by zero!"
    
    def power(a, b):
        return a ** b
    
    print("Available operations:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Power (**)")
    print("6. Exit")
    
    while True:
        print("\n" + "-" * 25)
        choice = input("Choose an operation (1-6): ")
        
        if choice == "6":
            print("👋 Thanks for using the calculator!")
            break
        
        if choice in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == "1":
                    result = add(num1, num2)
                    print(f"{num1} + {num2} = {result}")
                elif choice == "2":
                    result = subtract(num1, num2)
                    print(f"{num1} - {num2} = {result}")
                elif choice == "3":
                    result = multiply(num1, num2)
                    print(f"{num1} * {num2} = {result}")
                elif choice == "4":
                    result = divide(num1, num2)
                    print(f"{num1} / {num2} = {result}")
                elif choice == "5":
                    result = power(num1, num2)
                    print(f"{num1} ** {num2} = {result}")
                
            except ValueError:
                print("❌ Please enter valid numbers!")
        else:
            print("❌ Invalid choice! Please choose 1-6.")

# =============================================================================
# PROJECT 4: SHOPPING LIST MANAGER
# =============================================================================

print("\n\n🛒 PROJECT 4: SHOPPING LIST MANAGER")
print("-" * 45)

def shopping_list_manager():
    """
    A shopping list manager with add, remove, and display features.
    Combines: lists, functions, loops, user input, if/else
    """
    print("🛒 SHOPPING LIST MANAGER")
    print("=" * 30)
    
    shopping_list = []
    
    def display_menu():
        print("\n📋 MENU:")
        print("1. Add item to list")
        print("2. Remove item from list")
        print("3. Display shopping list")
        print("4. Clear entire list")
        print("5. Exit")
    
    def add_item():
        item = input("Enter item to add: ")
        if item.strip():  # Check if item is not empty
            shopping_list.append(item.strip())
            print(f"✅ Added '{item}' to your list!")
        else:
            print("❌ Please enter a valid item!")
    
    def remove_item():
        if not shopping_list:
            print("📝 Your shopping list is empty!")
            return
        
        print("\nCurrent items:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
        
        try:
            choice = int(input("Enter number of item to remove: "))
            if 1 <= choice <= len(shopping_list):
                removed_item = shopping_list.pop(choice - 1)
                print(f"✅ Removed '{removed_item}' from your list!")
            else:
                print("❌ Invalid number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def display_list():
        if not shopping_list:
            print("📝 Your shopping list is empty!")
        else:
            print(f"\n🛒 YOUR SHOPPING LIST ({len(shopping_list)} items):")
            print("-" * 30)
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
    
    def clear_list():
        if shopping_list:
            confirm = input("Are you sure you want to clear the entire list? (yes/no): ")
            if confirm.lower() in ["yes", "y"]:
                shopping_list.clear()
                print("✅ Shopping list cleared!")
            else:
                print("❌ List not cleared.")
        else:
            print("📝 Your shopping list is already empty!")
    
    # Main program loop
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            display_list()
        elif choice == "4":
            clear_list()
        elif choice == "5":
            print("👋 Thanks for using Shopping List Manager!")
            break
        else:
            print("❌ Invalid choice! Please choose 1-5.")

# =============================================================================
# PROJECT 5: NUMBER GUESSING GAME
# =============================================================================

print("\n\n🎯 PROJECT 5: NUMBER GUESSING GAME")
print("-" * 45)

def number_guessing_game():
    """
    A number guessing game with difficulty levels.
    Combines: random numbers, loops, functions, user input
    """
    import random
    
    print("🎯 NUMBER GUESSING GAME")
    print("=" * 30)
    
    def play_game(min_num, max_num, max_attempts):
        secret_number = random.randint(min_num, max_num)
        attempts = 0
        
        print(f"\n🎮 I'm thinking of a number between {min_num} and {max_num}.")
        print(f"You have {max_attempts} attempts to guess it!")
        
        while attempts < max_attempts:
            try:
                guess = int(input(f"\nAttempt {attempts + 1}: Guess the number: "))
                attempts += 1
                
                if guess == secret_number:
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                    return True
                elif guess < secret_number:
                    print("📈 Too low! Try a higher number.")
                else:
                    print("📉 Too high! Try a lower number.")
                
                remaining = max_attempts - attempts
                if remaining > 0:
                    print(f"Attempts remaining: {remaining}")
                
            except ValueError:
                print("❌ Please enter a valid number!")
                attempts -= 1  # Don't count invalid attempts
        
        print(f"\n😔 Game over! The number was {secret_number}.")
        return False
    
    def choose_difficulty():
        print("\n🎚️ Choose difficulty level:")
        print("1. Easy (1-10, 5 attempts)")
        print("2. Medium (1-50, 7 attempts)")
        print("3. Hard (1-100, 10 attempts)")
        print("4. Custom")
        
        while True:
            choice = input("Choose difficulty (1-4): ")
            
            if choice == "1":
                return 1, 10, 5
            elif choice == "2":
                return 1, 50, 7
            elif choice == "3":
                return 1, 100, 10
            elif choice == "4":
                try:
                    min_num = int(input("Enter minimum number: "))
                    max_num = int(input("Enter maximum number: "))
                    max_attempts = int(input("Enter maximum attempts: "))
                    if min_num < max_num and max_attempts > 0:
                        return min_num, max_num, max_attempts
                    else:
                        print("❌ Invalid range or attempts!")
                except ValueError:
                    print("❌ Please enter valid numbers!")
            else:
                print("❌ Invalid choice! Please choose 1-4.")
    
    # Main game loop
    total_games = 0
    wins = 0
    
    while True:
        print("\n" + "=" * 30)
        min_num, max_num, max_attempts = choose_difficulty()
        
        won = play_game(min_num, max_num, max_attempts)
        total_games += 1
        if won:
            wins += 1
        
        print(f"\n📊 Game Statistics:")
        print(f"Games played: {total_games}")
        print(f"Games won: {wins}")
        print(f"Win rate: {(wins/total_games)*100:.1f}%")
        
        play_again = input("\n🔄 Play again? (yes/no): ")
        if play_again.lower() not in ["yes", "y"]:
            print("👋 Thanks for playing!")
            break

# =============================================================================
# PROJECT 6: STUDENT GRADE TRACKER
# =============================================================================

print("\n\n📊 PROJECT 6: STUDENT GRADE TRACKER")
print("-" * 45)

def student_grade_tracker():
    """
    A program to track and analyze student grades.
    Combines: dictionaries, lists, functions, loops, calculations
    """
    print("📊 STUDENT GRADE TRACKER")
    print("=" * 30)
    
    students = {}
    
    def add_student():
        name = input("Enter student name: ")
        if name.strip():
            students[name] = []
            print(f"✅ Added student: {name}")
        else:
            print("❌ Please enter a valid name!")
    
    def add_grade():
        if not students:
            print("❌ No students found! Add a student first.")
            return
        
        print("\nSelect student:")
        student_names = list(students.keys())
        for i, name in enumerate(student_names, 1):
            print(f"{i}. {name}")
        
        try:
            choice = int(input("Enter student number: "))
            if 1 <= choice <= len(student_names):
                student_name = student_names[choice - 1]
                grade = float(input(f"Enter grade for {student_name}: "))
                if 0 <= grade <= 100:
                    students[student_name].append(grade)
                    print(f"✅ Added grade {grade} for {student_name}")
                else:
                    print("❌ Grade must be between 0 and 100!")
            else:
                print("❌ Invalid student number!")
        except ValueError:
            print("❌ Please enter a valid number!")
    
    def calculate_average(grades):
        if not grades:
            return 0
        return sum(grades) / len(grades)
    
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
    
    def display_grades():
        if not students:
            print("❌ No students found!")
            return
        
        print("\n📊 GRADE REPORT")
        print("=" * 40)
        
        for name, grades in students.items():
            if grades:
                average = calculate_average(grades)
                letter_grade = get_letter_grade(average)
                print(f"\n👤 {name}:")
                print(f"   Grades: {grades}")
                print(f"   Average: {average:.1f}")
                print(f"   Letter Grade: {letter_grade}")
            else:
                print(f"\n👤 {name}: No grades yet")
    
    def class_statistics():
        if not students:
            print("❌ No students found!")
            return
        
        all_grades = []
        for grades in students.values():
            all_grades.extend(grades)
        
        if not all_grades:
            print("❌ No grades found!")
            return
        
        print("\n📈 CLASS STATISTICS")
        print("=" * 25)
        print(f"Total students: {len(students)}")
        print(f"Total grades: {len(all_grades)}")
        print(f"Class average: {sum(all_grades)/len(all_grades):.1f}")
        print(f"Highest grade: {max(all_grades)}")
        print(f"Lowest grade: {min(all_grades)}")
    
    def display_menu():
        print("\n📋 MENU:")
        print("1. Add student")
        print("2. Add grade")
        print("3. Display all grades")
        print("4. Class statistics")
        print("5. Exit")
    
    # Main program loop
    while True:
        display_menu()
        choice = input("\nChoose an option (1-5): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            add_grade()
        elif choice == "3":
            display_grades()
        elif choice == "4":
            class_statistics()
        elif choice == "5":
            print("👋 Thanks for using Grade Tracker!")
            break
        else:
            print("❌ Invalid choice! Please choose 1-5.")

# =============================================================================
# HOW TO USE THESE PROJECTS
# =============================================================================

print("\n\n🚀 HOW TO USE THESE PROJECTS")
print("-" * 40)

print("\n💡 Teaching Tips:")
print("1. Start with one project at a time")
print("2. Explain each part as you go through it")
print("3. Let students modify and experiment")
print("4. Encourage students to add their own features")
print("5. Use these as templates for student projects")

print("\n🎯 Project Difficulty Levels:")
print("1. Personal Info Manager - Beginner")
print("2. Quiz Game - Beginner to Intermediate")
print("3. Simple Calculator - Intermediate")
print("4. Shopping List Manager - Intermediate")
print("5. Number Guessing Game - Intermediate")
print("6. Student Grade Tracker - Advanced")

print("\n📚 Concepts Covered:")
print("✅ Variables and data types")
print("✅ User input and output")
print("✅ Functions and parameters")
print("✅ Lists and dictionaries")
print("✅ Loops and conditionals")
print("✅ Error handling")
print("✅ Program organization")

print("\n" + "=" * 60)
print("🎉 Congratulations! You now have complete Python projects!")
print("These combine all the concepts you've learned.")
print("Use them as starting points for your own creations! 🚀")
print("=" * 60)

# Uncomment the line below to run a specific project
# personal_info_manager()
# quiz_game()
# simple_calculator()
# shopping_list_manager()
# number_guessing_game()
# student_grade_tracker()

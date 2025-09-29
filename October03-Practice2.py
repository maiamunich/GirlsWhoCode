#creating a function that greets a user by name 

def greet_user(name):
    print(f"Hello," + name + "! Welcome to Girls Who Code.")

#Call the function
greet_user("Maia")
greet_user("Alyssa")
greet_user("Riley")
greet_user("Emily")
greet_user("Olivia")
greet_user("Sophia")

#create a function that adds two numbers and returns the results 
def add_numbers(a, b):
    total = a + b
    return total

#call the function and store the result 
result = add_numbers(10, 20)
print("The sum is:", result)


#Use If Statements to Print a Message Based on Age
def age_message(age):
    if age <13:
        print("You are a child.")
    elif age <18:
        print("You are a teenager.")
    else:
        print("You are an adult.")

#Call the function with different ages 
age_message(10)
age_message(15)
age_message(20)

#You can combine this wiht input() to make it interactive 
user_age = int(input("Enter your age: "))
age_message(user_age)
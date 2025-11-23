def conditional_statements():
    """If, elif, else statements"""
    print("=== Conditional Statements ===")
    
    # Basic if-else
    temperature = 25
    if temperature > 30:
        print("It's hot outside!")
    elif temperature > 20:
        print("Perfect weather!")
    else:
        print("It's cold outside!")
    
    # Multiple conditions
    age = 18
    has_license = True
    
    if age >= 18 and has_license:
        print("You can drive!")
    else:
        print("You cannot drive.")
    
    # Ternary operator
    score = 85
    result = "Pass" if score >= 50 else "Fail"
    print(f"Score: {score}, Result: {result}")

def loop_structures():
    """For and while loops"""
    print("\n=== Loop Structures ===")
    
    # For loop with range
    print("Counting 1 to 5:")
    for i in range(1, 6):
        print(i, end=" ")
    print()
    
    # For loop with list
    fruits = ["apple", "banana", "cherry"]
    print("\nFruits:")
    for fruit in fruits:
        print(f"- {fruit}")
    
    # While loop
    print("\nCountdown:")
    count = 5
    while count > 0:
        print(count)
        count -= 1
    
    # Loop with else
    print("\nSearching for number:")
    numbers = [1, 3, 5, 7, 9]
    for num in numbers:
        if num == 4:
            print("Found 4!")
            break
    else:
        print("4 not found in list")

def loop_control_statements():
    """Break, continue, pass"""
    print("\n=== Loop Control Statements ===")
    
    # Break example
    print("Break example (stop at 5):")
    for i in range(1, 11):
        if i == 6:
            break
        print(i, end=" ")
    print()
    
    # Continue example
    print("Continue example (skip even numbers):")
    for i in range(1, 11):
        if i % 2 == 0:
            continue
        print(i, end=" ")
    print()
    
    # Pass example
    print("Pass example (placeholder):")
    for i in range(3):
        pass  # TODO: Implement later
    print("Loop completed (pass used as placeholder)")

def nested_loops():
    """Loops within loops"""
    print("\n=== Nested Loops ===")
    
    # Multiplication table
    print("Multiplication Table:")
    for i in range(1, 4):
        for j in range(1, 4):
            print(f"{i} x {j} = {i*j}", end="\t")
        print()
    
    # Pattern printing
    print("\nPattern:")
    for i in range(1, 6):
        for j in range(i):
            print("*", end="")
        print()

def match_statement():
    """Python 3.10+ match statement (like switch)"""
    print("\n=== Match Statement ===")
    
    def handle_http_status(code):
        match code:
            case 200:
                return "OK"
            case 404:
                return "Not Found"
            case 500:
                return "Internal Server Error"
            case _:
                return "Unknown Status"
    
    status_codes = [200, 404, 500, 403]
    for code in status_codes:
        print(f"HTTP {code}: {handle_http_status(code)}")

def practical_examples():
    """Practical control flow examples"""
    print("\n=== Practical Examples ===")
    
    # Number guessing game
    import random
    
    def guessing_game():
        secret_number = random.randint(1, 10)
        attempts = 3
        
        print("Guess the number (1-10):")
        for attempt in range(attempts):
            guess = int(input(f"Attempt {attempt + 1}: "))
            
            if guess == secret_number:
                print("Congratulations! You guessed it!")
                break
            elif guess < secret_number:
                print("Too low!")
            else:
                print("Too high!")
        else:
            print(f"Game over! The number was {secret_number}")
    
    # Uncomment to play the game
    # guessing_game()
    
    # FizzBuzz classic problem
    print("\nFizzBuzz (1-15):")
    for i in range(1, 16):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

def error_handling_control_flow():
    """Using control flow for error prevention"""
    print("\n=== Error Handling with Control Flow ===")
    
    def safe_divide(a, b):
        if b == 0:
            return "Error: Division by zero!"
        return a / b
    
    def validate_age(age):
        if not isinstance(age, int):
            return "Error: Age must be an integer"
        elif age < 0:
            return "Error: Age cannot be negative"
        elif age > 150:
            return "Error: Age seems unrealistic"
        else:
            return f"Valid age: {age}"
    
    # Test cases
    print(safe_divide(10, 2))
    print(safe_divide(10, 0))
    
    ages = [25, -5, 200, "twenty"]
    for age in ages:
        print(validate_age(age))

if __name__ == "__main__":
    conditional_statements()
    loop_structures()
    loop_control_statements()
    nested_loops()
    match_statement()
    practical_examples()
    error_handling_control_flow()
def function_basics():
    """Basic function concepts"""
    print("=== Function Basics ===")
    
    # Simple function
    def greet():
        return "Hello, World!"
    
    # Function with parameters
    def greet_person(name):
        return f"Hello, {name}!"
    
    # Function with multiple parameters
    def introduce(name, age, city):
        return f"I'm {name}, {age} years old from {city}"
    
    print(greet())
    print(greet_person("Alice"))
    print(introduce("Bob", 25, "New York"))

def return_values():
    """Returning values from functions"""
    print("\n=== Return Values ===")
    
    def calculate_rectangle(length, width):
        area = length * width
        perimeter = 2 * (length + width)
        return area, perimeter  # Returning multiple values
    
    def is_even(number):
        return number % 2 == 0
    
    area, perimeter = calculate_rectangle(5, 3)
    print(f"Rectangle - Area: {area}, Perimeter: {perimeter}")
    
    numbers = [1, 2, 3, 4, 5, 6]
    even_numbers = [num for num in numbers if is_even(num)]
    print(f"Even numbers: {even_numbers}")

def default_arguments():
    """Functions with default arguments"""
    print("\n=== Default Arguments ===")
    
    def create_profile(name, age=30, city="Unknown", country="Unknown"):
        return f"Name: {name}, Age: {age}, City: {city}, Country: {country}"
    
    print(create_profile("Alice"))
    print(create_profile("Bob", 25))
    print(create_profile("Charlie", city="London"))
    print(create_profile("Diana", 35, "Tokyo", "Japan"))

def keyword_arguments():
    """Using keyword arguments"""
    print("\n=== Keyword Arguments ===")
    
    def describe_pet(pet_name, animal_type="dog", age=1):
        return f"I have a {animal_type} named {pet_name} who is {age} years old"
    
    # Different ways to call the function
    print(describe_pet("Buddy"))
    print(describe_pet("Whiskers", "cat"))
    print(describe_pet("Tweety", age=2))
    print(describe_pet(animal_type="bird", pet_name="Polly", age=3))

def variable_arguments():
    """*args and **kwargs"""
    print("\n=== Variable Arguments ===")
    
    # *args for variable positional arguments
    def sum_numbers(*args):
        print(f"Arguments received: {args}")
        return sum(args)
    
    print(f"Sum: {sum_numbers(1, 2, 3)}")
    print(f"Sum: {sum_numbers(10, 20, 30, 40, 50)}")
    
    # **kwargs for variable keyword arguments
    def create_car(**kwargs):
        car_info = ""
        for key, value in kwargs.items():
            car_info += f"{key}: {value}\n"
        return car_info
    
    print("Car details:")
    print(create_car(brand="Toyota", model="Camry", year=2022, color="Blue"))

def lambda_functions():
    """Anonymous lambda functions"""
    print("\n=== Lambda Functions ===")
    
    # Simple lambda
    square = lambda x: x ** 2
    print(f"Square of 5: {square(5)}")
    
    # Lambda with multiple parameters
    multiply = lambda x, y: x * y
    print(f"5 * 3 = {multiply(5, 3)}")
    
    # Using lambda with map
    numbers = [1, 2, 3, 4, 5]
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"Numbers: {numbers}")
    print(f"Squared: {squared}")
    
    # Using lambda with filter
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"Even numbers: {even_numbers}")

def function_scope():
    """Local and global scope"""
    print("\n=== Function Scope ===")
    
    global_variable = "I'm global"
    
    def test_scope():
        local_variable = "I'm local"
        print(f"Inside function: {local_variable}")
        print(f"Global access: {global_variable}")
        
        # Modifying global variable
        global global_variable
        global_variable = "Modified global"
    
    test_scope()
    print(f"Outside function: {global_variable}")
    # print(local_variable)  # This would cause an error

def decorators():
    """Function decorators"""
    print("\n=== Decorators ===")
    
    def timer_decorator(func):
        import time
        
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Function {func.__name__} took {end_time - start_time:.4f} seconds")
            return result
        return wrapper
    
    @timer_decorator
    def slow_function():
        time.sleep(1)  # Simulate slow operation
        return "Function completed"
    
    @timer_decorator
    def calculate_sum(n):
        return sum(range(n))
    
    print(slow_function())
    print(f"Sum: {calculate_sum(1000000)}")

def recursion():
    """Recursive functions"""
    print("\n=== Recursion ===")
    
    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)
    
    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)
    
    print(f"Factorial of 5: {factorial(5)}")
    print(f"Factorial of 7: {factorial(7)}")
    
    print("Fibonacci sequence (first 10 numbers):")
    for i in range(10):
        print(fibonacci(i), end=" ")
    print()

def practical_function_examples():
    """Practical function examples"""
    print("\n=== Practical Function Examples ===")
    
    def calculate_grades(students):
        """Calculate average grade for each student"""
        results = {}
        for name, grades in students.items():
            average = sum(grades) / len(grades)
            results[name] = {
                'average': average,
                'max': max(grades),
                'min': min(grades)
            }
        return results
    
    def validate_password(password):
        """Validate password strength"""
        if len(password) < 8:
            return False, "Password too short"
        if not any(char.isdigit() for char in password):
            return False, "Password needs at least one digit"
        if not any(char.isupper() for char in password):
            return False, "Password needs at least one uppercase letter"
        return True, "Password is strong"
    
    # Test grade calculator
    student_grades = {
        "Alice": [85, 90, 78],
        "Bob": [92, 88, 95],
        "Charlie": [78, 85, 80]
    }
    
    grade_results = calculate_grades(student_grades)
    for student, data in grade_results.items():
        print(f"{student}: Average = {data['average']:.2f}, "
              f"Max = {data['max']}, Min = {data['min']}")
    
    # Test password validator
    passwords = ["weak", "Weak1", "StrongPassword123"]
    for pwd in passwords:
        is_valid, message = validate_password(pwd)
        print(f"'{pwd}': {message}")

if __name__ == "__main__":
    function_basics()
    return_values()
    default_arguments()
    keyword_arguments()
    variable_arguments()
    lambda_functions()
    function_scope()
    decorators()
    recursion()
    practical_function_examples()
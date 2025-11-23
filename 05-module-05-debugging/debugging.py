def common_errors():
    """Demonstration of common errors and debugging"""
    print("=== Common Errors and Debugging ===")
    
    # 1. Syntax Error Example (Commented out to avoid stopping execution)
    print("1. Syntax Error Example:")
    # print("Hello world"  # Missing closing parenthesis
    
    # 2. Name Error
    print("\n2. Name Error Example:")
    try:
        print(undefined_variable)
    except NameError as e:
        print(f"NameError caught: {e}")
    
    # 3. Type Error
    print("\n3. Type Error Example:")
    try:
        result = "5" + 3  # Can't add string and integer
    except TypeError as e:
        print(f"TypeError caught: {e}")
    
    # 4. Value Error
    print("\n4. Value Error Example:")
    try:
        number = int("abc")  # Can't convert 'abc' to integer
    except ValueError as e:
        print(f"ValueError caught: {e}")
    
    # 5. Index Error
    print("\n5. Index Error Example:")
    try:
        my_list = [1, 2, 3]
        print(my_list[5])  # Index out of range
    except IndexError as e:
        print(f"IndexError caught: {e}")

def debugging_techniques():
    """Various debugging techniques"""
    print("\n=== Debugging Techniques ===")
    
    # Technique 1: Using print statements
    print("1. Debugging with print statements:")
    def calculate_average(numbers):
        print(f"Debug: numbers = {numbers}")  # Debug print
        total = sum(numbers)
        print(f"Debug: total = {total}")  # Debug print
        count = len(numbers)
        print(f"Debug: count = {count}")  # Debug print
        average = total / count
        print(f"Debug: average = {average}")  # Debug print
        return average
    
    scores = [85, 90, 78, 92]
    result = calculate_average(scores)
    print(f"Average score: {result}")
    
    # Technique 2: Using assertions
    print("\n2. Debugging with assertions:")
    def divide_numbers(a, b):
        assert b != 0, "Divisor cannot be zero!"
        return a / b
    
    try:
        print(divide_numbers(10, 2))
        # print(divide_numbers(10, 0))  # This would raise AssertionError
    except AssertionError as e:
        print(f"AssertionError: {e}")

def using_try_except():
    """Proper error handling with try-except"""
    print("\n=== Using Try-Except ===")
    
    def safe_divide(a, b):
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            return "Error: Cannot divide by zero!"
        except TypeError:
            return "Error: Please provide numbers only!"
    
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
    print(f"10 / 'a' = {safe_divide(10, 'a')}")

if __name__ == "__main__":
    common_errors()
    debugging_techniques()
    using_try_except()
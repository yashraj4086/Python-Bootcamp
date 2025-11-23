def welcome_message():
    """First Module - Introduction"""
    print("=== Welcome to Python ===")
    print("This is the first module")
    print("Begin your Python programming journey!")

def basic_syntax():
    """Examples of basic syntax"""
    # Variable declaration
    name = "Python Learner"
    age = 25
    
    print(f"Name: {name}")
    print(f"Age: {age}")
    
    # Simple calculation
    result = 10 + 5
    print(f"10 + 5 = {result}")

if __name__ == "__main__":
    welcome_message()
    basic_syntax()
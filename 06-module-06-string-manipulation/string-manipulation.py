def string_basics():
    """String basics and operations"""
    print("=== String Basics ===")
    
    # String creation
    greeting = "Hello, Python!"
    name = "Alice"
    
    print(f"Original string: {greeting}")
    print(f"Length: {len(greeting)}")
    print(f"Uppercase: {greeting.upper()}")
    print(f"Lowercase: {greeting.lower()}")
    print(f"Title case: {greeting.title()}")

def string_indexing_slicing():
    """String indexing and slicing"""
    print("\n=== String Indexing & Slicing ===")
    
    text = "Python Programming"
    
    print(f"Original: {text}")
    print(f"First character: '{text[0]}'")
    print(f"Last character: '{text[-1]}'")
    print(f"First 6 characters: '{text[:6]}'")
    print(f"From index 7: '{text[7:]}'")
    print(f"Every second character: '{text[::2]}'")
    print(f"Reverse: '{text[::-1]}'")

def string_methods():
    """Common string methods"""
    print("\n=== String Methods ===")
    
    sentence = "   Python is fun and powerful!   "
    print(f"Original: '{sentence}'")
    
    # Stripping whitespace
    print(f"Stripped: '{sentence.strip()}'")
    
    # Replacement
    new_sentence = sentence.replace("fun", "awesome")
    print(f"After replacement: '{new_sentence.strip()}'")
    
    # Splitting
    words = sentence.strip().split()
    print(f"Split into words: {words}")
    
    # Joining
    joined = "-".join(words)
    print(f"Joined with '-': {joined}")
    
    # Checking methods
    test_string = "Hello123"
    print(f"'{test_string}' is alpha?: {test_string.isalpha()}")
    print(f"'{test_string}' is alphanumeric?: {test_string.isalnum()}")
    print(f"'{test_string}' starts with 'Hello'?: {test_string.startswith('Hello')}")

def string_formatting():
    """Different string formatting techniques"""
    print("\n=== String Formatting ===")
    
    name = "Bob"
    age = 30
    salary = 50000.50
    
    # Old style formatting
    print("Old style: %s is %d years old" % (name, age))
    
    # str.format() method
    print("str.format(): {} is {} years old".format(name, age))
    
    # f-strings (Python 3.6+)
    print(f"f-string: {name} is {age} years old and earns ${salary:,.2f}")
    
    # Multiline f-string
    message = f"""
    Employee Information:
    Name: {name}
    Age: {age}
    Salary: ${salary:,.2f}
    """
    print(message)

if __name__ == "__main__":
    string_basics()
    string_indexing_slicing()
    string_methods()
    string_formatting()
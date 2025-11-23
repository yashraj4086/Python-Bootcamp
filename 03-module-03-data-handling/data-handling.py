def list_operations():
    """List operations and methods"""
    print("=== List Operations ===")
    
    # Creating a list
    fruits = ['apple', 'banana', 'orange', 'grape']
    print(f"Original list: {fruits}")
    
    # Adding elements
    fruits.append('mango')
    print(f"After append: {fruits}")
    
    # Removing elements
    fruits.remove('banana')
    print(f"After remove: {fruits}")
    
    # Slicing
    print(f"First two: {fruits[:2]}")
    print(f"Last two: {fruits[-2:]}")

def dictionary_operations():
    """Dictionary operations and methods"""
    print("\n=== Dictionary Operations ===")
    
    # Creating a dictionary
    student = {
        'name': 'John Doe',
        'age': 22,
        'courses': ['Math', 'Science', 'English']
    }
    
    print(f"Student data: {student}")
    print(f"Student name: {student['name']}")
    print(f"Student courses: {student['courses']}")
    
    # Adding new key-value pair
    student['grade'] = 'A'
    print(f"After adding grade: {student}")

def file_handling():
    """Basic file handling operations"""
    print("\n=== File Handling ===")
    
    # Writing to a file
    with open('sample.txt', 'w') as file:
        file.write("Hello, this is a sample file.\n")
        file.write("Python file handling is easy!\n")
    
    # Reading from a file
    with open('sample.txt', 'r') as file:
        content = file.read()
        print("File content:")
        print(content)

if __name__ == "__main__":
    list_operations()
    dictionary_operations()
    file_handling()
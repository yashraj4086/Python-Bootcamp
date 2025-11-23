def dictionary_basics():
    """Dictionary basics and creation"""
    print("=== Dictionary Basics ===")
    
    # Different ways to create dictionaries
    empty_dict = {}
    student = {"name": "Alice", "age": 20, "major": "CS"}
    using_dict = dict(name="Bob", age=22, major="Math")
    from_list = dict([("a", 1), ("b", 2), ("c", 3)])
    
    print(f"Empty: {empty_dict}")
    print(f"Student: {student}")
    print(f"Using dict(): {using_dict}")
    print(f"From list of tuples: {from_list}")

def dictionary_operations():
    """Dictionary operations and methods"""
    print("\n=== Dictionary Operations ===")
    
    person = {
        "name": "John",
        "age": 30,
        "city": "New York",
        "email": "john@example.com"
    }
    
    print(f"Original: {person}")
    
    # Accessing values
    print(f"Name: {person['name']}")
    print(f"Age: {person.get('age')}")
    print(f"Country: {person.get('country', 'Not specified')}")
    
    # Adding/Updating
    person["country"] = "USA"
    person["age"] = 31
    print(f"After updates: {person}")
    
    # Removing
    removed_email = person.pop("email")
    print(f"After pop('email'): {person}, removed: {removed_email}")
    
    last_item = person.popitem()
    print(f"After popitem(): {person}, removed: {last_item}")

def dictionary_methods():
    """Dictionary methods"""
    print("\n=== Dictionary Methods ===")
    
    inventory = {
        "apples": 10,
        "bananas": 15,
        "oranges": 8,
        "grapes": 20
    }
    
    print(f"Inventory: {inventory}")
    
    # Keys, values, items
    print(f"Keys: {list(inventory.keys())}")
    print(f"Values: {list(inventory.values())}")
    print(f"Items: {list(inventory.items())}")
    
    # Update method
    new_items = {"mangoes": 5, "apples": 12}  # Update apples
    inventory.update(new_items)
    print(f"After update: {inventory}")
    
    # Setdefault
    bananas_count = inventory.setdefault("bananas", 0)
    peaches_count = inventory.setdefault("peaches", 0)
    print(f"After setdefault: {inventory}")

def dictionary_comprehension():
    """Dictionary comprehension examples"""
    print("\n=== Dictionary Comprehension ===")
    
    # Basic comprehension
    squares = {x: x**2 for x in range(1, 6)}
    print(f"Squares: {squares}")
    
    # With condition
    even_squares = {x: x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Even squares: {even_squares}")
    
    # Transforming existing dictionary
    prices = {"apple": 1.2, "banana": 0.8, "orange": 1.5}
    discounted = {item: price * 0.9 for item, price in prices.items()}
    print(f"Discounted prices: {discounted}")
    
    # Creating from two lists
    keys = ["a", "b", "c"]
    values = [1, 2, 3]
    combined = {k: v for k, v in zip(keys, values)}
    print(f"From two lists: {combined}")

def nested_dictionaries():
    """Working with nested dictionaries"""
    print("\n=== Nested Dictionaries ===")
    
    company = {
        "employee1": {
            "name": "Alice",
            "age": 28,
            "department": "Engineering",
            "skills": ["Python", "JavaScript", "SQL"]
        },
        "employee2": {
            "name": "Bob",
            "age": 32,
            "department": "Marketing",
            "skills": ["SEO", "Content Writing", "Analytics"]
        }
    }
    
    print("Company structure:")
    for emp_id, details in company.items():
        print(f"{emp_id}:")
        print(f"  Name: {details['name']}")
        print(f"  Department: {details['department']}")
        print(f"  Skills: {', '.join(details['skills'])}")

def dictionary_use_cases():
    """Practical dictionary use cases"""
    print("\n=== Dictionary Use Cases ===")
    
    # Counting frequency
    text = "apple banana apple orange banana apple"
    words = text.split()
    
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    print(f"Word count: {word_count}")
    
    # Grouping data
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "A"},
        {"name": "Diana", "grade": "C"}
    ]
    
    grouped = {}
    for student in students:
        grade = student["grade"]
        if grade not in grouped:
            grouped[grade] = []
        grouped[grade].append(student["name"])
    
    print(f"Grouped by grade: {grouped}")

if __name__ == "__main__":
    dictionary_basics()
    dictionary_operations()
    dictionary_methods()
    dictionary_comprehension()
    nested_dictionaries()
    dictionary_use_cases()
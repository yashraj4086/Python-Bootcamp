def nested_lists():
    """Working with nested lists"""
    print("=== Nested Lists ===")
    
    # 2D List (Matrix)
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("2D Matrix:")
    for row in matrix:
        print(row)
    
    print(f"\nElement at [1][2]: {matrix[1][2]}")
    print(f"First column: {[row[0] for row in matrix]}")
    
    # 3D List
    cube = [
        [[1, 2], [3, 4]],
        [[5, 6], [7, 8]]
    ]
    print(f"\n3D Cube element [1][0][1]: {cube[1][0][1]}")

def list_of_dictionaries():
    """Lists containing dictionaries"""
    print("\n=== List of Dictionaries ===")
    
    students = [
        {"name": "Alice", "age": 20, "grades": [85, 90, 78]},
        {"name": "Bob", "age": 22, "grades": [92, 88, 95]},
        {"name": "Charlie", "age": 21, "grades": [78, 85, 80]}
    ]
    
    print("Student Database:")
    for student in students:
        print(f"{student['name']} (Age: {student['age']}) - Grades: {student['grades']}")
    
    # Calculate average grade for each student
    print("\nAverage Grades:")
    for student in students:
        avg_grade = sum(student['grades']) / len(student['grades'])
        print(f"{student['name']}: {avg_grade:.2f}")

def dictionary_of_lists():
    """Dictionaries containing lists"""
    print("\n=== Dictionary of Lists ===")
    
    company = {
        "departments": ["Engineering", "Marketing", "Sales", "HR"],
        "employees": [50, 15, 20, 8],
        "locations": ["New York", "London", "Tokyo"],
        "projects": {
            "completed": ["Website", "Mobile App"],
            "ongoing": ["AI System", "Cloud Migration"]
        }
    }
    
    print("Company Structure:")
    for key, value in company.items():
        if key != "projects":
            print(f"{key}: {value}")
    
    print("\nProjects:")
    for status, projects in company["projects"].items():
        print(f"{status}: {', '.join(projects)}")

def nested_dictionaries():
    """Dictionaries within dictionaries"""
    print("\n=== Nested Dictionaries ===")
    
    university = {
        "computer_science": {
            "head": "Dr. Smith",
            "students": 300,
            "courses": {
                "first_year": ["Programming", "Math", "Physics"],
                "second_year": ["Algorithms", "Database", "Web Dev"]
            }
        },
        "mathematics": {
            "head": "Dr. Johnson",
            "students": 150,
            "courses": {
                "first_year": ["Calculus", "Algebra", "Statistics"],
                "second_year": ["Advanced Calculus", "Number Theory"]
            }
        }
    }
    
    print("University Departments:")
    for dept, info in university.items():
        print(f"\n{dept.title()}:")
        print(f"  Head: {info['head']}")
        print(f"  Students: {info['students']}")
        print("  Courses:")
        for year, courses in info['courses'].items():
            print(f"    {year}: {', '.join(courses)}")

def complex_data_manipulation():
    """Complex operations on nested structures"""
    print("\n=== Complex Data Manipulation ===")
    
    # Sample data: Online store orders
    orders = [
        {
            "order_id": 1001,
            "customer": "Alice",
            "items": [
                {"name": "Laptop", "price": 999.99, "quantity": 1},
                {"name": "Mouse", "price": 25.50, "quantity": 2}
            ],
            "status": "delivered"
        },
        {
            "order_id": 1002,
            "customer": "Bob",
            "items": [
                {"name": "Keyboard", "price": 75.00, "quantity": 1},
                {"name": "Monitor", "price": 299.99, "quantity": 1},
                {"name": "Cables", "price": 15.00, "quantity": 3}
            ],
            "status": "processing"
        }
    ]
    
    # Calculate total for each order
    print("Order Summary:")
    for order in orders:
        total = sum(item['price'] * item['quantity'] for item in order['items'])
        print(f"Order {order['order_id']} - {order['customer']}: ${total:.2f}")
    
    # Find all products sold
    all_products = set()
    for order in orders:
        for item in order['items']:
            all_products.add(item['name'])
    
    print(f"\nAll products sold: {', '.join(all_products)}")

def list_comprehension_nested():
    """Nested list comprehensions"""
    print("\n=== Nested List Comprehensions ===")
    
    # Flatten a 2D list
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    flattened = [num for row in matrix for num in row]
    print(f"Matrix: {matrix}")
    print(f"Flattened: {flattened}")
    
    # Create multiplication table
    multiplication_table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
    print("\nMultiplication Table (1-5):")
    for row in multiplication_table:
        print(row)

if __name__ == "__main__":
    nested_lists()
    list_of_dictionaries()
    dictionary_of_lists()
    nested_dictionaries()
    complex_data_manipulation()
    list_comprehension_nested()
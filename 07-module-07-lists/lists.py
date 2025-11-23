def list_creation_indexing():
    """List creation and indexing"""
    print("=== List Creation & Indexing ===")
    
    # Different ways to create lists
    numbers = [1, 2, 3, 4, 5]
    mixed_list = [1, "hello", 3.14, True]
    empty_list = []
    from_range = list(range(1, 6))
    
    print(f"Numbers: {numbers}")
    print(f"Mixed list: {mixed_list}")
    print(f"Empty list: {empty_list}")
    print(f"From range: {from_range}")
    
    # Indexing
    print(f"\nFirst element: {numbers[0]}")
    print(f"Last element: {numbers[-1]}")
    print(f"Second to fourth: {numbers[1:4]}")

def list_methods():
    """List methods and operations"""
    print("\n=== List Methods ===")
    
    fruits = ["apple", "banana"]
    print(f"Original: {fruits}")
    
    # Adding elements
    fruits.append("orange")
    print(f"After append: {fruits}")
    
    fruits.insert(1, "grape")
    print(f"After insert at index 1: {fruits}")
    
    fruits.extend(["mango", "pineapple"])
    print(f"After extend: {fruits}")
    
    # Removing elements
    removed_fruit = fruits.pop()
    print(f"After pop(): {fruits}, removed: {removed_fruit}")
    
    fruits.remove("banana")
    print(f"After remove('banana'): {fruits}")
    
    # Other methods
    numbers = [3, 1, 4, 1, 5, 9, 2]
    print(f"\nNumbers: {numbers}")
    print(f"Count of 1: {numbers.count(1)}")
    print(f"Index of 5: {numbers.index(5)}")
    
    numbers.sort()
    print(f"Sorted: {numbers}")
    
    numbers.reverse()
    print(f"Reversed: {numbers}")

def list_comprehension():
    """List comprehension examples"""
    print("\n=== List Comprehension ===")
    
    # Basic comprehension
    squares = [x**2 for x in range(1, 6)]
    print(f"Squares: {squares}")
    
    # With condition
    even_squares = [x**2 for x in range(1, 11) if x % 2 == 0]
    print(f"Even squares: {even_squares}")
    
    # Nested comprehension
    matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
    print(f"3x3 Matrix: {matrix}")
    
    # String manipulation
    words = ["hello", "world", "python"]
    capitalized = [word.upper() for word in words]
    print(f"Capitalized: {capitalized}")

def list_operations():
    """List operations and copying"""
    print("\n=== List Operations ===")
    
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    
    # Concatenation
    combined = list1 + list2
    print(f"Concatenated: {combined}")
    
    # Repetition
    repeated = list1 * 3
    print(f"Repeated 3 times: {repeated}")
    
    # Copying lists (important!)
    original = [1, 2, 3]
    shallow_copy = original.copy()  # or original[:]
    shallow_copy[0] = 99
    
    print(f"Original: {original}")
    print(f"Shallow copy: {shallow_copy}")

if __name__ == "__main__":
    list_creation_indexing()
    list_methods()
    list_comprehension()
    list_operations()
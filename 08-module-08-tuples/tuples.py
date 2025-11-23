def tuple_basics():
    """Tuple basics and characteristics"""
    print("=== Tuple Basics ===")
    
    # Tuple creation
    empty_tuple = ()
    single_item = (42,)  # Note the comma!
    multiple_items = (1, 2, 3, 4, 5)
    mixed_tuple = (1, "hello", 3.14, True)
    
    print(f"Empty tuple: {empty_tuple}")
    print(f"Single item: {single_item}")
    print(f"Multiple items: {multiple_items}")
    print(f"Mixed tuple: {mixed_tuple}")
    
    # Without parentheses (tuple packing)
    packed = 10, 20, 30
    print(f"Packed tuple: {packed}")
    
    # Tuple unpacking
    a, b, c = packed
    print(f"Unpacked: a={a}, b={b}, c={c}")

def tuple_operations():
    """Tuple operations and methods"""
    print("\n=== Tuple Operations ===")
    
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    
    # Concatenation
    combined = tuple1 + tuple2
    print(f"Concatenated: {combined}")
    
    # Repetition
    repeated = tuple1 * 2
    print(f"Repeated: {repeated}")
    
    # Membership testing
    print(f"2 in tuple1: {2 in tuple1}")
    print(f"7 in tuple1: {7 in tuple1}")
    
    # Tuple methods
    numbers = (1, 2, 3, 2, 4, 2, 5)
    print(f"Count of 2: {numbers.count(2)}")
    print(f"Index of 4: {numbers.index(4)}")

def tuple_vs_list():
    """Comparison between tuples and lists"""
    print("\n=== Tuple vs List ===")
    
    # Memory comparison
    import sys
    
    list_example = [1, 2, 3, 4, 5]
    tuple_example = (1, 2, 3, 4, 5)
    
    print(f"List memory: {sys.getsizeof(list_example)} bytes")
    print(f"Tuple memory: {sys.getsizeof(tuple_example)} bytes")
    
    # Performance comparison
    import time
    
    # List performance
    start = time.time()
    for _ in range(1000000):
        _ = list_example[2]
    list_time = time.time() - start
    
    # Tuple performance
    start = time.time()
    for _ in range(1000000):
        _ = tuple_example[2]
    tuple_time = time.time() - start
    
    print(f"List access time: {list_time:.6f} seconds")
    print(f"Tuple access time: {tuple_time:.6f} seconds")

def tuple_use_cases():
    """Practical use cases for tuples"""
    print("\n=== Tuple Use Cases ===")
    
    # Returning multiple values from function
    def get_student_info():
        return "Alice", 20, "Computer Science"
    
    name, age, major = get_student_info()
    print(f"Student: {name}, Age: {age}, Major: {major}")
    
    # Dictionary keys (tuples can be keys, lists cannot)
    coordinates_map = {
        (40.7128, -74.0060): "New York",
        (34.0522, -118.2437): "Los Angeles"
    }
    print(f"Coordinates map: {coordinates_map}")
    
    # String formatting
    person = ("John", 25)
    print("Name: %s, Age: %d" % person)

def tuple_immutability():
    """Demonstrating tuple immutability"""
    print("\n=== Tuple Immutability ===")
    
    immutable_tuple = (1, 2, 3)
    print(f"Original tuple: {immutable_tuple}")
    
    # This would cause an error (uncomment to see):
    # immutable_tuple[0] = 99  # TypeError!
    
    # But we can create new tuples
    new_tuple = immutable_tuple + (4, 5)
    print(f"New tuple: {new_tuple}")
    
    # Nested mutable objects in tuples
    mixed = (1, 2, [3, 4])
    print(f"Mixed tuple: {mixed}")
    mixed[2][0] = 99  # This works!
    print(f"After modifying nested list: {mixed}")

if __name__ == "__main__":
    tuple_basics()
    tuple_operations()
    tuple_vs_list()
    tuple_use_cases()
    tuple_immutability()
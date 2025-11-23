def set_basics():
    """Set basics and creation"""
    print("=== Set Basics ===")
    
    # Different ways to create sets
    empty_set = set()
    numbers_set = {1, 2, 3, 4, 5}
    from_list = set([1, 2, 2, 3, 3, 4])  # Duplicates removed!
    from_string = set("hello")
    
    print(f"Empty set: {empty_set}")
    print(f"Numbers set: {numbers_set}")
    print(f"From list (duplicates removed): {from_list}")
    print(f"From string: {from_string}")

def set_operations():
    """Set operations and methods"""
    print("\n=== Set Operations ===")
    
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    
    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")
    
    # Union
    print(f"Union (A | B): {set_a | set_b}")
    print(f"Union (A.union(B)): {set_a.union(set_b)}")
    
    # Intersection
    print(f"Intersection (A & B): {set_a & set_b}")
    print(f"Intersection (A.intersection(B)): {set_a.intersection(set_b)}")
    
    # Difference
    print(f"Difference (A - B): {set_a - set_b}")
    print(f"Difference (A.difference(B)): {set_a.difference(set_b)}")
    
    # Symmetric Difference
    print(f"Symmetric Difference (A ^ B): {set_a ^ set_b}")
    print(f"Symmetric Difference (A.symmetric_difference(B)): {set_a.symmetric_difference(set_b)}")

def set_methods():
    """Set methods"""
    print("\n=== Set Methods ===")
    
    fruits = {"apple", "banana", "orange"}
    print(f"Original set: {fruits}")
    
    # Adding elements
    fruits.add("grape")
    print(f"After add('grape'): {fruits}")
    
    fruits.update(["mango", "pineapple"])
    print(f"After update: {fruits}")
    
    # Removing elements
    fruits.remove("banana")  # Raises KeyError if not found
    print(f"After remove('banana'): {fruits}")
    
    fruits.discard("watermelon")  # No error if not found
    print(f"After discard('watermelon'): {fruits}")
    
    popped = fruits.pop()
    print(f"After pop(): {fruits}, removed: {popped}")
    
    # Other methods
    colors1 = {"red", "green", "blue"}
    colors2 = {"green", "blue"}
    
    print(f"colors1: {colors1}")
    print(f"colors2: {colors2}")
    print(f"Is colors2 subset of colors1? {colors2.issubset(colors1)}")
    print(f"Is colors1 superset of colors2? {colors1.issuperset(colors2)}")
    print(f"Do they have common elements? {colors1.isdisjoint(colors2)}")

def set_comprehension():
    """Set comprehension examples"""
    print("\n=== Set Comprehension ===")
    
    # Basic comprehension
    squares = {x**2 for x in range(1, 6)}
    print(f"Squares: {squares}")
    
    # With condition
    even_squares = {x**2 for x in range(1, 11) if x % 2 == 0}
    print(f"Even squares: {even_squares}")
    
    # Removing duplicates from list
    numbers_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
    unique_numbers = {x for x in numbers_with_duplicates}
    print(f"Unique numbers: {unique_numbers}")
    
    # String processing
    sentence = "hello world python programming"
    unique_chars = {char for char in sentence if char != ' '}
    print(f"Unique characters: {unique_chars}")

def frozen_sets():
    """Immutable sets"""
    print("\n=== Frozen Sets ===")
    
    # Frozen sets are immutable
    regular_set = {1, 2, 3}
    frozen = frozenset([1, 2, 3, 4, 5])
    
    print(f"Regular set: {regular_set}")
    print(f"Frozen set: {frozen}")
    print(f"Type of frozen set: {type(frozen)}")
    
    # Frozen sets can be used as dictionary keys
    set_dict = {
        frozenset([1, 2, 3]): "first set",
        frozenset([4, 5, 6]): "second set"
    }
    print(f"Dictionary with frozen sets as keys: {set_dict}")

def practical_set_uses():
    """Practical uses of sets"""
    print("\n=== Practical Set Uses ===")
    
    # Removing duplicates
    emails = ["user@example.com", "admin@test.com", "user@example.com", "info@demo.com"]
    unique_emails = set(emails)
    print(f"Original emails: {emails}")
    print(f"Unique emails: {unique_emails}")
    
    # Membership testing (very fast!)
    large_set = set(range(1000000))
    print(f"Is 999999 in large_set? {999999 in large_set}")
    print(f"Is 2000000 in large_set? {2000000 in large_set}")
    
    # Finding common elements between lists
    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    common = set(list1) & set(list2)
    print(f"Common elements: {common}")

if __name__ == "__main__":
    set_basics()
    set_operations()
    set_methods()
    set_comprehension()
    frozen_sets()
    practical_set_uses()
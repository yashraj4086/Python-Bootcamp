def arithmetic_operators():
    """Demonstration of arithmetic operators"""
    print("=== Arithmetic Operators ===")
    
    a = 15
    b = 4
    
    print(f"a = {a}, b = {b}")
    print(f"Addition (a + b): {a + b}")
    print(f"Subtraction (a - b): {a - b}")
    print(f"Multiplication (a * b): {a * b}")
    print(f"Division (a / b): {a / b}")
    print(f"Floor Division (a // b): {a // b}")
    print(f"Modulus (a % b): {a % b}")
    print(f"Exponent (a ** b): {a ** b}")

def comparison_operators():
    """Demonstration of comparison operators"""
    print("\n=== Comparison Operators ===")
    
    x = 10
    y = 20
    
    print(f"x = {x}, y = {y}")
    print(f"x == y: {x == y}")
    print(f"x != y: {x != y}")
    print(f"x < y: {x < y}")
    print(f"x > y: {x > y}")
    print(f"x <= y: {x <= y}")
    print(f"x >= y: {x >= y}")

def logical_operators():
    """Demonstration of logical operators"""
    print("\n=== Logical Operators ===")
    
    p = True
    q = False
    
    print(f"p = {p}, q = {q}")
    print(f"p and q: {p and q}")
    print(f"p or q: {p or q}")
    print(f"not p: {not p}")
    print(f"not q: {not q}")

def assignment_operators():
    """Demonstration of assignment operators"""
    print("\n=== Assignment Operators ===")
    
    num = 10
    print(f"Initial num: {num}")
    
    num += 5  # num = num + 5
    print(f"After num += 5: {num}")
    
    num -= 3  # num = num - 3
    print(f"After num -= 3: {num}")
    
    num *= 2  # num = num * 2
    print(f"After num *= 2: {num}")
    
    num //= 4  # num = num // 4
    print(f"After num //= 4: {num}")

if __name__ == "__main__":
    arithmetic_operators()
    comparison_operators()
    logical_operators()
    assignment_operators()
def data_types_demo():
    """Practical demonstration of data types"""
    # Different data types
    integer_num = 100
    float_num = 99.99
    string_text = "Hello Python"
    boolean_val = True
    my_list = [1, 2, 3, 4, 5]
    my_tuple = (10, 20, 30)
    my_dict = {"name": "Alice", "country": "USA"}
    
    print("Data Types Demo:")
    print(f"Integer: {integer_num}, Type: {type(integer_num)}")
    print(f"Float: {float_num}, Type: {type(float_num)}")
    print(f"String: {string_text}, Type: {type(string_text)}")
    print(f"Boolean: {boolean_val}, Type: {type(boolean_val)}")
    print(f"List: {my_list}, Type: {type(my_list)}")
    print(f"Tuple: {my_tuple}, Type: {type(my_tuple)}")
    print(f"Dictionary: {my_dict}, Type: {type(my_dict)}")

def control_structures():
    """Examples of control structures"""
    print("\nControl Structures:")
    
    # If-elif-else
    score = 85
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    else:
        grade = 'C'
    print(f"Score: {score}, Grade: {grade}")
    
    # For loop
    print("Counting from 1 to 5:")
    for i in range(1, 6):
        print(i)

if __name__ == "__main__":
    data_types_demo()
    control_structures()
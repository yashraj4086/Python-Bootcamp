def file_reading_basics():
    """Basic file reading operations"""
    print("=== File Reading Basics ===")
    
    # Writing sample data to file
    with open('sample.txt', 'w') as file:
        file.write("Hello, this is a sample file.\n")
        file.write("Python file handling is powerful!\n")
        file.write("Line 3: Learning file operations\n")
        file.write("Line 4: End of file content\n")
    
    # Reading entire file
    print("Reading entire file:")
    with open('sample.txt', 'r') as file:
        content = file.read()
        print(content)
    
    # Reading line by line
    print("\nReading line by line:")
    with open('sample.txt', 'r') as file:
        for line_num, line in enumerate(file, 1):
            print(f"Line {line_num}: {line.strip()}")

def file_writing_modes():
    """Different file writing modes"""
    print("\n=== File Writing Modes ===")
    
    # Write mode ('w') - overwrites existing content
    with open('test_write.txt', 'w') as file:
        file.write("This overwrites any existing content.\n")
        file.write("New content here.\n")
    
    # Append mode ('a') - adds to existing content
    with open('test_append.txt', 'a') as file:
        file.write("First line.\n")
        file.write("Second line appended.\n")
        file.write("Third line appended.\n")
    
    # Read+Write mode ('r+')
    with open('test_rplus.txt', 'w') as file:
        file.write("Initial content\n")
    
    with open('test_rplus.txt', 'r+') as file:
        content = file.read()
        file.write("Additional content\n")
    
    print("Files created with different modes: test_write.txt, test_append.txt, test_rplus.txt")

def reading_methods():
    """Different file reading methods"""
    print("\n=== Reading Methods ===")
    
    # Create a test file
    with open('methods_test.txt', 'w') as file:
        for i in range(1, 6):
            file.write(f"This is line {i}\n")
    
    with open('methods_test.txt', 'r') as file:
        # read() - entire content
        print("Using read():")
        file.seek(0)  # Go to beginning
        print(file.read())
        
        # readline() - one line at a time
        print("\nUsing readline():")
        file.seek(0)
        print("First line:", file.readline().strip())
        print("Second line:", file.readline().strip())
        
        # readlines() - all lines as list
        print("\nUsing readlines():")
        file.seek(0)
        lines = file.readlines()
        print(f"Total lines: {len(lines)}")
        for line in lines:
            print(f"→ {line.strip()}")

def working_with_csv():
    """Working with CSV files"""
    print("\n=== CSV File Handling ===")
    import csv
    
    # Writing to CSV
    with open('students.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Name', 'Age', 'Grade', 'City'])
        writer.writerow(['Alice', '20', 'A', 'New York'])
        writer.writerow(['Bob', '22', 'B', 'London'])
        writer.writerow(['Charlie', '21', 'A', 'Tokyo'])
    
    # Reading from CSV
    print("CSV Content:")
    with open('students.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row_num, row in enumerate(reader):
            if row_num == 0:
                print(f"Headers: {', '.join(row)}")
            else:
                print(f"Row {row_num}: {row}")
    
    # Using DictReader for better access
    print("\nUsing DictReader:")
    with open('students.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"Name: {row['Name']}, Age: {row['Age']}, "
                  f"Grade: {row['Grade']}, City: {row['City']}")

def json_file_handling():
    """Working with JSON files"""
    print("\n=== JSON File Handling ===")
    import json
    
    # Data to save
    company_data = {
        "company": "Tech Corp",
        "employees": [
            {
                "id": 1,
                "name": "Alice",
                "department": "Engineering",
                "skills": ["Python", "JavaScript", "SQL"]
            },
            {
                "id": 2,
                "name": "Bob",
                "department": "Marketing",
                "skills": ["SEO", "Content Writing"]
            }
        ],
        "founded": 2020,
        "active": True
    }
    
    # Writing JSON to file
    with open('company_data.json', 'w') as jsonfile:
        json.dump(company_data, jsonfile, indent=4)
    
    # Reading JSON from file
    with open('company_data.json', 'r') as jsonfile:
        loaded_data = json.load(jsonfile)
    
    print("JSON Data loaded successfully!")
    print(f"Company: {loaded_data['company']}")
    print(f"Number of employees: {len(loaded_data['employees'])}")
    print(f"First employee: {loaded_data['employees'][0]['name']}")

def file_operations():
    """File system operations"""
    print("\n=== File Operations ===")
    import os
    import shutil
    
    # Check if file exists
    files_to_check = ['sample.txt', 'nonexistent.txt']
    for filename in files_to_check:
        exists = os.path.exists(filename)
        print(f"File '{filename}' exists: {exists}")
    
    # Get file information
    if os.path.exists('sample.txt'):
        file_stats = os.stat('sample.txt')
        print(f"\nFile info for 'sample.txt':")
        print(f"Size: {file_stats.st_size} bytes")
        print(f"Last modified: {file_stats.st_mtime}")
    
    # List files in current directory
    print("\nFiles in current directory:")
    for file in os.listdir('.'):
        if file.endswith('.txt') or file.endswith('.json') or file.endswith('.csv'):
            print(f"  {file}")
    
    # Create and remove directory
    if not os.path.exists('test_dir'):
        os.makedirs('test_dir')
        print("\nCreated directory 'test_dir'")
    
    if os.path.exists('test_dir'):
        os.rmdir('test_dir')
        print("Removed directory 'test_dir'")

def error_handling_files():
    """Error handling in file operations"""
    print("\n=== Error Handling ===")
    
    # Try to read non-existent file
    try:
        with open('nonexistent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: File not found!")
    except IOError as e:
        print(f"IOError: {e}")
    except Exception as e:
        print(f"Unexpected error: {
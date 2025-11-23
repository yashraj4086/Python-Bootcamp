"""
Student Management System
A comprehensive project demonstrating Python fundamentals
"""

class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.next_id = 1001
    
    def add_student(self, name, age, grade_level, courses=None):
        """Add a new student to the system"""
        student_id = self.next_id
        self.next_id += 1
        
        self.students[student_id] = {
            'name': name,
            'age': age,
            'grade_level': grade_level,
            'courses': courses if courses else [],
            'grades': {}
        }
        print(f"Student {name} added with ID: {student_id}")
        return student_id
    
    def enroll_course(self, student_id, course_name):
        """Enroll a student in a course"""
        if student_id not in self.students:
            print(f"Student ID {student_id} not found!")
            return False
        
        student = self.students[student_id]
        if course_name not in student['courses']:
            student['courses'].append(course_name)
            student['grades'][course_name] = None  # Initialize grade as None
            print(f"Student {student['name']} enrolled in {course_name}")
            return True
        else:
            print(f"Student already enrolled in {course_name}")
            return False
    
    def add_grade(self, student_id, course_name, grade):
        """Add or update a grade for a student in a course"""
        if student_id not in self.students:
            print(f"Student ID {student_id} not found!")
            return False
        
        student = self.students[student_id]
        if course_name not in student['courses']:
            print(f"Student not enrolled in {course_name}")
            return False
        
        if not (0 <= grade <= 100):
            print("Grade must be between 0 and 100")
            return False
        
        student['grades'][course_name] = grade
        print(f"Grade {grade} added for {student['name']} in {course_name}")
        return True
    
    def calculate_gpa(self, student_id):
        """Calculate GPA for a student"""
        if student_id not in self.students:
            print(f"Student ID {student_id} not found!")
            return None
        
        student = self.students[student_id]
        grades = [grade for grade in student['grades'].values() if grade is not None]
        
        if not grades:
            return 0.0
        
        # Convert percentage to GPA (simplified conversion)
        total_percentage = sum(grades)
        average_percentage = total_percentage / len(grades)
        gpa = (average_percentage / 100) * 4.0  # Convert to 4.0 scale
        return round(gpa, 2)
    
    def get_student_info(self, student_id):
        """Get complete information for a student"""
        if student_id not in self.students:
            print(f"Student ID {student_id} not found!")
            return None
        
        student = self.students[student_id]
        gpa = self.calculate_gpa(student_id)
        
        info = f"""
        Student ID: {student_id}
        Name: {student['name']}
        Age: {student['age']}
        Grade Level: {student['grade_level']}
        Courses: {', '.join(student['courses']) if student['courses'] else 'None'}
        GPA: {gpa}
        Grades:
        """
        
        for course, grade in student['grades'].items():
            grade_display = grade if grade is not None else "No grade"
            info += f"  {course}: {grade_display}\n"
        
        return info
    
    def list_all_students(self):
        """List all students in the system"""
        if not self.students:
            print("No students in the system")
            return
        
        print("\n=== ALL STUDENTS ===")
        for student_id, student in self.students.items():
            gpa = self.calculate_gpa(student_id)
            print(f"ID: {student_id}, Name: {student['name']}, "
                  f"Grade Level: {student['grade_level']}, GPA: {gpa}")
    
    def get_top_students(self, top_n=3):
        """Get top N students by GPA"""
        if not self.students:
            print("No students in the system")
            return
        
        students_with_gpa = []
        for student_id, student in self.students.items():
            gpa = self.calculate_gpa(student_id)
            students_with_gpa.append((student_id, student, gpa))
        
        # Sort by GPA descending
        students_with_gpa.sort(key=lambda x: x[2], reverse=True)
        
        print(f"\n=== TOP {top_n} STUDENTS ===")
        for i, (student_id, student, gpa) in enumerate(students_with_gpa[:top_n], 1):
            print(f"{i}. {student['name']} (ID: {student_id}) - GPA: {gpa}")
    
    def remove_student(self, student_id):
        """Remove a student from the system"""
        if student_id in self.students:
            student_name = self.students[student_id]['name']
            del self.students[student_id]
            print(f"Student {student_name} (ID: {student_id}) removed from system")
            return True
        else:
            print(f"Student ID {student_id} not found!")
            return False

def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("      STUDENT MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add New Student")
    print("2. Enroll Student in Course")
    print("3. Add/Update Grade")
    print("4. View Student Information")
    print("5. List All Students")
    print("6. Show Top Students")
    print("7. Remove Student")
    print("8. Exit")
    print("="*50)

def main():
    """Main program function"""
    sms = StudentManagementSystem()
    
    # Add some sample data
    sms.add_student("Alice Johnson", 16, "10th Grade", ["Math", "Science"])
    sms.add_student("Bob Smith", 17, "11th Grade", ["History", "English"])
    sms.add_student("Charlie Brown", 15, "9th Grade")
    
    # Add some grades for sample students
    sms.add_grade(1001, "Math", 92)
    sms.add_grade(1001, "Science", 88)
    sms.add_grade(1002, "History", 95)
    sms.add_grade(1002, "English", 90)
    sms.enroll_course(1003, "Art")
    sms.add_grade(1003, "Art", 85)
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            print("\n--- Add New Student ---")
            name = input("Enter student name: ").strip()
            age = int(input("Enter student age: "))
            grade_level = input("Enter grade level: ").strip()
            sms.add_student(name, age, grade_level)
        
        elif choice == '2':
            print("\n--- Enroll Student in Course ---")
            student_id = int(input("Enter student ID: "))
            course = input("Enter course name: ").strip()
            sms.enroll_course(student_id, course)
        
        elif choice == '3':
            print("\n--- Add/Update Grade ---")
            student_id = int(input("Enter student ID: "))
            course = input("Enter course name: ").strip()
            grade = float(input("Enter grade (0-100): "))
            sms.add_grade(student_id, course, grade)
        
        elif choice == '4':
            print("\n--- View Student Information ---")
            student_id = int(input("Enter student ID: "))
            info = sms.get_student_info(student_id)
            if info:
                print(info)
        
        elif choice == '5':
            sms.list_all_students()
        
        elif choice == '6':
            try:
                top_n = int(input("How many top students to show? (default 3): ") or 3)
                sms.get_top_students(top_n)
            except ValueError:
                sms.get_top_students()
        
        elif choice == '7':
            print("\n--- Remove Student ---")
            student_id = int(input("Enter student ID to remove: "))
            sms.remove_student(student_id)
        
        elif choice == '8':
            print("Thank you for using Student Management System!")
            break
        
        else:
            print("Invalid choice! Please enter a number between 1-8.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
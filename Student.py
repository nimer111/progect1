from Course import Course


class Student():
    def __init__(self, student_name, student_level):
        self.student_id = None
        self.student_name = student_name
        self.student_level = student_level
        self.student_courses = []

    def add_course(self, course):
        if course.course_level == self.student_level:
            self.student_courses.append(course)
            print("Course added successfully.")
        else:
            print("Course level doesn't match student's level.")

    def display_details(self):
        print("Name:", self.student_name)
        print("Class:", self.student_level)
        print("Courses enrolled:")
        for course in self.student_courses:
            print("- " + course.course_name)

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.next_student_id = 1
        self.next_course_id = 1

    def add_student(self, student_name, student_level):
        student = Student(student_name, student_level)
        student.student_id = self.next_student_id
        self.next_student_id += 1
        self.students.append(student)
        print("Student saved successfully.")

    def remove_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("Delete done successfully.")
                return
        print("User does not exist.")

    def edit_student(self, student_id, new_name, new_level):
        for student in self.students:
            if student.student_id == student_id:
                student.student_name = new_name
                student.student_level = new_level
                print("Edit done successfully.")
                return
        print("User does not exist.")

    def display_all_students(self):
        print("List of all students:")
        for student in self.students:
            student.display_details()

    def create_new_course(self, course_name, course_level):
        course = Course(course_name, course_level)
        course.course_id = self.next_course_id
        self.next_course_id += 1
        self.courses.append(course)
        print("Course created successfully.")

    def add_course_to_student(self, student_id, course_id):
        student_found = False
        course_found = False

        for student in self.students:
            if student.student_id == student_id:
                student_found = True
                for course in self.courses:
                    if course.course_id == course_id:
                        course_found = True
                        student.add_course(course)
                        print("Course added to student successfully.")
                        return

        if not student_found:
            print("Student does not exist.")
        elif not course_found:
            print("Course does not exist.")


school_system = SchoolSystem()

while True:
    print("\nSelect Choice Please")
    print("1. Add New Student")
    print("2. Remove Student")
    print("3. Edit Student")
    print("4. Display All Students")
    print("5. Create New Course")
    print("6. Add Course to Student")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        student_name = input("Enter student name: ")
        student_level = input("Enter student level (A-B-C): ")
        school_system.add_student(student_name, student_level)

    elif choice == "2":
        student_id = int(input("Enter student id: "))
        school_system.remove_student(student_id)

    elif choice == "3":
        student_id = int(input("Enter student id: "))
        new_name = input("Enter new name: ")
        new_level = input("Enter new level (A-B-C): ")
        school_system.edit_student(student_id, new_name, new_level)

    elif choice == "4":
        school_system.display_all_students()

    elif choice == "5":
        course_name = input("Enter course name: ")
        course_level = input("Enter course level (A-B-C): ")
        school_system.create_new_course(course_name, course_level)

    elif choice == "6":
        student_id = int(input("Enter student id: "))
        course_id = int(input("Enter course id: "))
        school_system.add_course_to_student(student_id, course_id)

    elif choice == "0":
        break

    else:
        print("Invalid choice. Please select a valid option.")



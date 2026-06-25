class Student:
    def __init__(self, roll_no, name, age, course):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")
        print("-" * 25)


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        roll_no = input("Enter Roll No: ")

        for student in self.students:
            if student.roll_no == roll_no:
                print("Student already exists!")
                return

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        course = input("Enter Course: ")

        student = Student(roll_no, name, age, course)
        self.students.append(student)

        print("Student Added Successfully!")

    def search_student(self):
        roll_no = input("Enter Roll No to Search: ")

        for student in self.students:
            if student.roll_no == roll_no:
                print("\nStudent Found:")
                student.display()
                return

        print("Student Not Found!")

    def update_student(self):
        roll_no = input("Enter Roll No to Update: ")

        for student in self.students:
            if student.roll_no == roll_no:
                student.name = input("Enter New Name: ")
                student.age = int(input("Enter New Age: "))
                student.course = input("Enter New Course: ")

                print("Student Updated Successfully!")
                return

        print("Student Not Found!")

    def delete_student(self):
        roll_no = input("Enter Roll No to Delete: ")

        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    def display_all(self):
        if not self.students:
            print("No Records Found!")
            return

        print("\nStudent Records")
        print("=" * 25)

        for student in self.students:
            student.display()


manager = StudentManager()

while True:
    print("\n===== STUDENT DATA MANAGER =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        manager.add_student()

    elif choice == "2":
        manager.search_student()

    elif choice == "3":
        manager.update_student()

    elif choice == "4":
        manager.delete_student()

    elif choice == "5":
        manager.display_all()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
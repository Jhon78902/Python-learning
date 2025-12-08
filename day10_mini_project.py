def save_student_info(name, course, goal):
    student = {
        "Name" : name,
        "Course": course,
        "Goal": goal
    }

# Save to file (inside the function)

    with open("student_info.txt","w", encoding="utf-8") as file:
     for key, value in student.items():
        file.write(f"{key}: {value}\n")

# Read back (inside the function)

    with open("student_info.txt", "r", encoding="utf-8") as file:
        print("\n---Student Information---")
        print(file.read())

# Main programe

name = input("Enter your name:")
course = input("Enter your course:")
goal = input("Enter your career goal:")

save_student_info(name, course, goal)
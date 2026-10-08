# Gradebook Management System
# Section B - Lists and Tuples

number_of_students = int(input("Enter the number of students: "))

students = []

subjects = ["Computer Technology", "Web Dev", "Systems Development"]

for i in range(number_of_students):

    name = input("Enter student name: ")

    grades = []

    for subject in subjects:

        while True:
            grade = float(input("Enter " + subject + " grade (0-100): "))

            if 0 <= grade <= 100:
                break
            else:
                print("Invalid grade. Please enter a grade between 0 and 100.")

        grades.append(grade)

    student = (name, grades)

    students.append(student)

print("\n--- Student Results ---")

for student in students:

    name = student[0]
    grades = student[1]

    average = sum(grades) / len(grades)

    print("Name:", name)
    print("Computer Technology:", grades[0])
    print("Web Dev:", grades[1])
    print("Systems Development:", grades[2])
    print("Average:", average)
    print()

    print("\n--- Highest and Lowest Grades ---")

    for i in range(len(subjects)):

        subject_grades = []

        for student in students:
            grades = student[1]
            subject_grades.append(grades[i])

        highest = max(subject_grades)
        lowest = min(subject_grades)

        print(subjects[i], "- Highest:", highest, "| Lowest:", lowest)
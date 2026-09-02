number_of_students = int(input("Enter the number of students: "))
students = []
score = []
for i in range(number_of_students):
    student_name = input("Enter the name of student {}: ".format(i+1))
    students.append(student_name)
    student_score = float(input("Enter the score of student {}: ".format(i+1)))
    score.append(student_score)
print("\n{:<20} {:<10}".format("Student Name", "Score"))
print("-" * 30)
for i in range(number_of_students):
    print("{:<20} {:<10}".format(students[i], score[i]))
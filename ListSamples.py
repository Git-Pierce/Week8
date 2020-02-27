students = [["Joel", 85, 95, 70],
            ["Anne", 95, 100, 100],
            ["Mike", 77, 70, 80, 85]]

print("students 0,0:" + students[0][0])
student = []
student.append("Test")
student.append(70)
student.append(70)
student.append(70)
students.append(student)
print(students)

# looping through movies
for student in students: # for each row
    for item in student: # for each field in a row
        print(item, end=" ; ")
    print()

student1 = ["Joe", "Jill", "Jack", "John"]
for item in student1:
    print("student: " + item, end =" , ")
print()

del student1[0]
student1.append("Joe")
print(student1)
student1.remove("Joe")
print(student1)



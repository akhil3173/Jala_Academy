# 1. Create Dictionary with 5 key-value pairs
student_dict = {}
for _ in range(5):
    key = input("Enter student ID: ")
    value = input("Enter student name: ")
    student_dict[key] = value

print("Initial dictionary:", student_dict)

# 1.1 Add values in dictionary
new_key = input("Enter new student ID to add: ")
new_value = input("Enter new student name to add: ")
student_dict[new_key] = new_value
print("After adding:", student_dict)

# 1.2 Update values in dictionary
update_key = input("Enter student ID to update: ")
update_value = input("Enter new name: ")
if update_key in student_dict:
    student_dict[update_key] = update_value
print("After updating:", student_dict)

# 1.3 Access value in dictionary
access_key = input("Enter student ID to access: ")
if access_key in student_dict:
    print("Value:", student_dict[access_key])
else:
    print("Key not found")

# 1.4 Create nested loop dictionary
nested_dict = {}
n = int(input("Enter number of students for nested dict: "))
for _ in range(n):
    sid = input("Enter student ID: ")
    courses = {}
    course_count = int(input("Enter number of courses: "))
    for _ in range(course_count):
        cname = input("Enter course name: ")
        cgrade = input("Enter course grade: ")
        courses[cname] = cgrade
    nested_dict[sid] = courses
print("Nested dictionary:", nested_dict)

# 1.5 Access values of nested dictionary
sid_access = input("Enter student ID to access in nested dict: ")
if sid_access in nested_dict:
    for course in nested_dict[sid_access]:
        print(course, ":", nested_dict[sid_access][course])
else:
    print("Student ID not found")

# 1.6 Print keys present in a dictionary
print("Keys in student_dict:", end=" ")
for key in student_dict:
    print(key, end=" ")
print()

# 1.7 Delete a value from dictionary
del_key = input("Enter student ID to delete: ")
if del_key in student_dict:
    del student_dict[del_key]
print("After deletion:", student_dict)

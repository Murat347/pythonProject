# 04/04/2021

#filepath = "/Users/assylmuratamirov/PycharmProjects/pythonProject/students.txt    # this is for mac users (i guess?)

filepath = "/Users/assylmuratamirov/PycharmProjects/pythonProject/students.txt"

# *********READING FROM FILE************

# with open(filepath) as students:
#     contents = students.read()
#     print(contents)
#
#
# with open(filepath) as students:
#     #contents = students.read()
#     print(students)
#
# with open(filepath) as students:
#     for line in students:
#     print(line, end='')

# Making a list of lines from a file

# with open(filepath, mode='r') as students: # 'r' is an optional for opening mode, r is default mode that open in READ ONLY mode
#     lines = students.readlines()

# print(lines)
# print(lines[0].strip())
# print(lines[-1])
# print("==========")
# for line in lines:
#     print(line.strip())

# *********READING FROM FILE************
with open(filepath, 'a') as students: # 'a' is for append , that appends the value to the file content, 'w' is for write, that truncates the fire and adds new content
    print("writing to the file...")
    students.write(f"\nSergey")


with open(filepath, 'r') as students: # 'r' is an optional for opening mode, r is default mode that open in READ ONLY mode
    lines = students.readlines()
    print(lines)
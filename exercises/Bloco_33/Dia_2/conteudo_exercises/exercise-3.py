in_file = open('source-for-exercise/normal-exercise-3/data-3.txt', mode='r')

content = in_file.read().split('\n')
students_list = []

for x in content:
    students_list.append(x.split(' '))

rep_students = [x[0] for x in students_list if int(x[1]) < 6]

with open("source-for-exercise/normal-exercise-3/rep_stud.txt", "w") as file:
    for y in rep_students:
        print(y, file=file)

print(file.closed)

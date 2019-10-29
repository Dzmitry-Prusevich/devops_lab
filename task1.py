# take number of students
num1 = int(input("Enter number of students: "))
listpupil = []
# take students
for i in range(num1):
    listpupil.append(input("Enter student and marks").split())
# take fio of student
fio = input("Enter fio of student for getting marks")
# calc average mark
for i in range(num1):
    if fio == listpupil[i][0]:
        # insert converation because of listpupil.append(input("Enter student and marks").split())
        sum_mark = int(listpupil[i][1]) + int(listpupil[i][2]) + int(listpupil[i][3])
        average_mark = (sum_mark) / 3
print("%.2f" %average_mark)

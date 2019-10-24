# take number of students
num1 = int(input("Enter number of students: "))
listpupil = []
# take students
for i in range(num1):
    listpupil.append(str(input("Enter student and marks")).split())
# take fio of student
fio = str(input("Enter fio of student for getting marks"))
# calc average mark
for i in range(num1):
    if fio == listpupil[i][0]:
        sum_mark = float(listpupil[i][1]) + float(listpupil[i][2]) + float(listpupil[i][3])
        average_mark = float(sum_mark) / 3
print(fio + " " + str(average_mark))

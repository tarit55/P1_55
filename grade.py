def cal_grade(avg_percentage):
    if avg_percentage > 90:
        return "A"
    elif avg_percentage >80:
        return "B"
    elif avg_percentage >70:
        return "C"
    elif avg_percentage > 60:
        return "D"
    else:
        return "F"

n = int(input("Enter the number of students= "))
students = []

for i in range(n):
    print ("Enter marks for student "+str(i+1))
    marks = []
    for j in range(6):
        mark = float(input("Semester "+str(j+1)+": "))
        marks.append(mark)
    total_marks = sum(marks)
    avg_percentage = total_marks/6 
    grade = cal_grade(avg_percentage)
    students.append({"Student":i+1,"Marks":marks,"Average_Percentage":avg_percentage,"Grade":grade})
                    
print("\nStudent Result->:")
for student in students:
    print("\nStudent "+str(student['Student'])+":")
    print("  Marks: "+str(student['Marks']))
    print("  Average Percentage: {:.2f}%".format(student['Average_Percentage']))
    print("  Grade: "+str(student['Grade']))

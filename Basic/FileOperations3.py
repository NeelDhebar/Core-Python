import statistics

std_count = int(input("Number of students: "))

def write_data(n):
    studentInfo = []
    studentMarks = []
    Agrade = {}
    Bgrade = {}
    Cgrade = {}
    
    for s in range(1, n + 1):
        name = input("\nStudent Name: ")
        roll_no = input("Roll no.: ")
        marks = []
        for i in range(1, 4):
            marks.append(int(input(f"Marks for subject {i}: ")))

        studentInfo.append(f"{roll_no}-{name}")
        studentMarks.append(f"{roll_no}-{marks[0]}-{marks[1]}-{marks[2]}")

        avg = statistics.mean(marks)
        grade = f"{roll_no}-{name}-{avg:.2f}"
        
        if avg >= 80:
            Agrade[grade] = avg    
        elif avg >= 60:
            Bgrade[grade] = avg
        elif avg >= 40:
            Cgrade[grade] = avg

    def sortByMarks(sDict):
        return sorted(sDict, key=lambda k: sDict[k], reverse=True)

    with open("studentInfo.txt", "w") as info:
        info.write("\n".join(studentInfo))

    with open("studentMarks.txt", "w") as sMarks:
        sMarks.write("\n".join(studentMarks))

    with open("Agrade.txt", "w") as a:
        a.write("\n".join(sortByMarks(Agrade)))

    with open("Bgrade.txt", "w") as b:
        b.write("\n".join(sortByMarks(Bgrade)))

    with open("Cgrade.txt", "w") as c:
        c.write("\n".join(sortByMarks(Cgrade)))

write_data(std_count)

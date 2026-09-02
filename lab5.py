'''students = {}
stdCount = int(input("Number of students: "))

for i in range(stdCount):
    rollNum = input("Roll number: ")
    name = input("Name: ")
    marks = int(input("Marks: "))
    students[rollNum] = [name, marks]

print(students)'''

l = []
eCount = int(input("Number of elements: "))
for i in range(eCount):
    l.append(int(input(f"Enter element {i + 1}: ")))

sequences = []

i = 0
while i < len(l):
    temp = [l[i]]

    j = i + 1
    while j < len(l) and l[j-1] < l[j]:
        temp.append(l[j])
        j += 1

    if len(temp) > 1:
        sequences.append(temp)

    i = j



print(sequences)

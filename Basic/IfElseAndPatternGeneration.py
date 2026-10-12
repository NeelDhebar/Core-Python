c = input("Enter a character: ")

if c == "a":
    print("You have entered a")
elif c == "b":
    print("You have entered b")
elif c == "c":
    print("You have entered c")
else:
    print("Invalid character")

n = int(input("Number: "))
C = 7
F = 1.4

if n > 0:
    if n % 2 != 0:
        print(n + C)
    elif n % 2 == 0:
        print(n * F)
elif n < 0:
    if n % 2 != 0:
        print(n - C)
    elif n % 2 == 0:
        print(n / F)

marks = int(input("Marks: "))

if marks >=90 and marks <= 100:
    print("A grade")
elif marks >=80 and marks < 90:
    print("B grade")
elif marks >=60 and marks < 80:
    print("C grade")
elif marks > 40 and marks < 60:
    print("D grade")
elif marks < 40:
    print("Fail")
elif marks > 100:
    print("Invalid marks")

rows = int(input("Number of rows: "))

for i in range(rows):
    print("1 " * (i + 1))
print()

num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, " ", end="")
        num += 1
    print()
print()

for i in range(rows, 0, -1):
    print("* " * i)
print()


for i in range(1, rows + 1):
    spaces =  rows - i
    print(" " * spaces, "* " * i)
print()

for i in range(1, rows + 1):
    spaces =  rows - i
    print(" " * spaces, "* " * i)
for i in range(rows - 1, 0, -1):
    spaces =  rows - i
    print(" " * spaces, "* " * i)
print()

number = int(input("Enter number to find the factorial of: "))

fact = 1
while number != 0:
    fact *= number
    number -= 1
print(fact)

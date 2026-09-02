listsCount = int(input("Number of lists: "))

lists = []
for i in range(listsCount):
    lists.append([])

for l in lists:
    eCount = int(input(f"No. of elements in the list: "))
    for i in range(eCount):
        e = int(input(f"Element {i + 1}: "))
        l.append(e)

def calculate(lists):

    combined = []
    combined.extend(l for l in lists)

    if len(lists) == 1:
        print(lists[0])
    elif len(lists) == 2:
        print(f"The maximum and minimum value from both lists are {max(combined)} and {min(combined)}.")
    elif len(lists) == 3:
        print(f"The sum of the lists is {sum(combined)}")
    else:
        print(combined)
                   
calculate(lists)

numbers = [i for i in range(11)]

square = map(lambda n: n**2, numbers)
print(list(square))

odd = filter(lambda x: x % 2 == 0, numbers)
print(list(odd))

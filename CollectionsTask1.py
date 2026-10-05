values = input("Enter values separated by commas: ")

str_list = []
int_list = []

for value in values.split(","):
    value = value.strip()

    try:
        value = int(value)
        int_list.append(value)
    except ValueError:
        str_list.append(value)

print("\nInteger List:", int_list)
print("Minimum:", min(int_list))
print("Maximum:", max(int_list))

str_list.reverse()

print("\nString List:", str_list)

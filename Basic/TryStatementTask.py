#1
try:
    n = int(input("Enter a number to divide by: "))
    print(5 / n)
except ValueError:
    print(f"Can't convert to type int.")
except ZeroDivisionError:
    print("Can't divide by 0.")

#2
try:
    n = int(input("Enter a number to divide by: "))
except ValueError:
    print("Can't convert to type int.")

try:
    n = int(input("Enter a number to divide by: "))
    print(5 / n)
except ZeroDivisionError:
    print("Can't divide by 0.")

#3
try:
    n = int(input("Enter a number to divide by: "))
    try:
        print(5 / n)
    except ZeroDivisionError:
        print("Can't divide by 0.")
except ValueError:
    print(f"Can't convert to type int.")

#4
try:
    n = int(input("Enter a number to divide by: "))
    try:
        print(5 / n)
    except ZeroDivisionError:
        print("Can't divide by 0.")
    finally:
        print("Finally block")
except ValueError:
    print(f"Can't convert to type int.")

#5
try:
    n = int(input("Enter a number to divide by: "))
    print(5 / n)
except ValueError:
    print(f"Can't convert to type int.")
except ZeroDivisionError:
    print("Can't divide by 0.")

try:
    l = [22, 45, 56]
    ind = int(input("Enter an index: "))
    print(l[ind])
except ValueError:
    print("Can't convert to type int.")
except IndexError:
    print("Number is out of index.")

#6
try:
    n = int(input("Enter a number to divide by: "))
    print(5 / n)
except ValueError:
    print(f"Can't convert to type int.")
except ZeroDivisionError:
    print("Can't divide by 0.")
finally:
    print("1st operation done.")

try:
    l = [22, 45, 56]
    ind = int(input("Enter an index: "))
    print(l[ind])
except ValueError:
    print("Can't convert to type int.")
except IndexError:
    print("Number is out of index.")
finally:
    print("2nd operation done.")

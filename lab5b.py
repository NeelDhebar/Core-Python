lines = int(input("Number of lines: "))

with open("test.txt", "w+") as f:
    for l in range(lines):
        f.write(input(f"Line {l + 1}: ") + "\n")

    f.seek(0,0)
    contents = f.read()

print("Total characters:", len(contents))
print("Characters without newlines:", len(contents.replace("\n", "")))
print("Characters without spaces/newlines:", len(contents.replace("\n", "").replace(" ", "")))
print("Number of lines:", len(contents.splitlines()))
print("Number of words:", len(contents.split()))

    


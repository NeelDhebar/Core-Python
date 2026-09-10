lines = int(input("Number of lines: "))

with open("demo.txt", "w+") as f:
    for l in range(lines):
        f.write(input(f"Line {l + 1}: ") + "\n")

    f.seek(0, 0)
    contents = f.read()

new_cont = "\n".join(reversed(contents.splitlines()))
print("\n" + new_cont)

with open("dummy.txt", "w") as n:
    n.write(new_cont)
            
old = input("\nWord to replace: ")
new = input("Word to replace with: ")
rep_cont = new_cont.replace(old, new)

with open("dummy.txt", "w+") as n:

    n.write(rep_cont)
    
print("\n" + rep_cont)
    

        

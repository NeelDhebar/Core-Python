s = "this is string example"

# reversed
print(s[::-1])

# words reversed
print(" ".join(s.split(" ")[::-1]))

# 2 characters interchanged

x, y = 6, 13
print("".join([s[y] if i == x else s[x] if i == y else s[i] for i in range(len(s))]))

# space split, join with "*"

print("*".join(s.split(" ")))

# replace is -> was

print(s.replace("is", "was"))

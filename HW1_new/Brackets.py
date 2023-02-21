sequence = input()
correspondence = {")":"(", "]":"[", "}":"{"}
stack = []
for i in sequence:
    if len(stack) == 0 or i not in [")", "]", "}"]:
        stack.append(i)
    elif stack[-1] == correspondence[i]:
        stack.pop()
    else:
        stack.append(i)
if len(stack) == 0:
    print("yes")
else:
    print("no")
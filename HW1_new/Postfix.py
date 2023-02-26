problem = input().split()
stack = []
operands = ['+', '-', '*']
for i in problem:
    if i not in operands:
        stack.append(int(i))
    else:
        a = stack[-2]
        b = stack[-1]
        stack.pop()
        stack.pop()
        if i == '+':
            stack.append(a + b)
        elif i == '-':
            stack.append(a - b)
        elif i == '*':
            stack.append(a * b)
print(stack[0])


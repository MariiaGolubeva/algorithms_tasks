stack = []
while True:
    stackIsEmpty = len(stack) == 0
    command = input()
    if command.split()[0] == "push":
        stack.append(command.split()[1])
        print("ok")
    elif command == "pop":
        if stackIsEmpty:
            print("error")
            continue
        print(stack.pop())
    elif command == "back":
        if stackIsEmpty:
            print("error")
            continue
        print(stack[-1])
    elif command == "size":
        print(len(stack))
    elif command == "clear":
        stack.clear()
        print("ok")
    elif command == "exit":
        print("bye")
        break
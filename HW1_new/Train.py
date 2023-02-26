deadend = []
wagons_num = int(input())
wagons = map(int, input().split())
i = 1
for w in wagons:
    deadend.append(w)
    if w == i:
        deadend.pop()
        i += 1
    for w in deadend[::-1]:
        if w == i:
            deadend.pop()
            i += 1
if len(deadend) == 0:
    print("YES")
else:
    print("NO")

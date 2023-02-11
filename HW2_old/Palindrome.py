string = input()
reversedString = string[::-1]
needsRepair = 0
half = 1
if len(string) > 1:
    half = len(string) // 2
for i in range(half):
    if string[i] != reversedString[i]:
        needsRepair += 1
print(needsRepair)

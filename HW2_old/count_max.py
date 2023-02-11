max_num = int(input())
if max_num == 0:
    print("Empty sequence")
else:
    count_max = 1
    while True:
        num = int(input())
        if num == 0:
            break
        elif num > max_num:
            max_num = num
            count_max = 1
        elif num == max_num:
            count_max += 1
    print(count_max)

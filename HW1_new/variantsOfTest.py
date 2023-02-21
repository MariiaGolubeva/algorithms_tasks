students = int(input())
variants = int(input())
petya_row = int(input())
petya_place = int(input())

petya_num = (petya_row - 1) * 2 + petya_place
if petya_num > variants:
    petya_var = petya_num % variants 
else:
    petya_var = petya_num

if petya_num + variants <= students:
    vasya_num = petya_num + variants
elif petya_num - variants > 0:
    vasya_num = petya_num - variants
else:
    vasya_num = False
    result = -1

if vasya_num:
    if vasya_num % 2 == 0:
        vasya_row = vasya_num // 2
        vasya_place = 2
    else:
        vasya_row = vasya_num // 2 + 1
        vasya_place = 1
    result = ' '.join([str(vasya_row), str(vasya_place)])

print(result)


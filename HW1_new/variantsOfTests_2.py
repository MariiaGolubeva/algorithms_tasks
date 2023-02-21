def to_global_enum(row, place):
    return 2 * row + place

def from_global_enum(enum):
    return enum // 2, enum % 2

def petya_vasya_func(students, variants, petya_row, petya_place):
    petya_row -= 1
    petya_place -= 1
    petya_enum = to_global_enum(petya_row, petya_place)

    difference = None
    if petya_enum + variants < students:
        row, _ = from_global_enum(petya_enum + variants)
        difference = abs(row - petya_row)
        vasya_enum = petya_enum + variants
    if petya_enum - variants >= 0:
        row, _ = from_global_enum(petya_enum - variants)
        if difference is None or difference > abs(row - petya_row):
            difference = abs(row - petya_row)
            vasya_enum = petya_enum - variants
    if difference is None:
        return -1
    
    row, place = from_global_enum(vasya_enum) 
    return str(row + 1) + ' ' + str(place + 1)

if __name__ == "__main__":
    students = int(input())
    variants = int(input())
    petya_row = int(input())
    petya_place = int(input())
    
    print(petya_vasya_func(students, variants, petya_row, petya_place))
x, y, z = map(int, input().split())
unambiguous = (x > 12 or y > 12 or x == y)
print(int(unambiguous))

houses = input().split()
shops = []
for i in range(10):
    if houses[i] == '2':
        shops.append(i)
min_distances = []
for i in range(10):
    if houses[i] == '1':
        distances = []
        for j in range(len(shops)):
            distances.append(abs(i - shops[j]))
        min_distances.append(min(distances))
print(max(min_distances))

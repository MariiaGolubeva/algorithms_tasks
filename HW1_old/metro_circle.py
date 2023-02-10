n, i, j = map(int, input().split())

def short_way(n, i, j):
    way1 = abs(i - j) - 1
    way2 = n - 2 - way1
    best_way = min(way1, way2)
    return best_way

print(short_way(n, i, j))
        

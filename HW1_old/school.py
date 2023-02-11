import statistics
n = int(input())
students = map(int, input().split())
print(round(statistics.median(students)))

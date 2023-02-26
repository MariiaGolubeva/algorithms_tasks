import math

def necessary_benches(bench_len, cubes_num, cubes):
    center = math.floor(bench_len / 2)
    result = []
    if bench_len % 2 != 0 and center in cubes:
        result.append(str(center))
    else:
        for i in range(cubes_num):
            if cubes[i] >= center:
                result.append(str(cubes[i - 1]))
                result.append(str(cubes[i]))
                break
    return ' '.join(result)


if __name__ == "__main__":
    bench_len, cubes_num = map(int, input().split())
    cubes = [int(x) for x in input().split()]
    print(necessary_benches(bench_len, cubes_num, cubes))

number_diego = int(input())
collection = sorted(
    list(
        set(
            map(
                int, 
                input().split()
            )
        )
    )
)
number_visitors = int(input())
restrictions = list(map(int, input().split()))

for v in range(len(restrictions)):
    visitor_limit = restrictions[v]
    stickers = 0
    for s in collection:
        if s < visitor_limit:
            stickers += 1
        else:
            break
    print(stickers)

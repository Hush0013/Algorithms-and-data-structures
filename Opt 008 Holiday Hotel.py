while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    hotel = []
    for i in range(n):
        hotel.append(list(map(int, input().split())))
    hotel.sort()
    cheapest = 10001
    for i in range(n):
        if cheapest > hotel[i][1]:
            cheapest = hotel[i][1]
            ans += 1
    print(ans)
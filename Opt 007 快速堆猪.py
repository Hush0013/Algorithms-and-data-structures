import heapq
pigs = []
weight = []
heapq.heapify(weight)
dicPig = {}
while True:
    try:
        s = input().split()
        if s[0] == 'push':
            x = int(s[1])
            pigs.append(x)
            try:
                dicPig[x] += 1
            except KeyError:
                dicPig[x] = 1
            heapq.heappush(weight, x)
        elif s[0] == 'pop':
            if len(pigs):
                x = pigs.pop()
                dicPig[x] -= 1
        else:
            if len(pigs):
                s = heapq.heappop(weight)
                while not dicPig[s]:
                    s = heapq.heappop(weight)
                heapq.heappush(weight, s)
                print(s)
    except EOFError:
        break

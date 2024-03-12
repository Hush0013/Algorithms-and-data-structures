ans = 0


def marge(arr):
    global ans
    m = len(arr)
    if m == 1:
        return arr
    mid = m // 2
    L = marge(arr[:mid])
    R = marge(arr[mid:])
    new = []
    i = j = 0
    while j < len(R) and i < len(L):
        if L[i] < R[j]:
            new.append(L[i])
            i += 1
            ans += j
        elif L[i] > R[j]:
            new.append(R[j])
            j += 1
            ans += 1
    while i < len(L):
        new.append(L[i])
        i += 1
        ans += j
    ans -= j
    while j < len(R):
        new.append(R[j])
        j += 1
    return new


while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    alist = []
    for i in range(n):
        alist.append(int(input()))
    a = marge(alist)
    print(ans)

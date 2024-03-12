#  CS101 07745
odd = []
even = []
s = list(map(int, input().split()))
for i in range(10):
    if s[i] % 2 == 0:
        even.append(s[i])
    else:
        odd.append(s[i])
odd.sort(reverse=True)
even.sort()
ans = odd + even
print(*ans)
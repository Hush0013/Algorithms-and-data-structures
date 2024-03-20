#  CS101 05345
s, add = [], 0  # s 用于存储同余数的个数
p = [2 ** (i + 1) for i in range(16)]
for i in range(16):
    s.append([0] * p[i])
n, m = map(int, input().split())
num = list(map(int, input().split()))
for i in range(n):
    for j in range(16):
        s[j][num[i] % p[j]] += 1  # 对每个2**(i+1)，将输入的数的余数存储数增加1
for j in range(16):
    for k in range(1, p[j]):
        s[j][k] += s[j][k - 1]  # 前缀和方便查询
for i in range(m):
    st = input().split()
    if st[0] == 'C':
        add += int(st[1])
    else:
        ind = int(st[1])
        al = p[ind]
        x = - (add % al) + al // 2 - 1  # 找到前缀和的前端，如果位置小于0，则增加al表示前缀和末端，同时个数补充n个
        y = x + al // 2
        print(s[ind][y] - s[ind][x] if x >= 0 else n + s[ind][y] - s[ind][x + al])

#  Openjudge 20472
x, y = 0, 0
s = input()
dire = [[0, 1], [1, 0], [0, -1], [-1, 0]]
di = 0
for d in s:
    if d == 'G':
        x += dire[di][0]
        y += dire[di][1]
    elif d == 'R':
        di += 1
        di %= 4
    else:
        di -= 1
        di %= 4
if x != 0 and y != 0 and di == 0:
    print(0)
else:
    print(1)
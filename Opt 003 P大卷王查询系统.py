#  CS101 21759
Stu = {}
n, x, y = map(int, input().split())
for _ in range(n):
    c, name, grade = input().split()
    grade = int(grade)
    try:
        Stu[name][0] += 1
        Stu[name][1] += grade
    except KeyError:
        Stu[name] = [1, grade]
m = int(input())
for _ in range(m):
    name = input()
    if Stu[name][0] >= x and y * Stu[name][0] < Stu[name][1]:
        print('yes')
    else:
        print('no')
## Project 1 Fraction 类

目前拥有计算分数加减法的功能

```python
def gcd(x, y):
    if x > y:
        x, y = y, x
    if y % x == 0:
        return x
    y %= x
    return gcd(y, x)


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        b = gcd(self.num, self.den)
        self.num //= b
        self.den //= b
        if self.den == 1:
            return str(self.num)
        else:
            return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        n_num = self.num * other.den + self.den * other.num
        n_den = self.den * other.den
        return Fraction(n_num, n_den)

    def __sub__(self, other):
        o = Fraction(-other.num, other.den)
        return self + o

    def __eq__(self, other):
        f1 = self.num * other.den
        f2 = self.den * other.num
        return f1 == f2


ans = Fraction(0, 1)
s = input()
pos = 1
l = 0
for i in range(len(s) + 1):
    if i == len(s) or s[i] == '+' or s[i] == '-':
        frac_s = s[l: i].split('/')
        frac = Fraction(int(frac_s[0]) * pos, int(frac_s[1]))
        l = i + 1
        ans += frac
    if i == len(s):
        break
    if s[i] == '+':
        pos = 1
    if s[i] == '-':
        pos = -1
print(ans)
```


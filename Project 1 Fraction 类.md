## Project 1 Fraction 类

目前拥有计算分数加减法的功能

```python
def gcd(x, y):
    if x == 0:
        return 1
    if y == 0:
        raise ZeroDivisionError('Zero can\'t be the den')
    if abs(x) > abs(y):
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

    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return Fraction(num, den)


ans = Fraction(0, 1)
s = input()
if s[-1] != '=':
    s += '='
pos = 1
l = 0
for i in range(len(s)):
    if s[i] == '=' or s[i] == '+' or s[i] == '-':
        frac_s = s[l: i].split('/')
        if len(frac_s) == 2:
            if frac_s[0] == '' or frac_s[1] == '':
                raise TypeError('"/" can\'t be the first or the last character in a member')
            try:
                frac = Fraction(int(frac_s[0]) * pos, int(frac_s[1]))
            except ValueError:
                raise ValueError('Some members contain non-numerical characters')
        elif len(frac_s) == 1:
            try:
                frac = Fraction(int(frac_s[0]) * pos, 1)
            except ValueError:
                raise ValueError('Some members contain non-numerical characters')
        else:
            raise TypeError('Some members have more than one "/"')
        l = i + 1
        ans += frac
    if s[i] == '=':
        break
    if s[i] == '+':
        pos = 1
    if s[i] == '-':
        pos = -1
print(ans)

```


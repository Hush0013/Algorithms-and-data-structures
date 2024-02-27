## Project 1 Fraction 类

目前拥有计算分数加减法的功能

```python
class Stack:  # 栈类
    def __init__(self):
        self.items = []

    def Empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)


def gcd(x, y):  # 计算两数的最大公因数
    if x == 0:
        return 1
    if abs(x) > abs(y):
        x, y = y, x
    if y % x == 0:
        return x
    y %= x
    return gcd(y, x)


class Fraction:  # 分数类
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom
        b = gcd(self.num, self.den)
        self.num //= b
        self.den //= b

    def __str__(self):
        if self.den == 1:  # 分母为1或-1时，将写成整数形式
            return str(self.num)
        if self.den == -1:
            return str(-self.num)
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

    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return Fraction(num, den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den


def make_fraction(x):  # 将整数和小数化成分数，便于直接进行计算
    if '.' in x:
        x1, x2 = x.split('.')
        xx = Fraction(int(x1) * (10 ** len(x2)) + int(x2), 10 ** len(x2))
    elif '/' in x:
        x1, x2 = map(int, x.split('/'))
        xx = Fraction(x1, x2)
    else:
        xx = Fraction(int(x), 1)
    return xx


def calculate(x, y, c):  # 定义加减乘除
    xx = make_fraction(x)
    yy = make_fraction(y)
    if c == '+':
        return str(xx + yy)
    elif c == '-':
        return str(xx - yy)
    elif c == '*':
        return str(xx * yy)
    elif c == '/':
        return str(xx / yy)


def InfixCalculator(infix):  # 将中序表达式转化为后序表达式，便于使用栈进行计算
    pre = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1, '[': 1, '{': 1}
    ch = '+-*/()[]{}'
    opens = '([{'
    closers = ')]}'
    infix = '( ' + infix + ' )'
    infix_list = infix.split()
    ans = Stack()
    s = Stack()
    for item in infix_list:
        if item not in ch and item[0] not in opens and item[-1] not in closers:
            ans.push(item)
        elif item[0] in opens and len(item) != 1:
            s.push(item[0])
            ans.push(item[1:])
        elif item in opens:
            s.push(item)
        elif item[-1] in closers:
            if len(item) != 1:
                ans.push(item[:len(item) - 1])
            while s.peek() not in opens:
                y = ans.pop()
                x = ans.pop()
                ans.push(calculate(x, y, s.pop()))
            s.pop()
        else:
            while not (s.Empty() or pre[s.peek()] < pre[item]):
                y = ans.pop()
                x = ans.pop()
                ans.push(calculate(x, y, s.pop()))
            s.push(item)
    return ans.pop()


print(InfixCalculator(input()))
```


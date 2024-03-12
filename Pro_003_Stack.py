class Stack:
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


def parChecker(st):
    opens = '([{'
    closers = ')]}'
    s = Stack()
    for i in range(len(st)):
        if st[i] in opens:
            s.push(st[i])
        elif st[i] in closers:
            if s.Empty():
                return False
            else:
                if opens.index(s.peek()) == closers.index(st[i]):
                    s.pop()
                else:
                    return False
    if s.Empty():
        return True
    else:
        return False


def BaseConverter(dec, ind):
    if ind <= 1:
        return 'Invalid index'
    re = Stack()
    while dec > 0:
        s = dec % ind
        if s < 10:
            re.push(str(s))
        else:
            re.push(chr(ord('A') + s - 10))
        dec //= ind

    ans = ""
    while not re.Empty():
        ans += re.pop()
    return ans


def InfixToPostfix(infix):
    pre = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1, '[': 1, '{': 1}
    ch = '+-*/()[]{}'
    opens = '([{'
    closers = ')]}'
    infix = '( ' + infix + ' )'
    infix_list = infix.split()
    ans_list = []
    s = Stack()
    for item in infix_list:
        if item not in ch:
            ans_list.append(item)
        elif item in opens:
            s.push(item)
        elif item in closers:
            while s.peek() not in opens:
                ans_list.append(s.pop())
            s.pop()
        else:
            while not (s.Empty() or pre[s.peek()] < pre[item]):
                ans_list.append(s.pop())
            s.push(item)
    return " ".join(ans_list)
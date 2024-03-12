class Stack:
    def __init__(self):
        self.index = []

    def Empty(self):
        return self.index == []

    def put(self, ind):
        self.index.append(ind)

    def cut(self):
        return self.index.pop()

    def show(self):
        return self.index


while True:
    try:
        st = input()
        s = Stack()
        n = len(st)
        ans = [' '] * n
        print(st)
        for i in range(n):
            if st[i] == '(':
                s.put(i)
            elif st[i] == ')':
                if s.Empty():
                    ans[i] = '?'
                else:
                    s.cut()
        while not s.Empty():
            ind_ = s.cut()
            ans[ind_] = '$'
        f = ''
        for x in ans:
            f += x
        print(f)
    except EOFError:
        break

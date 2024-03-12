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


s = input()
n = len(s)
while True:
    try:
        l = input()
        m = len(l)
        if n != m:
            print('NO')
            continue
        i = j = 0
        st = Stack()
        while i < n:
            if j < n and l[i] == s[j]:
                i += 1
                j += 1
            elif not st.Empty() and l[i] == st.peek():
                i += 1
                st.pop()
            else:
                if j == n:
                    break
                st.push(s[j])
                j += 1
        if i == n:
            print('YES')
        else:
            print('NO')

    except EOFError:
        break

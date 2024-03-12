class LogicGate:
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.calculate()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, n, pa=None, pb=None):
        super().__init__(n)
        self.pinA = pa
        self.pinB = pb

    def getPinA(self):
        if self.pinA is None:
            return int(input('Input Pin A for the binary gate ' + str(self.label) + '\n'))
        else:
            try:
                return self.pinA.getFrom().getOutput()
            except AttributeError:
                return self.pinA

    def getPinB(self):
        if self.pinB is None:
            return int(input('Input Pin B for the binary gate ' + str(self.label) + '\n'))
        else:
            try:
                return self.pinB.getFrom().getOutput()
            except AttributeError:
                return self.pinB

    def set(self, source):
        if self.pinA is None:
            self.pinA = source
        elif self.pinB is None:
            self.pinB = source
        else:
            raise RuntimeError('Error: The gate has been full')


class UnaryGate(LogicGate):
    def __init__(self, n, p=None):
        super().__init__(n)
        self.pin = p

    def getPin(self):
        if self.pin is None:
            return int(input('Input Pin for the unary gate ' + str(self.label) + '\n'))
        else:
            try:
                return self.pin.getFrom().getOutput()
            except AttributeError:
                return self.pin

    def set(self, source):
        if self.pin is None:
            self.pin = source
        else:
            raise RuntimeError('Error: The gate has been full')


class AndGate(BinaryGate):
    def __init__(self, n, pa=None, pb=None):
        super().__init__(n, pa, pb)

    def calculate(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n, pa=None, pb=None):
        super().__init__(n, pa, pb)

    def calculate(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == b == 0:
            return 0
        else:
            return 1


class NotGate(UnaryGate):
    def __init__(self, n, p=None):
        super().__init__(n, p)

    def calculate(self):
        a = self.getPin()
        return 1 - a


class Connector:
    def __init__(self, fgate, tgate):
        self.fg = fgate
        self.tg = tgate
        tgate.set(self)

    def getFrom(self):
        return self.fg

    def getTo(self):
        return self.tg


Co = []
Gates = []
print('''You are wellcome, Now this is an introduction:
In each line, you should input a GateName first, with no space between the name, and it can't be 'c' or 'p' or 'Over',
if so, just read the followings.

And then, input the type, including 'AG' for AndGate, 'OG' for OrGate and 'NG' for NotGate.
Next, if you have determined the pins, just add one or two numbers behind.
Such as 'G1 AG 1' means an AndGate named by 'G1' and one pin is 1.

If you are going to connect some of them, use 'c' as a connector.
and then input the two names of the gates, the first one's output will use as an input of the second one.
Such as 'c G1 G2'

Finally, if you want to  find out an output of a gate, input 'p' and then the name of a gate.
Such as 'p G3'

Input 'Over' to stop execution.''')
while True:
    s = input().split()
    if s[0] == 'Over':
        break
    if s[0] == 'c':
        f = None
        t = None
        for i in Gates:
            if i.label == s[1]:
                f = i
            elif i.label == s[2]:
                t = i
        x = Connector(f, t)
    elif s[0] == 'p':
        r = None
        for i in Gates:
            if i.label == s[1]:
                r = i
        print(r.getOutput())
    else:
        if len(s) == 2:
            x = y = None
        elif len(s) == 3:
            x = int(s[2])
            y = None
        else:
            x = int(s[2])
            y = int(s[3])
        if s[1] == 'AG':
            g = AndGate(s[0], x, y)
        elif s[1] == 'OG':
            g = OrGate(s[0], x, y)
        else:
            g = NotGate(s[0], x)
        Gates.append(g)




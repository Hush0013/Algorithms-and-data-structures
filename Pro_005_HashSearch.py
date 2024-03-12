def hashes(num, size):
    return num % size


def rehash(pos, size):
    return (pos + 3) % size


class HashTable:
    def __init__(self):
        self.size = 31
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value):
        hashValue = hashes(key, self.size)
        if self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.data[hashValue] = value
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = value
            else:
                next_pos = rehash(hashValue, self.size)
                while self.slots[next_pos] is not None and self.slots[next_pos] != key:
                    next_pos = rehash(next_pos, self.size)
                if self.slots[next_pos] is None:
                    self.slots[next_pos] = key
                    self.data[next_pos] = value
                else:
                    self.data[next_pos] = value

    def get(self, key):
        hashValue = hashes(key, self.size)
        data = None
        stop = False
        found = False
        next_pos = hashValue
        if self.slots[hashValue] == key:
            data = self.data[hashValue]
        while self.slots[next_pos] is not None and self.slots[next_pos] != key and not stop and not found:
            next_pos = rehash(next_pos, self.size)
            if self.slots[next_pos] == key:
                found = True
                data = self.data[next_pos]
            else:
                next_pos = rehash(next_pos, self.size)
                if next_pos == hashValue:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        return self.put(key, value)


H = HashTable()
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    H[x] = y
for i in range(n):
    x = int(input())
    print(H[x])
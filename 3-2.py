class Stack(object):
    def __init__(self):
        self.array = []
        self.min = None

    def pop(self):
        if self.array:
            to_pop = self.array[-1]
            self.array = self.array[:-1]
            if to_pop.value == self.min:
                self.min = to_pop.min
            return to_pop.value

    def push(self, value):
        if self.min == None:
            self.array += [Element(value, None)]
            self.min = value
        else:
            self.array += [Element(value, self.min)]
            if value < self.min:
                self.min = value

    def minimum(self):
        return self.min

class Element(object):
    def __init__(self, value, min):
        self.value = value
        self.min = min

if __name__ == '__main__':
    stack = Stack()
    print 'pushing 2, 3, 1, 1, 2, 1'
    to_add = [2, 3, 1, 1, 2, 1]
    for num in to_add:
        stack.push(num)
    print 'checking min then popping'
    while stack.array:
        print 'min:', stack.minimum()
        print 'popped:', stack.pop()

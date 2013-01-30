###### From 3-2.py
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
###### End 3-2.py

class Queue(object):
    def __init__(self):
        self.stack = Stack()
        self.queue = Stack()

    def enqueue(self, value):
        while self.queue.array:
            elem = self.queue.pop()
            self.stack.push(elem)
        self.stack.push(value)
        while self.stack.array:
            elem = self.stack.pop()
            self.queue.push(elem)

    def dequeue(self):
        return self.queue.pop()

if __name__ == '__main__':
    queue = Queue()
    print 'Here comes the queue 0-9'
    for num in xrange(10):
        queue.enqueue(num)
    print 'Taking them out now'
    for num in xrange(10):
        print queue.dequeue()

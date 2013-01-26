class Stack(object):
    def __init__(self):
        self.array = []
        self.two_start = 0
        self.three_start = 0

    def pop(self, stack):
        if stack == 3 and self.three_start != len(self.array):
            to_pop = self.array[-1]
            self.array = self.array[:-1]
            return to_pop
        elif stack == 2 and self.two_start != self.three_start:
            to_pop = self.array[self.three_start-1]
            self.array = self.array[:self.three_start-1] + \
                         self.array[self.three_start:]
            self.three_start -= 1
            return to_pop
        elif stack == 1 and self.two_start != 0:
            to_pop = self.array[self.two_start-1]
            self.array = self.array[:self.two_start-1] + \
                         self.array[self.two_start:]
            self.two_start -= 1
            self.three_start -= 1
            return to_pop

    def push(self, stack, value):
        if stack == 3:
            self.array += [value]
        if stack == 2:
            self.array = self.array[:self.three_start] + \
                         [value] + \
                         self.array[self.three_start:]
            self.three_start += 1
        if stack == 1:
            self.array = self.array[:self.two_start] + \
                         [value] + \
                         self.array[self.two_start:]
            self.two_start += 1
            self.three_start += 1

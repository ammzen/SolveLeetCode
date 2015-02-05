# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.mini = None
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.stack.append(x)
        if self.stack == [x]:
            self.mini = x
        elif self.mini > x:
            self.mini = x
        return x

    # @return nothing
    def pop(self):
        top = self.stack.pop()
        if top == self.mini:
            if self.stack:
                self.mini = min(self.stack)
            else:
                self.mini = None
            print 'pop1'

    # @return an integer
    def top(self):
        return self.stack[-1]

    # @return an integer
    def getMin(self):
        return self.mini

if __name__ == '__main__':
    s = MinStack()
    s.push(9)
    print s.getMin()
    s.push(0)
    print s.getMin()
    s.push(1)
    print s.getMin()
    s.push(0)
    print s.getMin()
    s.pop()
    print s.getMin()
    s.pop()
    print s.getMin()
    s.pop()
    print s.getMin()
    s.pop()
    print s.getMin()


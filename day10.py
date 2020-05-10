# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.
class MinStack(object):

    def __init__(self):
            """
            initialize your data structure here.
            """
            #self.stack = [i for i in stack]
            self.stack = []
            self.minval = sys.maxint
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x<= self.minval:
            self.stack.append(self.minval)
            self.minval = x
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: None
        """
        # if self in self.stack: 
        #     self.stack.remove(self)
        if(self.stack and self.stack.pop()==self.minval): 
            self.minval=self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        # self.stack = sorted(self.stack)
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        # self.stack =  sorted(self.stack)
        # return self.stack[0]
        return self.minval
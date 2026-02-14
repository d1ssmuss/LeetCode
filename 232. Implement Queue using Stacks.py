class MyQueue(object):

    def __init__(self):
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        return self.stack

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop(0)

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        :rtype: bool
        """
        return False if self.stack else True

# Your MyQueue object will be instantiated and called as such:
myQueue = MyQueue()
print(myQueue.push(1)) # // queue is: [1]
print(myQueue.push(2)) # // queue is: [1, 2] (leftmost is front of the queue)
print(myQueue.peek()) # // return 1
print(myQueue.pop()) # // return 1, queue is [2]
print(myQueue.empty()) # // return false
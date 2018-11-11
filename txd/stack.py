class stack(object):
    # 栈
    capacity = 10
    top = -1
    arr = [0] * capacity

    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.arr = [0] * capacity

    def push(self, param):
        self.top = self.top + 1
        if self.capacity <= self.top:
            self.extCapacity(capacity=self.capacity)
        self.arr[self.top] = param

    def pop(self):
        if self.top < 0:
            # raise RuntimeError("已经没有元素可以取了！")
            return -1
        result = self.arr[self.top]
        self.top = self.top - 1
        return result

    def extCapacity(self, capacity):
        self.arr = self.arr[:] + [0] * self.capacity
        self.capacity = capacity * 2


if __name__ == '__main__':
    stack = stack(2)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.capacity)

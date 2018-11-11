
class stack(object):
    # 栈
    capacity = 10
    top = -1
    arr = [0]*capacity

    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.arr = [0]*capacity

    def push(self, param):
        self.top = self.top+1
        self.arr[self.top] = param

    def pop(self):
        result = self.arr[self.top]
        self.top = self.top - 1
        return result


if __name__ == '__main__':
    stack = stack(20)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.capacity)

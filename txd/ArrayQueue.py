class ArrayQueue(object):

    # 初始化队列
    def __init__(self, size: int):
        self.arr = [None] * size
        self.head = 0
        self.end = 0
        self.size = size

    # 入队
    def inQueue(self, data):
        if self.size <= self.end:
            if self.head != 0:
                # 可以搬移数据
                for i in range(0, self.end-self.head):
                    self.arr[i] = self.arr[self.head+i]
                    self.arr[self.head + i] = None
                self.end = self.end-self.head
                self.head = 0
            else:
                print("队列已经满了！")
                return
        self.arr[self.end] = data
        self.end += 1


    # 出队
    def outQueue(self):
        if self.head >= self.end:
            return

        data = self.arr[self.head]
        # 清除元素
        self.arr[self.head] = None
        self.head += 1
        return data


if __name__ == '__main__':
    arr = ArrayQueue(5)
    arr.inQueue("a")
    arr.inQueue("b")
    arr.inQueue("c")
    arr.inQueue(4)

    print(arr.outQueue())
    print(arr.outQueue())
    arr.inQueue("d")
    arr.inQueue("e")
    print(arr.outQueue())
    arr.inQueue("f")
    print(arr.outQueue())
    print(arr.outQueue())

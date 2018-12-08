class Node(object):
    def __init__(self, data, next):
        self.data = data
        self.next = next


class linked(object):

    # data 为初始化的链表
    def __init__(self, data):
        # 链表头结点（基结点）
        self.head = Node(None, None)

        # 定义一个前驱结点
        prevNode = self.head

        for i in data[0:]:
            # 当前结点为Node,当前结点数据为i，指针为None
            # 当前结点的引用"指针"为node
            node = Node(i, None)

            # 前驱结点的指针指向当前结点的引用"指针"
            prevNode.next = node

            # 前驱结点 变为当前结点
            prevNode = node

    def get(self, index: object) -> object:

        # 从头结点逐个遍历
        prevNode = self.head
        i = 0
        while prevNode.next is not None:
            prevNode = prevNode.next
            if index == i:
                return prevNode.data
            i += 1
        return

    # 追加元素
    def append(self, data: object):
        # 从头结点（基结点）逐个遍历
        prevNode = self.head
        while True:
            if prevNode.next is None:
                prevNode.next = Node(data,None)
                break
            prevNode = prevNode.next

    # 删除元素
    def delete(self, index):
        # 从头结点（基结点）逐个遍历
        prevNode = self.head
        i = 0
        while prevNode.next is not None:
            # 要被删除的元素
            delNode: None = prevNode.next
            if i == index:
                prevNode.next = delNode.next
                break
            i += 1
            prevNode = delNode

    # 插入元素
    def inset(self, index, data):
        # 从头结点（基结点）逐个遍历
        prevNode = self.head
        i = 0
        # 要被添加的元素
        node = Node(data, None)
        while prevNode.next is not None:
            # 要被添加的元素位置
            currNode: None = prevNode.next
            if i == index:
                prevNode.next = node
                node.next = currNode
                break
            i += 1
            prevNode = currNode

    def printLinked(self):
        # 从头结点（基结点）逐个遍历
        prevNode = self.head
        while prevNode.next is not None:
            prevNode = prevNode.next
            print(prevNode.data, end=",")
        print("")


if __name__ == '__main__':
    linkList = linked([1, 7, 2, 9, 5])

    print(linkList.get(1))
    linkList.append(22)
    linkList.printLinked()
    print(linkList.get(4))
    print(linkList.get(5))
    print(linkList.delete(4))
    linkList.printLinked()
    print(linkList.inset(4, 55))
    linkList.printLinked()




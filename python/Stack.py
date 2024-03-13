# using list to implement stack
class Stack1:
    def __init__(self) -> None:
        self.stack = []

    def push(self, ele) -> None:
        self.stack.append(ele)

    def pop(self) -> None:
        if not self.isEmpty():
            self.stack.pop()

    def isEmpty(self) -> bool:
        return len(self.stack) == 0

    def peek(self):
        return self.stack[-1]

    def __print__(self):
        print(self.stack)


# using linkedlist to implement stack
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class Stack2:
    def __init__(self) -> None:
        self.head = None

    def push(self, data) -> None:
        n = Node(data)
        if not self.head:
            self.head = n
        else:
            n.next = self.head
            self.head = n

    def isEmpty(self) -> bool:
        return self.head is None

    def pop(self):
        if not self.isEmpty():
            pop_data = self.head.data
            self.head = self.head.next
            return pop_data
        else:
            return None

    def peek(self):
        if self.isEmpty():
            return None
        return self.head.data

    def __print__(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


if __name__ == "__main__":
    s2 = Stack2()
    print(s2.isEmpty())
    s2.push(8)
    s2.push(3)
    s2.__print__()
    s2.pop()
    s2.__print__()
    s2.push(5)
    print(s2.peek())

    s1 = Stack1()
    s1.push(8)
    s1.push(3)
    s1.__print__()
    s1.pop()
    s1.__print__()
    s1.push(5)
    print(s1.peek())

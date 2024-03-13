class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    # add new node at the tail of the linkedlist
    def append(self, data) -> None:
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # insert new node with given index
    def insert(self, index, val) -> None:
        if index >= self.length() or index == 0:
            self.append(val)
        new_node = Node(val)
        current_node = self.head
        for _ in range(index - 1):
            current_node = current_node.next
        new_node.next = current_node.next
        current_node.next = new_node

    # remove element by given index
    def remove(self, index) -> None:
        if index == 0:
            self.head = self.head.next
            return
        current_node = self.head
        prev_node = None
        for _ in range(index):
            if current_node is None:
                raise IndexError("Index out of range")
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            raise IndexError("Index out of range")
        prev_node.next = current_node.next

    # return the length og the linkedlist
    def length(self) -> int:
        l = 0
        temp = self.head
        while temp:
            l += 1
            temp = temp.next
        return l

    # print the whole the elements in the linkedlist
    def print_list(self) -> str:
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # return whether the linkedlist is null
    def isEmpty(self) -> bool:
        return self.head is None

    # return the first appear index with given value
    def indexOf(self, val) -> int:
        temp = self.head
        idx = 0
        while temp:
            if temp.data == val:
                return idx
            temp = temp.next
            idx += 1
        return -1

    # reverse the linkedlist
    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    print(linked_list.length())
    linked_list.print_list()
    linked_list.insert(2, 4)
    print(linked_list.indexOf(2))
    linked_list.print_list()
    linked_list.remove(3)
    linked_list.reverse()
    linked_list.print_list()

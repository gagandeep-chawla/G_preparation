class Node:

    def __init__(self, data):
        self.next = None
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        old_node = self.head
        while old_node.next:
            old_node = old_node.next
        old_node.next = new_node

    def prepand(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        pre_node = self.head
        self.head = new_node
        self.head.next = pre_node

    def print_list(self):
        llist = self.head
        while llist:
            print(llist.data)
            if llist.next is None:
                break
            llist = llist.next


def main():
    ll = LinkedList()
    ll.append('a')
    ll.print_list()
    ll.prepand('b')
    ll.print_list()
    ll.append('c')
    ll.print_list()
    ll.append('e')
    ll.print_list()

if __name__ == "__main__":
    main()

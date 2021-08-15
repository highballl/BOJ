# import sys, heapq

# n, m, v = map(int, sys.stdin.readline().split())
# graph = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# print(graph)

class Node(object):
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, node):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            node.prev = current
        else:
            self.head = node
    def insertNodeAtIndex(self, idx, node):
        prev_node = None
        next_node = None

        if idx == 0:
            if self.head:
                next_node = self.head
                self.head = node
                self.head.next = next_node
                next_node.prev = self.head
            else:
                self.head = node

        else:
            current_i = 0
            current = self.head
            while current_i < idx:
                if current:
                    prev_node = current
                    current = current.next
                else:
                    break
            if current_i == idx:
                node.prev = prev_node
                node.next = current
                prev_node.next = node
                if current:
                    current.prev = node
            else:
                print(-1)
                return -1

    def getDataIndex(self, data):
        current = self.head
        current_i = 0

        while current:
            if current.data == data:
                return current_i
            current = current.next
            current_i += 1
        print(-1)
        return -1
    
    def insertNodeData(self, data, node):
        index = self.getDataIndex(data)
        if index >= 0:
            self.insertNodeAtIndex(index, node)
        else:
            print(-1)
            return -1
    
    def deleteAtIndex(self, idx):
        next_node = None
        prev_node = None
        current_i = 0

        if idx == 0:
            if self.head:
                self.head = self.head.next
                self.head.prev = None
                return
            else:
                print(-1)
                return -1
        current = self.head
        
        while current_i < idx:
            if current.next:
                prev_node = current
                current = current.next
                next_node = current.next
            else:
                break
            current_i += 1
        
        if current_i == idx:
            if next_node:
                next_node.prev = prev_node
            prev_node.next = next_node
        else:
            print(-1)
            return -1

    def print(self):
        current = self.head
        string = ''
        prev_node = None
        while current:
            string += str(current.data)
            if current.next and current.prev == prev_node:
                string += '<->'
            prev_node = current
            current = current.next
        
        print(string)


if __name__ == "__main__":
    dl = DoubleLinkedList()
    dl.append(Node(1))
    dl.append(Node(2))
    dl.append(Node(3))
    dl.append(Node(4))
    dl.append(Node(6))
    dl.print()
    dl.insertNodeAtIndex(5, Node(7))
    dl.print()
    dl.insertNodeAtIndex(6, Node(5))
    dl.print()
    dl.deleteAtIndex(6)
    dl.print()
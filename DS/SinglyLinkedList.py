"""
    SLL 클래스
    1. append
    2. display
    3. search
    4. pop
    5. insert
    6. remove
"""
class Node:
    def __init__(self, data = 0):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
        self.length = 0
    
    def __len__(self):
        return self.length
    
    def append(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            prev = self.head
            while prev.next:
                prev = prev.next
            prev.next = node
        self.length += 1
    
    def display(self):
        if self.head == None:
            print("Empty List")
        else:
            node = self.head
            while node.next:
                print(node.data, end = " -> ")
                node = node.next
            print(node.data)
    
    def search(self, data):
        node = self.head
        while node:
            if node.data == data:
                return True
            node = node.next
        return False

    def insert(self, i, data):
        if i >= self.length:
            self.append(data)
        else:
            prev = self.head
            for _ in range(i - 1):
                prev = prev.next
            node = Node(data)
            node.next = prev.next #prev.next의 값은 그 다음 값을 의미
            prev.next = node # prev.next는 값이 아닌 공간 즉, 전노드가 어떤 것을 가르켜야하는지
            self.length += 1


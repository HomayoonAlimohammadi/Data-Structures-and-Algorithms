from sklearn.feature_selection import SelectFdr


class Node:

    def __init__(self, value):

        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):

        result = f'''
        value: {self.value},
        next: {self.next},
        prev: {self.prev}'''
        return result

    def __repr__(self):

        result = f'Node {self.value}, next: {self.next}, prev: {self.prev}'


class DoublyLinkedList:

    def __init__(self, value):

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):

        new_node = Node(value)
        tail = self.tail
        tail.next = new_node
        new_node.prev = tail
        self.tail = new_node
        self.length += 1

    def prepend(self, value):

        new_node = Node(value)
        head = self.head
        head.prev = new_node
        new_node.next = head
        self.head = new_node
        self.length += 1

    def insert(self, index, value):

        self.checkIndexInRange(index)

        if index == 0 or index >= self.length:
            print('Please user Prepend or Append Instead')
        else:
            before = self.getNodeByIndex(index-1)
            after = self.getNodeByIndex(index)
            new_node = Node(value)
            before.next = new_node
            new_node.prev = before
            after.prev = new_node
            new_node.next = after
            self.length += 1

    def pop(self, index=None):

        if index is None: 
            index = self.length - 1
        self.checkIndexInRange(index)
        if index == self.length - 1:
            old_tail = self.tail
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                new_tail = old_tail.prev
                self.tail = new_tail
                new_tail.next = None
            self.length -= 1
            del old_tail
        elif index == 0:
            old_head = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                new_head = old_head.next
                new_head.prev = None
                self.head = new_head
            self.length -= 1
            del old_head
        else:
            del_node = self.getNodeByIndex(index)
            before = self.getNodeByIndex(index - 1)
            after = self.getNodeByIndex(index + 1)
            before.next = after
            after.prev = before
            del del_node
            self.length -= 1

    def set(self, index, value):

        self.checkIndexInRange(index)
        node = self.getNodeByIndex(index)
        node.value = value

    def getNodeByIndex(self, index):

        self.checkIndexInRange(index)
        temp = self.head
        i = 0
        while i != index:
            i += 1
            temp = temp.next

        return temp

    def checkIndexInRange(self, index):
        
        if index < 0 or index >= self.length:
            raise IndexError('Index not in DoublyLinkedList range')

    def __str__(self):
        if self.length == 0:
            return 'None   |   Length: 0'
        result = 'DoublyLinkedList: '
        temp = self.head
        result += 'None <-- '
        while temp.next:
            result += str(temp.value) + ' <--> '
            temp = temp.next
        result += f'{temp.value} --> None   |   Length: {self.length}'
        return result



l = DoublyLinkedList(10)
print(l)
l.append(1000)
print(l)
l.prepend(2)
print(l)
l.pop()
print(l)
l.insert(1, 100)
print(l)
l.pop()
l.pop()
print(l)
l.pop()
print(l)


    

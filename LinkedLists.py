class Node:

    def __init__(self, value):

        self.value = value
        self.next = None

    def __str__(self):
        result = f'''[
    value: {self.value},
    next: {self.next}
]'''
        return result

class LinkedList:

    def __init__(self, value):

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):

        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def prepend(self, value):

        new_node = Node(value)
        last_head = self.head
        self.head = new_node
        self.head.next = last_head
        self.length += 1

    def insert(self, index, value):

        if index == 0 or index == self.length - 1:
            print('Please use Append or Prepend instead.')
        else:
            new_node = Node(value)
            before = self.getNodeByIndex(index-1)
            after = self.getNodeByIndex(index)
            new_node.next = after
            before.next = new_node
            self.length += 1

    def pop(self, index=''):

        if index == 0:
            del_node = self.head
            self.head = del_node.next
            del del_node
        elif index == '': 
            node = self.getNodeByIndex(self.length - 2)
            node.next = None
            del self.tail
            self.tail = node
        else:
            before = self.getNodeByIndex(index-1)
            after = self.getNodeByIndex(index+1)
            before.next = after
        self.length -= 1

    def getNodeByIndex(self,index):

        if index < 0 or index >= self.length:
            raise IndexError('Index out of range.')
        if index == 0:
            return self.head
        elif index == self.length - 1:
            return self.tail
        temp = self.head
        i = 0
        while temp.next:
            if i == index:
                return temp
            i += 1
            temp = temp.next
        return temp

    def __str__(self):

        temp = self.head
        result = str(temp.value) + ' --> '
        while temp.next:
            temp = temp.next
            result += str(temp.value) + ' --> '
        result += f'None  |  Length: {self.length}'
        return result


linked_list = LinkedList(1)
linked_list.append(10)
linked_list.prepend(20)
linked_list.insert(1, 30)
linked_list.pop(0)


print(linked_list)
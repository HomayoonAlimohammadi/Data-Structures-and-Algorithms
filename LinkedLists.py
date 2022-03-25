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

    def __repr__(self):
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

    def set_value(self, index, value):
        node = self.getNodeByIndex(index)
        node.value = value

    def reverse(self):
        if self.length > 1:
            temp = self.head
            after = self.head.next
            # print(f'{temp=}')
            # print(f'{after=}')
            temp.next = None
            self.tail = temp
            while after.next:
                after_after = after.next
                after.next = temp
                temp = after
                after = after_after
            after.next = temp
            self.head = after


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
linked_list.insert(2,50)
linked_list.pop(0)


print(linked_list)
linked_list.reverse()
print(linked_list)
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
    def __str__(self,):
        return f'''value: {self.value}
        next: [{self.next}]'''
    
    def __repr__(self):
        return f'Value: {self.value}, Next: [{self.next}]'


class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1

    def enqueue(self, value):
        new_node = Node(value)
        self.last.next = new_node
        self.last = new_node
        self.length += 1
        return self

    def dequeue(self):
        if self.length == 0:
            print('No items in the Queue.')
            return None

        if self.length == 1:
            self.first = None
            self.last = None
            return_node = None
            
        else:

            ## Optional -- Making return_node a new_node
            return_node = Node(self.first.value)
        
            self.first = self.first.next

        self.length -= 1
        return return_node

    def __str__(self):
        temp = self.first
        result = ''
        while temp.next:
            result += f'{temp.value}, '
            temp = temp.next
        result += f'{temp.value}    |   Length: {self.length}'
        return result


queue = Queue(10)
print(queue)
queue.enqueue(20)
print(queue)
for i in range(30, 100, 10):
    queue.enqueue(i)
print(queue)
dequeue_node = queue.dequeue()
print(dequeue_node)
print(queue)

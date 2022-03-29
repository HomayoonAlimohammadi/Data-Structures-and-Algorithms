class Node:
    def __init__(self, value):
        self.value = value
        self.next = None\

    def __str__(self):
        return f'''[
            value: {self.value}
            next: {self.next}
            ]'''
        
    def __repr__(self):
        return f'''[
            value: {self.value}
            next: {self.next}
            ]'''
        

class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.length = 1

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1
        return self

    def pop(self):
        if self.length == 0:
            print('No items left in the Stack.')
            return self
        elif self.length == 1:
            self.top = None
        else:
            self.top = self.top.next
        self.length -= 1
        return self

    def __str__(self):
        if self.length == 0:
            return 'Length: 0'
        temp = self.top
        result = ''
        while temp.next:
            result += f'{temp.value} --> '
            temp = temp.next
        result += f'{temp.value}    |   Length: {self.length}'
        return result

    def __repr__(self):
        if self.length == 0:
            return 'Length: 0'
        temp = self.top
        result = ''
        while temp.next:
            result += f'{temp.value} --> '
            temp = temp.next
        result += f'{temp.value}    |   Length: {self.length}'
        return result


def main():
    stack = Stack(10)
    print(stack)
    stack.push(20)
    print(stack)
    stack.push(100)
    print(stack)
    stack.pop()
    print(stack)
    print(stack.pop())
    print(stack)
    print(stack.pop())
    print(stack.pop())


if __name__ == '__main__':
    main()
class Node:

    def __init__(self, value, ends_num):
        self.value = value
        self.children = []
        self.ends_num = ends_num

    def getChildrenValues(self):
        return [node.value for node in self.children]

    def getChildNodeByValue(self, value):
        for node in self.children:
            if node.value == value:
                return node

        raise NameError(f'Node "{value}" not in "{self.value}" children')

    def __str__(self):
        result = f'{{\nValue: {self.value}, Ends No.: {self.ends_num}\n Children: ['
        for child in self.children:
            result += str(child) + '\n'
        result += ']}'

        return result

class Trie:

    def __init__(self, value='""'):
        new_node = Node(value, 0)
        self.root = new_node
        self.total_number_subsets = 0

    def insertWord(self, word):
        
        current_node = self.root

        for i,char in enumerate(word):

            ends_num = 1 if i == len(word)-1 else 0

            # print(f'current node: "{current_node.value}" with children: "{current_node.getChildrenValues()}"')
            if char not in current_node.getChildrenValues():
                new_node = Node(char, ends_num)
                current_node.children.append(new_node)
                # print(f'added "{char}" to "{current_node.value}" children')
                current_node = new_node
                

            else:
                # print(f'switched to "{current_node.value}" child "{char}"')
                current_node = current_node.getChildNodeByValue(char)
                current_node.ends_num += ends_num

    def findParentWords(self, word):
        '''
        Find number the words which our input is a subset of.
        '''
        raise NotImplementedError
        



    def __str__(self):
        return f'Root: {self.root}'     

    
def main():

    trie = Trie()
    trie.insertWord('salam')
    trie.insertWord('salmon')
    trie.insertWord('sobhi')
    trie.insertWord('sal')
    trie.insertWord('sob')
    trie.insertWord('sobh')
    print(trie)



if __name__ == '__main__':
    main()
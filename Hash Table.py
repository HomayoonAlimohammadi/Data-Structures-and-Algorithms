from time import time
from random import sample, shuffle

class HashTable:
    def __init__(self, num_cells = 7):
        self.cells = [[] for i in range(num_cells)]
        self.num_cells = num_cells

    def custom_hash(self, key):
        hashed_key = sum([ord(char) for char in str(key)]) % self.num_cells
        return hashed_key

    def generic_hash(self, key):
        return hash(key)

    def set_item(self, key, value, method='custom'):

        '''
        Set <key> = <value> in the hash table.
        Hash <method> will effect the results.
        '''

        if method == 'custom':
            cell_num = self.custom_hash(key)

        elif method == 'generic':
            cell_num = self.generic_hash(key)

        else:
            print('Invalid input for <method> arguement. It must be <generic> or <custom>.')    
            return self

        if self.get_item(key) is None:
            self.cells[cell_num].append([key, value])
        else:
            for stored_data in self.cells[cell_num]:
                if key == stored_data[0]:
                   stored_data[1] = value 
        return self

    def get_item(self, key, method='custom'):

        '''
        Lookup for a given <key> in the hash table.
        Hash <method> will effect the results.
        Returns None in case of absence.
        '''

        if method == 'custom':
            cell_num = self.custom_hash(key)

        elif method == 'generic':
            cell_num = self.generic_hash(key)
            
        else:
            print('Invalid input for <method> arguement. It must be <generic> or <custom>.')
            return None   

        for stored_key, stored_value in self.cells[cell_num]:
            if key == stored_key:
                return stored_value
        
        ### Optional
        # print('No key, value pair found for the input key. try changing the hash method.')
        
        return None

    def __str__(self):
        result = ''
        for i, cell in enumerate(self.cells):
            result += f'Cell No. {i}: {cell}\n'
        return result


ht = HashTable()
ht.set_item('name', 'homayoon')
ht.set_item('age', 1)
ht.set_item(2000, 1378)
ht.set_item(2000, 2000)
ht.set_item(2000, 1378)
ht.set_item('age', 2000)
ht.set_item('homayoon', 2000)
ht.set_item('nooshin', 1999)
ht.set_item('homayoon_love', 'nooshin')
ht.set_item('nooshin_love', 'homayoon')
print(ht)

### Interview Question:

list1 = sample(list(range(1_00000)), 10000)
list2 = sample(list(range(1_00000)), 10000)
shuffle(list1)
shuffle(list2)

### Check to see if list2 items exist in list1

### Bad Approach: O(n^2)
t0 = time()
for item2 in list2:
    for item1 in list1:
        if item1 == item2:
            # print(item2, True)
            break
    else:
        # print(item2, False)
        pass

print(time() - t0) # About 5.5 seconds!
### Good Approach: O(n)

print()

t0 = time()
my_dict = {key: True for key in list1}
for item in list2:
    result = my_dict.get(item, False)
    # print(item, result)

print(time() - t0) # About 0.002 seconds!
        
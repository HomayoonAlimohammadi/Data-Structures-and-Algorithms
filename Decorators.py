def meta(power):
    def list_add(func):
        def inner(list_of_tuples):
            return [func(val[0], val[1]) ** power for val in list_of_tuples]
        return inner
    return list_add

@meta(power=2)
def add(a, b):
    return a + b


print(add([(1,2), (3,4)]))
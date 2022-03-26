### Towards Data Science Tutorial

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

### Another Tutoriall

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped
@make_bold
@make_italic
@make_underline
def hello():
    return "hello world"
print(hello()) ## returns "<b><i><u>hello world</u></i></b>"

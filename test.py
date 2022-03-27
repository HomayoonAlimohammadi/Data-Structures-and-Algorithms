from typing import List

def f(a: int = 10) -> list:
    print(a)

print(f.__annotations__)
f()
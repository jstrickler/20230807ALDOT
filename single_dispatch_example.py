from functools import singledispatch

@singledispatch
def handle(value):
    raise TypeError(f"Invalid type {type(value).__name__}")

@handle.register(int)
def _(value):
    print(f"Handling integer {value}")

@handle.register(float)
def _(value):
    print(f"Handling float {value}")

@handle.register(str)
def _(value):
    print(f"Handling str {value}")

@handle.register(list)
def _(value):
    print(f"Handling list {value}")

a = 5
b = 10.2
c = "abc"
d = [1, 2, 3]

for v in a, b, c, d:
    handle(v)


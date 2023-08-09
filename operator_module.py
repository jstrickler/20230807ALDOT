import operator as op

a = 10
b = 8
c = a + b
print(f"c: {c}")

c = op.add(a, b)
print(f"c: {c}")
 
def doit(j, k, func):
    result = func(j, k)
    return result

d = doit(20, 40, op.add)
print(f"d: {d}")

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(op.getitem(fruits, 8))   # same as fruits[8]




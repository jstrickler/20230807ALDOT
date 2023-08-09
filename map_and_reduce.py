from timeit import Timer
from functools import reduce
from operator import add

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

f1 = map(str.upper, fruits)
print(f"list(f1): {list(f1)}\n")

f1 = map(str.upper, fruits)
for fruit in f1:
    print(fruit, end=' ')
print("\n\n")

numbers = [5, -8, 47, 19, -2, -20, 8, 18]

an = map(abs, numbers)
print(f"list(an): {list(an)}")

an = [abs(n) for n in numbers]
print(f"an: {an}\n")

an = (abs(n) for n in numbers)
print(f"list(an): {list(an)}\n")

setup = "numbers = [5, -8, 47, 19, -2, -20, 8, 18]"
code1 = "list(map(abs, numbers))"
code2 = "[abs(n) for n in numbers]"
code3 = "list(abs(n) for n in numbers)"

for code in code1, code2, code3:
    t = Timer(code, setup)
    print(t.timeit())
print('-' * 60)


#  reduce(func, values)
total = reduce(add, numbers)   # same as sum()
print(total)
print(sum(numbers))










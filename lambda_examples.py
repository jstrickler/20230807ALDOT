

def doit(func):
    print(f"func: {func}")
    print(f"type(func): {type(func)}")
    
    result = func()
    return result

def apple():
    return 42

x = doit(apple)
print(f"x: {x}")

y = doit(lambda : 100)
print(f"y: {y}")

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

sorted_fruits = sorted(fruits, key=lambda f: (f[-1], f[0]))
print(f"sorted_fruits: {sorted_fruits}")





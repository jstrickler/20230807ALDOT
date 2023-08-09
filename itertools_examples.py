import itertools as it

for s in it.repeat("Python rocks!", 10):
    print(s)

fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

fgen = (f.upper() for f in fruits)
print(f"fgen: {fgen}\n")
f_slice = it.islice(fgen, 0, 5)
print(f"f_slice: {f_slice}\n")
print(f"list(f_slice): {list(f_slice)}")


alpha = [1, 2, 3]
beta = 4, 5, 6
gamma = "789"

for value in it.chain(alpha, beta, gamma):
    print(value, end=" ")
print("\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'), 
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Ada', 'Lovelace', 'Analytical Engine', '1815-12-10'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for value in it.chain.from_iterable(people):
    print(value)
print()






fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
         "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear", "banana",
         "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry", "lychee",
         "grape"]

f1 = sorted(fruits, key=str.lower)
print(f"f1: {f1}\n")

f2 = sorted(fruits, key=len)
print(f"f2: {f2}\n")

def custom_sort(item):
    sort_value = len(item), item.lower()
    print(f"comparing '{item}' as '{sort_value}'")
    return sort_value

f3 = sorted(fruits, key=custom_sort)
print(f"f3: {f3}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Guido', 'van Rossum', 'Python', '1956-01-31'),
    ('Thomas', 'Kurtz', 'BASIC', '1928-02-28'),
    ('Grace', 'Hopper', 'COBOL', '1906-12-09'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Ada', 'Lovelace','Babbage calculator', '1815-12-10'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

def by_dob(p):
    return p[3]

for person in sorted(people, key=lambda p: p[3]):
    print(person)

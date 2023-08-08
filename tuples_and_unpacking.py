colors = 'red', 'green', 'purple'
factors = 5, 9, 4.3

print(colors[0])
print(factors[2])

person = "Bill", "Gates", "Microsoft", "1955-10-28"

print(person[0], person[1])

# iterable unpacking
first_name, last_name, product, dob = person

print(first_name, last_name)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
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
    ('Linus', 'Torvalds', 'Linux', 'git', '1969-12-28'),
]

print(people[0])
print(people[0][0])

for person in people:
    print(person[0], person[1])
print()

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, dob, product)


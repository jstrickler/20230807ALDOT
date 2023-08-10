
names = ['Larry', 'Harry', 'Barry', 'Mary', 'Kerry']

unames = [name.upper() for name in names]  # list comprehension
print(f"unames: {unames}\n")

#  (EXPR for VAR in ITERABLE if CONDITION ...)
uname_gen = (name.upper() for name in names)   # generator expression
print(f"uname_gen: {uname_gen}\n")


print(f"next(uname_gen): {next(uname_gen)}")
print(f"next(uname_gen): {next(uname_gen)}")
print(f"next(uname_gen): {next(uname_gen)}")
print()

for name in uname_gen:
    print(name)
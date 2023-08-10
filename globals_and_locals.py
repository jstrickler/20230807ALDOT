import sys
import operator

color = "red"
value = 123.456

def spam():
    print("spam spam spam")

g = globals()
print(f"g: {g}")

print(f"g['color']: {g['color']}")


g['cat'] = "Felix"

print(f"cat: {cat}")

func_name = "spam"

g[func_name]()


def ham():
    x = 10
    y = 25
    print(f"locals(): {locals()}")
    
ham()
print('-' * 60)

print(f"dir(ham): {dir(ham)}\n")


print(f"type(ham): {type(ham)}")

ham.color = "pink"
ham.ocean = "Atlantic"

print(f"dir(ham): {dir(ham)}")

print(f"ham.color: {ham.color}")







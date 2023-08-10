from president import President
from EXAMPLES import geometry 

p = President(18)
print(f"p: {p}")
print(f"p.first_name: {p.first_name}")
print(f"p.last_name: {p.last_name}")

ln = getattr(p, "last_name")
print(f"ln: {ln}")

print(f"hasattr(p, 'party'): {hasattr(p, 'party')}")
print(f"hasattr(p, 'wombat'): {hasattr(p, 'wombat')}")

x = [1, 2, 3]
print(f"hasattr(x, '__next__'): {hasattr(x, '__next__')}")
print(f"hasattr(x, '__iter__'): {hasattr(x, '__iter__')}")

def  fn(self):
    return f"{self.first_name} {self.last_name}"

setattr(President, "full_name", fn)

print(f"p.full_name(): {p.full_name()}")




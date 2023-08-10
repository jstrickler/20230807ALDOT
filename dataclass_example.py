from dataclasses import dataclass


@dataclass
class President:
    first_name: str
    last_name: str
    party: str

p = President('Theodore', 'Roosevelt', 'Republican')
print(f"p: {p}")
print(f"p.first_name: {p.first_name}")
print('-' * 60)

print(dir(p))
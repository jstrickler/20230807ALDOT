from math import pi as PI
import typing as T

Numeric = T.Union[int, float, str]


def circle_area(diameter: Numeric) -> float:
    if isinstance(diameter, (str, bytes)):
        print("Weird. I got a string")
        return 0
    return PI * ((diameter / 2) ** 2)

print(circle_area(10))

print(circle_area("wombat"))
print(circle_area(5.9))

color: str = "blue"

color = 25

print(f"color: {color}")

print(f"circle_area.__annotations__: {circle_area.__annotations__}")
print('-' * 60)

print(dir(color))

class Dog:
    ENEMY: "Cat"

class Cat:
    pass

def groom(dog: Dog):
    pass


def parse_logs(logs: T.Iterable[str]) -> bool:
    for log in logs:
        print("parsing...")


def spam(items: T.Iterable[Numeric]) -> Numeric:
    pass

def eggs(arg1: T.Any) -> T.Any:
    pass

values: T.Iterable[Numeric] = 1, 2, 3, 4.5

bad_values: T.Iterable[Numeric] = ["a", "b", "c"]

def toast(thing: T.Optional[str]) -> T.Optional[str]:
    pass

# def toast(thing: int) -> T.Optional[str]: ...

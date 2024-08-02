# learned from https://fastapi.tiangolo.com/python-types/#python-types-intro

from typing import Optional


def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e


def process_items(items: list[str]):
    for item in items:
        print(item)


def process_items2(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s


def process_items3(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)


def process_item(item: int | str):
    print(item)


def say_hi(name: Optional[str] = None):
    if name is not None:
        print


# calling say_hi3() will raise a type error
# only say_hi(name=None) is valid
def say_hi3(name: Optional[str]):
    print(f"Hey {name}!")


def say_hi4(name: str | None = None):
    print(f"Hey {name}!")


class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


# call all functions with examples
print(get_full_name("john", "doe"))
print(get_name_with_age("john", 25))
print(get_items("item_a", 1, 2.5, True, b"bytes"))
process_items(["item_a", "item_b", "item_c"])
print(process_items2((1, 2, "three"), {b"one", b"two", b"three"}))
print(process_items3({"item_a": 1.99, "item_b": 2.99, "item_c": 3.99}))
print(process_item("item_a"))
print(process_item(1))
print(say_hi())
print(say_hi("John"))
print(say_hi(None))
print(say_hi3(None))
print(say_hi3("John"))
print(say_hi4())
print(say_hi4("John"))

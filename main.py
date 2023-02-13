from dataclasses import dataclass
from typing import Optional, Union


@dataclass
class User:
    name: str
    age: int
    email: Optional[str] = None

    def greet(self) -> str:
        return f"Hello, my name is {self.name}"

    """ Added method for adding two User instances together """

    def __add__(self, other):
        return User(name=f"{self.name} + {other.name}", age=self.age + other.age)


""" Changed the function to use the new __add__ method for adding two user instances together """


def add(a: Union[int, float, User], b: Union[int, float, User]) -> Union[int, float, User]:
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, User) and isinstance(b, User):
        return a + b
    else:
        raise TypeError("Inputs must be either numbers or User instances")


if __name__ == "__main__":
    user = User("Den", 25, "den_25@gmail.com")

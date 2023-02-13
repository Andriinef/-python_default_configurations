from typing import Union

def add(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    return a + b


if __name__ == "__main__":
    sum = add(5, 6.2)
    print(sum)
    
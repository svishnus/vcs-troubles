def func_1(a: str, b: str) -> str:
    return a + b


def func_2(a: str, b: str) -> str:
    return b + a


def test():
    print(func_1("a", "b"))
    print(func_2("a", "b"))


if __name__ == "__main__":
    test()

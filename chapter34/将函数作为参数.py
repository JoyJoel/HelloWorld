def func_1():
    x = 10

    def func_2():
        x = 20
        return x + 10
    return func_2()


print(func_1())


def func_1():
    x = 10

    def func_2():
        nonlocal x  # 使用非本地x
        return x + 10
    return func_2()


print(func_1())

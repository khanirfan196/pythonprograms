def smart_divide(func):
    def inner(a, b):
        print("Inner function has been called..")
        if b == 0:
            print("Whoops! cannot divide")
            return
        else:
            print("I am going to divide", a, "and", b)
            x = a / b
            return func(None, None, x)

    return inner


@smart_divide
def divide(a, b, x):
    print(x)


divide(9, 3)
divide(10, 5)

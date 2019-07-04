# e.g. of closure
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)
    return inner_func


if __name__ == "__main__":

    res_func = outer_func('Hello')
    res_func()  # -> <function outer_func.<locals>.inner_func at 0x7fb4ff06eea0> (remembers outer scope)


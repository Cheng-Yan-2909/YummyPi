import time


class MyData:
    """

    """

    data: dict = None

    def __init__(self, *, data):
        self.data = data

    def add_data(self, *, key, value):
        self.data[key] = value

    def __setitem__(self, key, value):
        self.add_data(key=key, value=value)


class DefaultVal:
    default_val = {}

def test_default_arg_value(now=time.time()):
    print(f"now is: {now}")



def test():
    my_data1 = DefaultVal()
    my_data2 = DefaultVal()
    my_data3 = DefaultVal()
    print(f"my_data1: {id(my_data1.default_val)}")
    print(f"my_data2: {id(my_data2.default_val)}")
    print(f"my_data3: {id(my_data3.default_val)}")

    print("=============================================")

    test_default_arg_value()
    test_default_arg_value()
    test_default_arg_value()

test()


import time


class MyData:
    """
        class doc... describe the class here
    """

    data: dict = None

    def __init__(self, *, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = data

    def add_data(self, *, key, value):
        self.data[key] = value

    def __setitem__(self, key, value):
        self.add_data(key=key, value=value)

    def __getitem__(self, item):
        if item in self.data:
            return self.data[item]
        return None


class DefaultVal:
    default_val = {}

def test_default_arg_value(now=time.time()):
    print(f"now is: {now}")


def test_default_arg_value2(data={}):
    print(f"data is @: {id(data)}")


def test_argument(primitive_type, object_type):
    print("inside of 'test_argument' method")
    print(f" - primitive_type value: {primitive_type}")
    print(f" - object_type value: {object_type}")
    print("changing both values")
    primitive_type += 1
    object_type.append("efgh")
    print("after data changed")
    print(f" - primitive_type value: {primitive_type}")
    print(f" - object_type value: {object_type}")


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

    print("=============================================")
    test_default_arg_value2()
    test_default_arg_value2()
    test_default_arg_value2()

    print("=============================================")
    primitive_data = 3
    object_data = ["abcd"]
    test_argument(primitive_data, object_data)
    print("after the function call to 'test_argument'")
    print(f" - primitive_data: {primitive_data}")
    print(f" - object_data: {object_data}")

    print("=============================================")
    my_data = MyData()
    my_data["test"] = "works"

    print(f"my_data.data: {my_data.data}")

test()


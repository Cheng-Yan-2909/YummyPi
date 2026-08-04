import time


class Jobs:
    """
        class doc... describe the class here
    """

    available_jobs = [
        "teacher", "principal", "administrator"
    ]

    teacher = None
    principal = None
    administrator = None


    def add_data(self, *, key, value):
        if not key in self.available_jobs:
            return
        setattr(self, key, value)

    def __setitem__(self, key, value):
        self.add_data(key=key, value=value)

    def __getitem__(self, item):
        if item in self.available_jobs:
            return getattr(self, item)
        return None

    def __str__(self):
        s = ""
        for job in self.available_jobs:
            s = f"{s}, {job}={getattr(self, job)}"
        return s


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

##################################################################

class SingletonClass:
    _singleton_instance_name_ = "_singleton_instance_name_"

    def __new__(cls, *args, **kwargs):
        try:
            instance_name = f"{SingletonClass._singleton_instance_name_}_{cls.__module__}_{cls.__name__}"
        except:
            instance_name = f"{SingletonClass._singleton_instance_name_}_{cls.__name__}"

        singleton_instance = getattr(cls, instance_name, None)

        if singleton_instance is None:
            singleton_instance = super(SingletonClass, cls).__new__(cls)
            setattr(cls, instance_name, singleton_instance)

        return singleton_instance

class TestSingleton1(SingletonClass): pass

class TestSingleton2(SingletonClass): pass


##################################################################

decorated_method = []
def my_decorator(func):
    print(f"wrapping func: {func.__name__}")
    decorated_method.append(func)
    return func

def test_func_wrap():
    print("======== test_func_wrap ========= ")
    global decorated_method
    decorated_method = []
    def _my_func():
        print("I am my_func")

    global my_func
    my_func = my_decorator( _my_func )

def test_decorator():
    print("======== test_decorator ========= ")
    global decorated_method
    decorated_method = []

    global my_func
    @my_decorator
    def my_func():
        print("I am my_func")



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
    job = Jobs()
    job["test"] = "testing job"
    job["teacher"] = "science"
    job["principal"] = "Bob"
    print(f"job of 'teacher': {job['teacher']}")
    print(f"my_job: {job}")

    print("=============================================")
    print(f"Singleton instance 1 id: {id(TestSingleton1())}")
    print(f"Singleton instance 1 id: {id(TestSingleton1())}")
    print(f"Singleton instance 1 id: {id(TestSingleton1())}")
    print(f"Singleton instance 2 id: {id(TestSingleton2())}")
    print(f"Singleton instance 2 id: {id(TestSingleton2())}")
    print(f"Singleton instance 2 id: {id(TestSingleton2())}")

    print("=============================================")
    test_decorator()
    print("Calling 'my_func' -- ", end="")
    my_func()
    for func in decorated_method:
        print("Calling from 'decorated_method' list: ", end="")
        func()

    test_func_wrap()
    print("Calling 'my_func' -- ", end="")
    my_func()
    for func in decorated_method:
        print("Calling from 'decorated_method' list: ", end="")
        func()

    print("=============================================")
    print("Globals")
    for k, v in globals().items():
        print(f"{k} ==> {v}")



test()


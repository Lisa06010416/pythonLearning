# ----- static_method -----
class Test():
    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

    @staticmethod
    def static_method():
        # 不能使用 class 內的 self
        # self.value => error
        # 可以不被初始化成實例使用
        print("I am static method!")


# Test.get_value() # TypeError: get_value() missing 1 required positional argument: 'self'
Test.static_method()

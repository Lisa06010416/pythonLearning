

# ----- class_method -----
class Test():
    value_a = 123

    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

    def static_method(self): # 沒有用到需要init的參數
        print("I am static method!")

    @classmethod
    def classmethod_method(cls):
        # 可以調用class裡面的方法以及變數
        # 但在class初始化前不能使用會需要init的方法以及變數
        # 常用來實體化類別 ex 模型讀取pretrain weight
        print(cls.value_a)
        print("I am classe method!")

    @classmethod
    def classmethod_method_print_init_val(cls):
        print(cls.value)


Test.classmethod_method()
# Test().classmethod_method()


# ----- class_method -----
class Date():
    def __init__(self, year: str, month: str, date: str):
        self.year = year
        self.month = month
        self.day = date

    @ classmethod
    def get_date(cls, str: str):
        import re
        a = re.split(r"[_\-|/.\\]", str)
        print(a)
        return cls(a[0],a[1],a[2])

    def print_date(self):
        print("year: {}, Month: {}, Day: {}".format(self.year, self.month, self.day))

print("\nclassmethod used:")
date = Date.get_date(r"2020\11\12")
date.print_date()




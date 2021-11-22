# ----------------------------------------
# a normal class
class selftest():
    def __init__(self):
        print("self 指向創建的實例 :")
        print(self)

        print("self 的 class :")
        print(self.__class__)

        self.a = {"0":1}
        print("可以直接拿到 instance 裡面的資料 ：")
        print(self.__dict__)

    def getself(self):
        return self

testobject = selftest()
testobject.b = "321" # 新增b
self = testobject.getself()
print(self.__dict__)
self.c = "3123123"  # 新增c
print(self.__dict__)
print()



# ----------------------------------------
# 一個物件只要有 下面幾個函式 ， 就可以像list和dict一樣 調用len(object) , object[0], object[0] =1 , del object[0]
# （1）__len__(self)
#  (2)__getitem__(self,key)
#  (3)__setitem__(self,key,value)
#  (4)__delitem__(self,key)

# a class inheret dict
class selftest_dict(dict):
    def __init__(self):
        print("self 指向創建的實例 :")
        print(self)

        print("self 的 class :")
        print(self.__class__)

        self.a = {"0":1}
        print("可以直接拿到 instance 裡面的資料 ：")
        print(self.__dict__)

    def print_self_len(self):
        print("print_self_len :")
        print(len(self))

    def is_self(self):
        if not self:
            print("self in empty")


# self => 指向創建的實例

t = selftest_dict()

# 新增資料
t.print_self_len()
t.__setitem__("a","123")
t['b'] = "321"
t.print_self_len()


# ----------------------------------------
# 可以修改 fun Name
def NewType(name, tp):
    def new_type(x):
        return x

    new_type.__name__ = name
    new_type.__supertype__ = tp
    return new_type

B = NewType("B",NewType)
print("\n modify function Name")
print(B(123))
print(B)


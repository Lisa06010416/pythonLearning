# learn from https://medium.com/@dboyliao/%E6%B7%BA%E8%AB%87-python-metaclass-dfacf24d6dd5
# metaclass 的使用時機大多是在實現一個 framework，
# 而你希望透過 metaclass 去控制使用者自定義的 class 是否有符合某些條件，
# 譬如說正確 overwrite 某些 method 等等時可以用；
# 另外就是實現一些特殊的語意，譬如說 python 的 enum 模組裡面的許多 class
# 都是用 metaclass 實現的。

class Meow():
    def __init__(self, color: str, cid: int):
        self.color = color
        self.id = cid

    def print_color(self):
        print(self.color)


cat1 = Meow("三花", 0)

# isinstance() 子類會屬於父類
print(isinstance(Meow, object))  # true
print(issubclass(Meow, object))  # true

# python 裡內建的 metaclass 就是 type
print(isinstance(type, object))  # true
print(issubclass(type, object))  # true

# metaclass type 的 type: -> type
print(type(type) == type)

# ----- 自定義 Metaclass -----
# type.__new__(mcls, name, base, attribs)
# mcls: metaclass 物件本身 => type 本身 不用自己傳
# name: 要被創建的 class 的名字
# base: 要被創建的 class 所繼承的其他 class
# attribs: 要被創建的 class 本身的各項 attribute

MyMeow = type(
    'MyMeow',
    (object,),
    {
        'color': "black",
        'print_color': lambda self, color: print(color)
    }
)
a = MyMeow()
a.print_color("red")
print(a)


# ----- 用 MyMeta 來建立 Class -----
class MyMeta(type):
    def __new__(mcls, name, base, attribs):
        name = 'Meow' + name
        return super().__new__(mcls, name, base, {'print_color': lambda self, color: print(color)})


class MyClass(object, metaclass=MyMeta):
    def meow_func(self):
        return "meow!meow!meow!"


# 多了print_color function
MyClass().print_color('yellow')
# 出現 error 'MeowMyClass' object has no attribute 'meow_func'
# 且 class 名稱 變為 MeowMyClass
MyClass().meow_func()

# tyoing
# python 3.5 以上版本
# 方便檢查function input與output的type
from typing import List, Union



# ----- 1 -----
print("基本的標註輸入與輸出的type :")


def typing_hello(name: str) -> None:
    print("Hello~{}".format(name))


typing_hello("Lisa")


# # ----- Type alases -----
print("\nType alases :")

name_list = List[str]


def repeat_name(names: name_list) -> name_list:
    return names * 2


names = repeat_name(["Lisa", "Meow"])
print(names)
names = repeat_name([1, 2])  # 不會error 但是會有提醒
print(names)
names = repeat_name([1, 2, "names"])  # 只要有一個str 就過惹 List[Union(str,int)]
print(names)


# ----- NewType -----
# NewType -> 回傳一個 function name 為 name，父類別為tp的函式，該function會回傳輸入的值
# def NewType(name, tp):
#     def new_type(x):
#         return x
#
#     new_type.__name__ = name
#     new_type.__supertype__ = tp
#     return new_type
print("\nNewType :")
from typing import NewType

UserId = NewType('UserId', int)  # UserId實際上只是一個函式，因此不能直接創建其子類
# class A(UserId):
#     def __init__(self): # super class is missing
#         pass
Meow = NewType('Meow', UserId)  # 但可以用NewType創建繼承UserId的子類function

# new_type(x) -> return x
s = UserId(123) + UserId(321)
print(s)

# ****** Type alases vs new type ******
# Type alases => 使得 A 完全等於 B，如果B是很複雜的類型的話，可以簡化程式
# NewType => 使得A為B的子類，因此在做類型判斷時A!=B，防止程式錯誤
# ************

name_list1 = NewType('UserId', List[int])
def repeat_name2(names: name_list1) -> List[int]:
    return names * 2
repeat_name2(["123",1]) #

# ----- TypeVar -----
# 定義一個類別的變數，用在不能事先確定要傳入的類別時
# 可以指定哪些是同樣的類別
from typing import TypeVar

t1 = TypeVar('t1') # 會return一個名字為t1的class
t2 = TypeVar('t2')


def TypeVar1(x: List[t1], y: t1, z: t2) -> t1:
    return "123"


TypeVar1(x=["123", "321"], y=123, z=123)  # list x 裡面裝的item與y要一樣

# ----- 定義自己的generic type -----
from typing import Generic


# A generic type is typically declared by inheriting from this class parameterized with one or more type variables.

# 傳入一個list做初始，t1 = > list內的object的type, t2 => index
# my_list只可以傳入一個內部的object型態皆相同的list
# 且在修改值時也只能給予相同形態的object
V = TypeVar('V')
# 不能單億限制 ex 只有 int
II = TypeVar('II', int, float)  # 限制類行為int與float

#class Pair(Generic[T, T]):   # INVALID


class MyList(Generic[V, II]):
    def __init__(self, init_list: List[V]):
        self.my_list = init_list
        pass

    def __len__(self) -> int:
        return len(self.my_list)

    def __getitem__(self, index: II) -> V:
        return self.my_list[index]

    def __setitem__(self, key: II, value: V) -> None:
        self.my_list[key] = value


def get_value(my_list: MyList[str, int], index: II) -> V:
    return my_list[index]


a = MyList([1, 2, 0.2])
b = MyList(["321", "123", 0.2])

print("\n generic type :")
v1 = get_value(a, 0)
print(v1)
v2 = get_value(b, 0)  # ????
print(v2)


class MyList1(Generic[V]):
    def __init__(self, init_list: List[V]):
        self.my_list = init_list
        pass

    def __len__(self) -> int:
        return len(self.my_list)

    def __getitem__(self, index: int) -> V:
        return self.my_list[index]

    def __setitem__(self, key: int, value: V) -> None:
        self.my_list[key] = value


def get_value1(my_list: MyList1[str], index: int) -> V:
    return my_list[index]


a = MyList1([1, 2, 0.2])
b = MyList1(["321", 1, "123"])

print("\n generic type :")
v1 = get_value1(a, 0)
print(v1)
v2 = get_value1(b, 0) # MyList1[Union[str, int]] == MyList[str, int]
print(v2)


# Union
# Union[X, Y] 意味着：要不是 X，要不是 Y
print(Union[str, int])

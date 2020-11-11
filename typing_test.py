# python 3.5 以上版本
# 方便檢查function input與output的type


print("基本的標註輸入與輸出的type :")
def typing_hello(name: str) -> None:
    print("Hello~{}".format(name))
typing_hello("Lisa")

print("\nType alases :")
from typing import List
name_list = List[str]
def typing_hello(names: name_list) -> name_list:
    return names*2
names = typing_hello(["Lisa","Meow"])
print(names)
names = typing_hello([1,2])  # 不會error 但是會有提醒
print(names)


print("\nNewType :")
from typing import NewType

UserId = NewType('UserId', int)
Meow = NewType('Meow', str)
some_id = UserId(524313)

# NewType -> 回傳一個 function name 為 name，父類別為tp的函式，該functionc會回傳輸入的值
# def NewType(name, tp):
#     def new_type(x):
#         return x
#
#     new_type.__name__ = name
#     new_type.__supertype__ = tp
#     return new_type

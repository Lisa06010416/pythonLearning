# https://medium.com/@chipiga86/circular-references-without-memory-leaks-and-destruction-of-objects-in-python-43da57915b8d
# https://rushter.com/blog/python-garbage-collector/

# 在做迴圈引用時，或是自己引用自己，會導致reference count 至少唯一
# 因此Object的生命週期不會結束，所以python用gc來回收
# gc會週期性的執行，有分3個generations，每一個新的object都屬於第一個generations，一個垃圾回收的回合結束後，沒有被刪掉後會到第二個generations
# 越前面的generation會越常呼叫collection
# 原理是越久沒有被刪除的，越不會是垃圾

import gc
import sys

class ObjectA():
    def __del__(self):
        print("ObjectA Delete ~~~")


# 正常的刪除，a會被刪掉
a = ObjectA()
print("The reference count of a : {}".format(sys.getrefcount(a)))
del a
print("")

# 自己引用自己，del時不會被刪掉
class SelefReferenceObjectA():
    def __init__(self):
        self.a = self

    def __del__(self):
        print("SelefReferenceObjectA Delete ~~~")


self_reference_a = SelefReferenceObjectA()
print("The reference count of self_reference_a : {}".format(sys.getrefcount(self_reference_a)))
del self_reference_a
print("")

# circular reference，也不會刪掉
class CircularObjectA():
    def add_object(self, o):
        self.o = o

    def __del__(self):
        print("CircularObjectA Delete ~~~")

class CircularObjectB():
    def add_object(self, o):
        self.o = o

    def __del__(self):
        print("CircularObjectB Delete ~~~")

circul_a = CircularObjectA()
circul_b = CircularObjectA()
circul_a.add_object(circul_b)
circul_b.add_object(circul_a)
print("The reference count of circul_a : {}".format(sys.getrefcount(circul_a)))
print("The reference count of circul_b : {}".format(sys.getrefcount(circul_b)))
del circul_a, circul_b
gc.collect()

print("~~~~~~~~~~~ End Test ~~~~~~~~~~~")
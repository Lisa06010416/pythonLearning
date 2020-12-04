# timeit.timeit(stmt, setup,timer, number)
# stmt: statement的n縮寫，要執行的程式碼，default  "pass"
# setup: 執行的環境
# number: stmt執行的次數，default 1000000
import timeit

# ------------------- 簡單的傳入代碼的字串 -------------------
print("-------- 簡單的傳入代碼的字串 ------")
t1 = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(t1)
t2 = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(t2)
t3 = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print(t3)


# ------------------- 傳入一個functino的字串 -------------------
code = '''
def joinstr(list):
    s = ""
    for i in list:
        s += i+"_"
    return s
'''
print("-------- 傳入一個functino的字串 ------")
t1 = timeit.timeit(stmt='joinstr([str(n) for n in range(100)])',setup=code, number=10000)
print(t2)
t2 = timeit.timeit(stmt='joinstr((str(n) for n in range(100)))',setup=code, number=10000)
print(t2)


# ------------------- 直接傳function，必須回傳一個fumction -------------------
# _joinstr => 主要測試的function，且不可傳參數到_joinstr
def joinstr_1(list): # ok
    def _joinstr():
        # do something to num1 and num2
        s = ""
        for i in list:
            s += i+"_"
        return s
    return _joinstr

A = [str(i) for i in range(100)]
t = timeit.Timer(joinstr_1(A))  # timeit.Timert 創建一個 setup
print("-------- 直接傳function，必須回傳一個fumction ------")
print(t.timeit(10000))

def joinstr_2(list): # err
    def _joinstr(list): # 因為傳參數進list
        pass
    return _joinstr

def joinstr_3(list): # err # 需要回傳函數
    s = ""
    for i in list:
        s += i+"_"
    return s

# ------------------- 直接傳function，簡化的傳法 -------------------
print("-------- 直接傳function，簡化的傳法 ------")
# timeit.timeit(functools.partial(joinstr_3,A))


# ------------------- import 環境 from __main__ -------------------
def joinstr_test(A):
    joinstr_3(A)
    
print("-------- import 環境 from __main__ ------")
print(timeit.timeit("joinstr_test(A)", setup="from __main__ import joinstr_test,A", number=10000))

# ------------------- import 環境 globals -------------------
print("-------- import 環境 globals ------")
print(timeit.timeit("joinstr_test(A)", globals=globals(), number=10000))








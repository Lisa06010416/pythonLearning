import timeit

# 會將 PerformanceTest.timeit_test.timeit_test 的程式都執行一次
t = timeit.Timer(stmt="a.foo(a.A, a.B)", setup="import PerformanceTest.timeit_test.timeit_test as a")
print("-------- import 環境 --------")
print(t.timeit(10000))
print("~~~")
## Pergormance Test

#### Timeit
* 少量程式碼的效能測試
* timeit_test.py    

* profile : 用python實現的效率評估
* cProfile : 用C實現的
profile與cProfile的interface一樣

* line_profiler : 每行程式碼的執行時間與次數
    
* memory_profiler : 每行程式使用的

* PyCharm圖形化效能測試工具

* objgraph : 找到Python中，object reference的關係(解決memory leak)
    * 在Python每個東西都是Object，由Reference來控制Object的life cycle，像是做assignc或是呼叫function都會讓Reference count + 1
    * 通常memory leak會發生在
        * Circular Reference
        * Reference到global變數上
# yield

* yield的目的是節省記憶體，可以先輸出當下需要的內容
    ```
    # 模仿python3的range函式
    def my_range(x):
        x = 0
        while True:
            yield x
            x += 1
            if x == n:
                break
    for i in my_range(10):
        print(i) # ---> 0123456789
    ```

* 函式如果有yield則會被視為一個Generator，可以使用下咧方法拿到值：

    * next() : Generator為一個具有Iterator介面的物件，具有 __next__()
    * send() : 可以傳直到grnerate中
  ```
    def get_val(val):
        while True:
            res = yield val
            print("res:",res)
    g = get_val(10)
    g.next()  ----> print : res: None
    g.send(100)   ----> print : res: 100
  ```
  
* () + for 會是一個generator
# Queue

## Deque
* 由 collections 提供，雙向的queue
* 操作跟list較像，可以以用build-in function ex, len()
* 有的function :

|  功能 | 說明  |
|  ----  | ----  |
|  pop()  | 移去並且返回最右邊的一個元素  |
|  popleft()  | 移去並且返回最左邊的一個元素  |
|  append(x)  | 添加 x 到右端  in-memory|
|  appendleft(x)  | 添加 x 到左端  in-memory|
|  extend(iterable)  | 添加 iterable 到右端  in-memory|
|  extendleft(iterable) | 添加 iterable 到左端  in-memory|
|  insert(i, x)  | 在位置 i 插入 x  in-memory|
|  clear()  | 移除所有元素  in-memory|
|  remove(x)  | 移除找到的第一個x。 如果沒有的話就引發 ValueError。 in-memory |
|  copy()  | 創建一份淺拷貝。 in-memory  |
|  count(x)  | 計算 deque 中元素等於 x 的個數  |
|  index(x[, start[, stop]])  | 返回 x 在 deque 中的位置。 返回第一個匹配項，如果未找到則引發 ValueError  |
|  reverse()  | 逆序排列。in-memory |
|  rotate(n=1)  | 向右循環移動 n 步。如果 n 是負數，就向左循環 。 in-memory。 原本的list沒有|
|  maxlen  | Deque的最大尺寸，如果沒有限定的話就是 None  |


## queue
* threading 使用？

* 有三種類別：

|  物件 | 說明  |
|  ----  | ----  |
|  queue.Queue  | FIFO 先進先出  |
|  queue.LifoQueue  | LIFO 先進後出。基本上是stack  |
|  queue.PriorityQueue  | 根據優先級 pop item  |
* 宣告方法
```
import queue
q = queue.Queue(maxsize=1) #指定佇列大小為1
q = queue.Queue() #不指定佇列大小
```
* 判斷是否為空
```
q = queue.Queue()
if q:
    print("QQQQ")
>>> QQQQ
```
* 序列化存取資料：
```
q.queue[0]
```
* function :

|  功能 | 說明  |
|  ----  | ----  |
|  get(item[, timeout]]) | 取出一個元素  |
|  put(item[, timeout]]) | 放入一個元素  |
|  queue.qsize() | 佇列的大小  |
|  full() | 佇列是否滿了  |
|  empty() | 佇列是否為空  |
|  get_nowait() |   |
|  put_nowait(item) |   |
|  join() | 阻塞  |
|  task_done() |   |

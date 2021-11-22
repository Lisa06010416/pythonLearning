
# Collection
在內建資料型別（dict、list、set、tuple）的基礎上，collections模組提供了幾個額外的資料型別
* namedtuple ：生成可以使用名字來訪問元素內容的tuple，通常用來增強程式碼的可讀性， 在訪問一些tuple型別的資料時尤其好用.
* deque      ：雙端佇列，可以快速的從另外一側追加和推出物件.
* Counter    ：計數器，主要用來計數.
* OrderedDict：有序字典.
* defaultdict：帶有預設值的字典.

## nametuple
```
from collections import namedtuple
>>> Ponint = namedtuple('Ponint', ['x', 'y'])
>>> p = Ponint(1, 2)
>>> p.x # 1
>>> p.y # 2
```

## deque
double-ended queue，用linking list實作(修改資料時比list快，訪問特定index資料比list慢)

與list很相似，多了popleft()、extendleft()、appendleft()

deque是线程安全的
```
>>> from collections import deque
>>> dq = deque([1, 2, 3])
>>> dq.append('z')
>>> dq.appendleft('a')  # 從頭部新增元素
>>> dq.pop() # 'z'
>>> dq.popleft()  # 從頭部彈出元素 # 'a'
```

## Counter
計算值出現的次數.
```
from collections import Counter

s = '''
    A Counter is a dict subclass for counting hashable objects. 
    It is an unordered collection where elements are stored as dictionary keys and 
    their counts are stored as dictionary values. 
    Counts are allowed to be any integer value including zero or negative counts. 
    The Counter class is similar to bags or multisets in other languages.
'''.lower()

c = Counter(s)
# 獲取出現頻率最高的4個字元
print(c.most_common(4))  # [(' ', 74), ('e', 32), ('s', 25), ('a', 24)]
```

## OrderedDict
在Python中，dict這個資料結構由於hash的特性，是無序的，但Python3.6版本以後的字典是有序的了.
。OrderedDict的key是按照插入的順序排列的，而不是Key本身排序。
```
>>> from collections import OrderedDict
>>> od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
>>> od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
```

## defaultdict
在使用Python原生的資料結構dict的時候，如果用d[key]這樣的方式訪問，當指定的key不存在時，是會丟擲KeyError異常的

但是，如果使用defaultdict，只要你傳入一個預設的工廠方法，那麼請求一個不存在的key時， 便會呼叫這個工廠方法使用其結果來作為這個key的預設值.

```
>>> from collections import defaultdict
>>> dd = defaultdict(lambda: 'N/A')
>>> dd['name'] = "花千骨"
>>> dd['name']
'花千骨'
>>> dd['sex']   #'sex'不存在，將返回預設值
'N/A'
```
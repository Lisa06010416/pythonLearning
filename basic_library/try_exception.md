# try ... exception ... finally ...

* 列出錯誤的訊息
```
try:
    a = 2/0
except Exception as e:
    error_class = e.__class__ #取得錯誤類型
    error_class = e.__class__.__name__ #取得錯誤類型名稱
    detail = e.args[0] #取得詳細內容
    cl, exc, tb = sys.exc_info() #取得Call Stack
    lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
    fileName = lastCallStack[0] #取得發生的檔案名稱
    lineNum = lastCallStack[1] #取得發生的行號
    funcName = lastCallStack[2] #取得發生的函數名稱
    errMsg = "File \"{}\", line {}, in {}: [{}] {}".format(fileName, lineNum, funcName, error_class, detail)
    print(errMsg)
```

* 捕捉特定錯誤
```
try:
    your code ...
except ZeroDivisionError: # e.__class__
    print("exception1")
exception (ValueError, xxxError):
    print("exception2")
```

* finally 不論是否有觸發 exception 都會執行 finally
```
try:
    file = open("xxx.text")
except ValueError:
    print(e.__class__)
    file.close()
finally:
    file.close()
```

# aline
def align(_string:str, _length:int, _type: str ='L'):
    """
    _type =>
    L => 至左對齊
    R => 至右對齊
    C => 至中對齊
    """
    _str_len = len(_string)  # 計算字串長度
    for _char in _string:  # 判斷中文字數量
        if u'\u4e00' <= _char <= u'\u9fa5':  # 判斷是否為中文字
            _str_len += 1
    _space = _length-_str_len  # 計算需要填的空格數量
    if _type == 'L':  # 往右填空格
        _left = 0
        _right = _space
    elif _type == 'R': # 往左填空格
        _left = _space
        _right = 0
    else:              # 左右評分空格數
        _left = _space//2
        _right = _space-_left
    return ' '*_left + _string + ' '*_right


# print with color
# https://medium.com/jeasee%E9%9A%A8%E7%AD%86/%E8%AE%93python%E8%AE%8A%E5%BE%97%E7%BE%8E%E7%BE%8E%E7%9A%84-%E5%BD%A9%E8%89%B2%E7%9A%84%E5%AD%97-d9195f7ff6a8


text = "Hi~"

# \033 1=>粗體 ; 32=>前景色-綠色 ; 40=>被景色-黑色 m{文字} \033[ 47=>文字以外地方的背景色 m
color_temp_1 = "\033[1;32;40m{}\033[47m"
# \033 4=>底線 ; 31=>前景色-紅色 ; 46m=>被景色-青藍色 m{文字} \033[ 0=>文字以外地方的無色 m
color_temp_2 = "\033[4;31;46m{}\033[0m"
print(color_temp_1.format(text))
print(color_temp_2.format(text))

# ------------------ 顏色 ---------------------
# 字體色     |     字背景色     |   顏色描述
# ------------------------------------------
# 30        |        40       |    黑色
# 31        |        41       |    紅色
# 32        |        42       |    綠色
# 33        |        43       |    黃色
# 34        |        44       |    藍色
# 35        |        45       |    紫紅色
# 36        |        46       |    青藍色
# 37        |        47       |    白色
# -------------------------------------------

# -------------- 效果 ------------
# 顯示方式     |      效果
# -------------------------------
# 0           |     終端默認設置
# 1           |     高亮顯示
# 4           |     使用下劃線
# 7           |     反白顯示
# -------------------------------

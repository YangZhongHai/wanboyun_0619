import time
# 生成当前时间
def nowTime():
    # """格式化成2016-03-20 11:45:39形式"""
    tim = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return tim
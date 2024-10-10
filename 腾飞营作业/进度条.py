import time


def progress_bar (second,callback_fuction):
    """
    这是一个进度条函数，参数是进度条每前进一格需要的秒数，回调函数
    """
    for i in range(0,101):
        print("▨" * i + "□" * (100 - i), end = "\r")
        time.sleep(second)
        if i == 100:
            callback_fuction()



def callback_fuction ():
    """
    这是一个回调函数，当进度条走完时，会调用这个函数
    """
    print("抖音！！！！") 


progress_bar(0.1,callback_fuction)



   
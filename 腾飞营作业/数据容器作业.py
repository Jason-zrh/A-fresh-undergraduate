import time

def progress_bar(second):
    for i in range(0,101):
        print("■" * i +"□" * (100-i) + f" {i}%", end="\r")
        time.sleep(second)

# progress_bar(0.1)


my_list = [ "这是一个字符串", 6732123, ["计算机", "机器人", "自动化"],
           
           "", 12.9682, 6+9j, ["清华大学", "浙江大学"], "Apple", 
           progress_bar, print("我是个print函数, 被执行了！") ]

# while my_list:
#     my_list.pop()

# print(my_list)

new_list = []

for item in range(len(my_list)-1, -1, -1):
    if type(my_list[item]) == list:
        for sub_item in range(len(my_list[item])-1, -1, -1):
            new_list.append(my_list[item][sub_item])
    else:   
        new_list.append(my_list[item])


print(new_list)






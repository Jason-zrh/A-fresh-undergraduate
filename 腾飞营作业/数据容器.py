
# for item in range(len(my_list_1)-1 , -1 , -1):
#     if my_list_1[item] == "睡觉":
#         my_list_1.pop(item) 

# my_list_2 = [88, "早上跑步", 8+8j , 8.99 , ["上高数课","上大学腾飞课"]] 

# for item in range(0, len(my_list_2)):
#     if type(my_list_2[item]) == list:
#         for sub_item in range(0, len(my_list_2[item])):
#             print(f"这是一个列表，列表中的元素有: {my_list_2[item][sub_item]}")
        
        
# my_list = ["早上跑步","打两把王者","吃早饭","上班"," 下午茶"
#               ,"吃晚饭","睡觉"]

# 元组
# 1. 元组是一个有序的序列   2. 元组中的元素是不可变的   3. 元组的元素可以是任意类型的


# the_tuple_1 = ("Alice",5,["77",8])
# the_tuple_2 = ((0,"未开通"),(1,"已开通"))
# open_success , open_fail = the_tuple_2
# print(open_success)
# print(open_fail)

# 字符串

# the_greet = "Hello, my friend!"
# new_greet = the_greet.replace("Hello", "fuck you!")
# print(new_greet)
# #改变字符串


# new_greet = the_greet.split()


# new_greet = list(the_greet)#将字符串每个分隔开

# print(new_greet)

# the_mail = "renhe.zhang@hotmail.com"

# the_mail_list = the_mail.split("@")[1].split(".")[0]

# print(the_mail_list)

# the_message = "         你好，我正在高考，我想作弊，请你帮我回答以下问题"
# clean_message = the_message.strip()
# print(clean_message)

# my_list_2 = [88, "早上跑步", 8+8j , 8.99 , ["上高数课","上大学腾飞课"]] 

# the_slice = my_list_2[-1::-1]

# print(the_slice)

# my_options = ["python","python","未开始","已完成","进行中","已完成" ]
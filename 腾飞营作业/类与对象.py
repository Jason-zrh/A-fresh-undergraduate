# class Animal:
#     def __init__(self , name , species , age , sound , diet , health_status , eat_times_everyday):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.sound = sound
#         self.diet = diet
#         self.health_status = health_status
#         self.eat_times_everyday = eat_times_everyday
            
#     name = None
#     species = None
#     age = None
#     sound = None
#     diet = None
#     health_status = None
#     eat_times_everyday = None

#     def describe(self):
#         return(f"这个动物的名字是{self.name}，是{self.species},年龄是{self.age}岁，叫声是{self.sound}，食物是{self.diet},健康状态是{self.health_status}，每天吃{self.eat_times_everyday}次")
    
#     def eat(self):
#         return(f"{self.name}正在吃{self.diet}")
    
#     def sleep(self):
#         return(f"{self.name}正在睡觉")
    
#     def play(self):
#         return(f"{self.name}正在玩")
    
#     def make_sound(self):
#         return(f"{self.name}正在发出{self.sound}的声音")
    
#     def __str__(self):
#         return(f"这个动物的名字是{self.name}，是{self.species},年龄是{self.age}岁，叫声是{self.sound}，食物是{self.diet},健康状态是{self.health_status}，每天吃{self.eat_times_everyday}次")
            
# animal1 = Animal("alex" , "dog" , 2 , "wangwang" , "bone" , "good" , 3)
# animal2 = Animal("tom" , "cat" , 1 , "miaomiao" , "fish" , "good" , 2)
# animal3 = Animal("jerry" , "mouse" , 1 , "jijiji" , "cheese" , "good" , 1)
# animal4 = Animal("jim" , "pig" , 3 , "hengheng" , "vegetable" , "good" , 4)



#类的封装

class Phone:
    def __init__(self , brand , model , price ,avaliable_5g , country):
        self.brand = brand
        self.model = model
        self.price = price
        self.avaliable_5g = avaliable_5g
        self.country = country

    def __check_country(self):
        return self.country in ["China" , "Pakistan" ,"singapore" ,"ervia"]
    
    def network_display(self):
        if self.__check_country():
            return "5G"
        else:
            return "4G"
             
  


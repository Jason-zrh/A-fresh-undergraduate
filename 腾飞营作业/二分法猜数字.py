low_number = 0
high_number = 10000
import random



def guess_number (low_number, high_number):
    """
这是一个二分法猜数字的函数,函数的参数是数字范围0到10000,函数的返回值是猜对的次数，并使用解包的方式接受函数的返回值
"""

    randon_number = random.randint(low_number, high_number)
    answer = random.randint(low_number, high_number)
    guess_count = 0
    while answer != randon_number:
        guess_count += 1
        if answer < randon_number:
            low_number = answer
            answer = (low_number + high_number) / 2
        elif answer > randon_number:
            high_number = answer
            answer = (low_number + high_number) / 2
    return answer , guess_count


a , b = guess_number(low_number, high_number)
print(f"恭喜你猜对了，数字是{a}")
print(f"你猜了{b}次。")
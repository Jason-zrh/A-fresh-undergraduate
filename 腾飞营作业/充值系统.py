my_money = input("Enter your money:")
my_money = float(my_money)
give_money = 0

if 1000 <= my_money < 5000:
    give_money = my_money * 0.15
elif 5000 <= my_money <= 10000:
    give_money = my_money * 0.20
    give_money += 500
elif 10000 <= my_money:
    give_money = 10000

my_money += give_money
print(my_money)
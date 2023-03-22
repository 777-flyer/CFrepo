each_banana, wallet, number_of_bananas = input().split(" ")

wallet = int(wallet)
each_banana = int(each_banana)
number_of_bananas = int(number_of_bananas)

total_money = 0
money_needed = 0

for i in range(1,number_of_bananas+1):
    
    total_money += i * each_banana
    
if total_money > wallet:
    money_needed = total_money - wallet
    print(money_needed)
else:
    print(0)
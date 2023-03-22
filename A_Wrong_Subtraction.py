number, times = input().split(" ")

number = int(number)
times = int(times)

for i in range(times):
    
    if number % 10 == 0:
        
        number = number // 10
        
    else:
        
        number -= 1
        
print(number)
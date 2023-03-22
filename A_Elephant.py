# distance = int(input())

# steps = [1, 2, 3, 4, 5]
# counter = 0

# if distance in steps:
    
#     print(1)

# else:
    
#     while distance > 0:
        
#         distance -= 5
#         counter += 1
        
#     print(counter)

x = int(input())

steps = x // 5  
if x % 5 != 0:
    steps += 1 
    
print(steps)

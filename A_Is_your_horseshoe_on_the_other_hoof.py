shoes = input().split()
unique_list = []

for i in shoes:
    
    i = int(i)
    
    if i not in unique_list:
        
        unique_list.append(i)
        
shoes_needed = len(shoes) - len(unique_list)

print(shoes_needed)
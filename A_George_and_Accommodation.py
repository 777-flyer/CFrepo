n = int(input())
counter = 0

for i in range(n):
    
    room = input().split()
    
    if int(room[1]) - int(room[0]) >= 2:
        
        counter += 1
        
    else:
        
        pass
    
print(counter)
n = int(input())
counter = 0

for i in range(n):
    
    x, y, z = input().split()
    
    x = int(x)
    y = int(y)
    z = int(z)
    
    if (x + y + z) >= 2:
        counter += 1
        
print(counter)
x = int(input())
bacteria = 1
counter = 0

while x > 0:
    
    if x % 2 == 1:
        
        counter += 1
        
    x //= 2

print(counter)


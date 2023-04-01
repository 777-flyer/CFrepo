n, h = input().split()

n = int(n)
h = int(h)

heights = input().split()
width = 0

for height in heights:
    
    height = int(height)
    
    if height <= h:
        
        width += 1
        
    elif height > h:
        
        width += 2
        
print(width)
x, y = map(int, input().split())

if y <= (x + 1) // 2:
    
    print((y - 1)*2 + 1)
    
else:
   
    print((y - (x + 1) // 2) * 2)


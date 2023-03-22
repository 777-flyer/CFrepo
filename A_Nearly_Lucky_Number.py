number = input()

counter = 0

for i in number:
    
    if i == '4' or i == '7':
        
        counter += 1
    
if counter == 7 or counter == 4:
    
    print('YES')
    
else:
    
    print('NO')
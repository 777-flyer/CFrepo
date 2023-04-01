string = input()
 
instructions = ['H', "Q", '9']
flag = False
 
for i in string:
    
    if i in instructions:
        
        flag = True
        
        break
 
if flag:
    print("YES") 
else:
    print("NO")
string = input()

hello = "hello"
j = 0
length = len(string)

for i in range(length):
    
    if string[i] == hello[j]:
        
        j += 1
        
    if j == 5:
        
        break

if j == 5:
    
    print("YES")
    
else:
    
    print("NO")

# characters = int(input())
# string = input().lower()
 
# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# registered = []

# for i in range(characters):
    
#     if string[i] in alphabets and string[i] not in registered:
        
#         registered.append(string[i])
        
#         if len(registered) == 26:
#             break
        
# if len(registered) == 26:
#     print('YES')
# else:
#     print('NO')

n = int(input())
s = input().lower()

alphabets = 'abcdefghijklmnopqrstuvwxyz'

for char in alphabets:
    if char not in s:
        print("NO")
        break
else:
    print("YES")

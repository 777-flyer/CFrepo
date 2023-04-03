n = int(input())

y_list = ['y', 'Y']
e_list = ['e', 'E']
s_list = ['s', 'S']

for _ in range(n):
    
    string = input()
    
    if string[0] in y_list and string[1] in e_list and string[2] in s_list:
        
        print('YES')
        
    else:
        
        print('NO')
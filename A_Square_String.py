n = int(input())

for i in range(n):
    
    string = input()
    length = len(string)
    
    if length % 2 == 0:
        
        first_string = string[0 : length // 2]
        second_string = string[length // 2 :]
        
        if first_string == second_string:
            
            print('YES')
            
        else:
            
            print('NO')
            
    else:
        
        print('NO')
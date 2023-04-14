t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    l_count = 0
    r_count = 0
    moves = 0
    
    for i in range(n):
        if s[i] == '(':
            l_count += 1
        else:
            r_count += 1
        
        # if there are more right brackets than left brackets,
        # move a right bracket to the beginning of the string
        if r_count > l_count:
            moves += 1
            r_count -= 1
        
        # if the string is unbalanced, move a left bracket to the end of the string
        elif l_count > (n//2):
            moves += 1
            l_count -= 1
            
    print(moves)

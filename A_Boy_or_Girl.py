string = input()
distinct_char = []

for i in string:
    
    if i not in distinct_char:
        distinct_char.append(i)
        
if len(distinct_char) % 2 == 0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')
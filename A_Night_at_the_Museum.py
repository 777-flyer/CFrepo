string = input().strip()
'''
zeus, ares, map
'''
steps = 0
current = 'a'

for character in string:
    
    difference = abs(ord(current) - ord(character))
    from_left = 26 - difference #total chars - diff
    
    if difference > from_left:
        steps += from_left
    else:
        steps += difference
        
    current = character

print(steps)

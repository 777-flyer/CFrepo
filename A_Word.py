string = input()

cap_a = ord("A")
cap_z = ord("Z")
small_a = ord('a')
small_z = ord('z')

cap_ctr = 0
small_ctr = 0

for i in string:
    
    if ord(i) in range(cap_a, cap_z + 1):
        cap_ctr += 1
    elif ord(i) in range(small_a, small_z + 1):
        small_ctr += 1
        
if cap_ctr > small_ctr:
    string = string.upper()
    
elif cap_ctr == small_ctr:
    string = string.lower()
    
elif cap_ctr < small_ctr:
    string = string.lower()
    
print(string)
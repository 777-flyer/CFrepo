string_1 = input().lower()
string_2 = input().lower()

length_of_strings = len(string_1)

for i in range(length_of_strings):
    
    if ord(string_1[i]) < ord(string_2[i]):
        
        print("-1")
        break
    
    elif ord(string_1[i]) > ord(string_2[i]):
        
        print("1")
        break

else:
    print("0")
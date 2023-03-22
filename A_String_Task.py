string = input().lower()
new_string = ''

vowels = ["a", "o", "y", "e", "u", "i"]

for i in string:
    
    if i in vowels:
        pass
    else:
        new_string += "." + i
        
print(new_string)
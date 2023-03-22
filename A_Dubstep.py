string = input().split("WUB")
song_name = ''

for i in string:
    
    if len(i) >= 1:
        
        song_name += i + " "
        
print(song_name)
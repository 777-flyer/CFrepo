number_of_words = int(input())
list_containing_words = []

for i in range(number_of_words):
    
    words = input()
    list_containing_words.append(words)
    
new_words = []
codded_word = ""
counter = 0
new_word = ''

for j in list_containing_words:
    
    if len(j) <= 10:
        
        new_words.append(j)
        
    elif len(j) > 10:
        
        codded_word = j[1:len(j) -1]
        counter = len(codded_word)
        new_word = j[0] + str(counter) + j[len(j) - 1]
        new_words.append(new_word)
        
for k in new_words:
    print(k)
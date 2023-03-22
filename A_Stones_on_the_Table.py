stones = int(input())
colors = input()
counter = 0

for i in range(1, stones):
    
    if colors[i] == colors[i - 1]:
        counter += 1
        
print(counter)
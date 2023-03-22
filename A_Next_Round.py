n, k = input().split(" ")

n = int(n)
k = int(k)

scores = input()
counter = 0

individual_scores = list(scores.split(" "))
    
for j in individual_scores:
    
    int_score = int(j)
    
    if int_score >= int(individual_scores[k-1]) and int_score > 0:
        counter += 1
            
print(counter)
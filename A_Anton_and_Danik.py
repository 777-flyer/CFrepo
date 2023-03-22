games = int(input())
results = input()

a_count = 0
d_count = 0

for i in results:
    
    if i == 'A':
        a_count += 1
    elif i == 'D':
        d_count += 1
        
if a_count > d_count:
    print('Anton')
elif d_count > a_count:
    print('Danik')
elif a_count == d_count:
    print('Friendship')
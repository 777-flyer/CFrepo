# numbers = input().split("+")
# numbers.sort()
# print('+'.join(numbers))

#another way to solve this problem

s = input().split('+') 
count = [0, 0, 0] 

for i in s:
    if i == '1':
        count[0] += 1
    elif i == '2':
        count[1] += 1
    else:
        count[2] += 1

sorted_s = '1+' * count[0] + '2+' * count[1] + '3+' * count[2]
sorted_s = sorted_s[:-1] 

print(sorted_s)
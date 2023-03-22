year = int(input())

new_year = ''

for i in range(year + 1, 10000):
    
    year = str(i)
    
    x = year[0]
    y = year[1]
    z = year[2]
    f = year[3]
    
    current_year = []
    
    current_year.append(x)
    current_year.append(y)
    current_year.append(z)
    current_year.append(f)
    
    checking_year = []
    
    for c in current_year:
        
        if c not in checking_year:
            
            checking_year.append(c)
            
    if len(checking_year) == 4:
        
        new_year = int(checking_year[0] + checking_year[1] + checking_year[2] + checking_year[3])
        print(new_year)
        break


# def distinct_digits_year(year):
#     year += 1
#     while len(set(str(year))) != len(str(year)):
#         year += 1
#     return year

# y = int(input())
# print(distinct_digits_year(y))

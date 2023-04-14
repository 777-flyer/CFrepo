test_cases = int(input())

for _ in range(test_cases):
    
    length, digit = map(int, input().split())
    number = input()
    inserted = False
    
    for i in range(length):
        
        if number[i] < str(digit):
            
            number = number[:i] + str(digit) + number[i:]
            inserted = True
            break
    
    if not inserted:
        number += str(digit)
    
    print(number)

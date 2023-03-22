string_1 = input()
string_2 = input()

reversed_string = string_1[::-1]

if string_2 == reversed_string:
    print('YES')

else:
    print('NO')
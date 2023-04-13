s1 = input().strip()
s2 = input().strip()
letters = input().strip()

if len(letters) != len(s1) + len(s2):
    print("NO")
    exit()

letters_list = list(letters)

for c in s1:
    if c in letters_list:
        letters_list.remove(c)
    else:
        print("NO")
        exit()

for c in s2:
    if c in letters_list:
        letters_list.remove(c)
    else:
        print("NO")
        exit()

print("YES")

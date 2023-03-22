s = input()

if s.isupper():
    print(s.lower())
elif len(s) > 1 and s[0].islower() and s[1:].isupper():
    print(s.capitalize())
elif len(s) == 1 and s[0].islower():
    print(s[0].upper())
else:
    print(s)

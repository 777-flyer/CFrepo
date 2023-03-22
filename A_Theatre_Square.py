n, m, a = input().split(" ")

n = int(n)
m = int(m)
a = int(a)

rows = n // a

if n % a != 0:
    rows += 1

cols = m // a

if m % a != 0:
    cols += 1

print(rows * cols)
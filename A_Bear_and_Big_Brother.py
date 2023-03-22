x, y = input().split()

x = int(x)
y = int(y)

counter = 0

while x <= y:
    x *= 3
    y *= 2
    counter += 1
    
print(counter)

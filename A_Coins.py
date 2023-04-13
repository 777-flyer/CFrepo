def if_possible(n, k):
    
    if n % 2 != 0 and k % 2 == 0:
        return "NO"
    else:
        return "YES"

t = int(input())

for i in range(t):
    
    n, k = map(int, input().split())
    print(if_possible(n, k))

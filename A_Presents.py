n = int(input())
gifts = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    
    giver = gifts[i] - 1
    receiver = i + 1
    result[giver] = receiver

print(*result)

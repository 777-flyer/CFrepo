n = int(input())
scores = {}
for i in range(n):
    team = input().strip()
    if team in scores:
        scores[team] += 1
    else:
        scores[team] = 1

winning_team = None
winning_score = -1

for team, score in scores.items():
    if score > winning_score:
        winning_team = team
        winning_score = score

print(winning_team)

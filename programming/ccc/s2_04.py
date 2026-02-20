#https://dmoj.ca/problem/ccc04s2
#CCC S2 2004

players, rounds = map(int, input().split())

playerList = [0]*players
worst_rank = [1] * players

for i in range(rounds):
    roundInput = list(map(int, input().split()))
    for j in range(players):
        playerList[j] += roundInput[j]
    for i in range(players):
        rank = 1
        for j in range(players):
            if playerList[j] > playerList[i]:
                rank += 1
        worst_rank[i] = max(worst_rank[i], rank)

max_score = max(playerList)

for i in range(players):
    if playerList[i] == max_score:
        print(f"Yodeller {i+1} is the TopYodeller: score {playerList[i]}, worst rank {worst_rank[i]}")

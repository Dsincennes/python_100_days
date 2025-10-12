import  random

max_gold = int(input("Type max amount you want to roll: "))

player_count = int(input("How many players want to gamble? "))
players = {}
for i in range(1, player_count + 1):
    rand_num = random.randint(1, max_gold)
    players[i] = rand_num
    print(f"Player {i} rolled between 1 - {max_gold} and got {rand_num}")

winner = max(players, key=players.get)
loser = min(players, key=players.get)
owing = players[winner] - players[loser]
winner_roll = players[winner]
print(f"Winner is {winner} with a roll of {winner_roll}.\n{loser} owes {winner} {owing} gold!")










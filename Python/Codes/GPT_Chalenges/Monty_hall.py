import random as rd

hits_not_change = 0
hits_change = 0

for _ in range(1000000):
    gamedf = ['evellyn', 'goat', 'goat']
    rd.shuffle(gamedf)
    if gamedf[1] == 'evellyn':
        gamedf.pop(2)
    elif gamedf[2] == 'evellyn':
        gamedf.pop(1)
    else:
        gamedf.pop(1)

    if gamedf[0] == 'evellyn':
        hits_not_change += 1
    elif gamedf[1] == 'evellyn':
        hits_change += 1

print(hits_change)

print(hits_not_change)
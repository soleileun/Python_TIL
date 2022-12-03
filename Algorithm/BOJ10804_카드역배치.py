import sys

cards = list(range(1,21))

for i in range(10):
   x, y = map(int, sys.stdin.readline().split())
   x = x-1
   temp = reversed(cards[x:y])
   
   for j in range(x,y):
        cards[j] = next(temp)

for card in cards:
    print(card,end=' ')
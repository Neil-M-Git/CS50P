# shuffling cards using the shuffle fn of random library

import random

cards = ["K", "Q", "J", "A"]
random.shuffle(cards)

for card in cards:
    print(card)
#random = .choice, .randint, . shuffle
#statistics = .mean, 

import random

coin = random.choice(["heads", "tails"])
print(coin)

#--------------------------------------------------------------------------------------------------   random.choice will 
#this works too, 

from random import choice

coin = choice(["heads", "tails"])
print(coin)

#--------------------------------------------------------------------------\ random.randint(a, b) does the same thing for integers
import random

number = random.randint(1, 10)
print(number)

#--------------------------------------------------------------------\  shuffles and prints it in random order, for card in cards makes it loop it prints it in newlines
import random

cards = ["Jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)


# finds the mean of numbers, can be used for grading 
import statistics

print(statistics.mean([100, 90]))







  
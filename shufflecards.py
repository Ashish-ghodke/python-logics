import random, itertools
deck = list(itertools.product(range(1,14),["spade","club","Hearts","Daimond"]))

 
random.shuffle(deck)
for i in range(5):
    print(deck[i][0],"of",deck[i][1])
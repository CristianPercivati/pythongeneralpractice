import itertools

ranks = list(range(2,11))+['J','K','Q','A']
ranks = [str(rank) for rank in ranks]

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

#Here we use product to get the cartesian product of both ranks and suits sets

deck = [card for card in itertools.product(ranks,suits)]

#And here we can use combinations, where the first argument is m (deck) and the second is n (5)
#combinations formula is: m!/(m-n)!*n!

hands = [hand for hand in itertools.combinations(deck, 5)]

print(f'The total number of possible combinations of a 5-cards poker hand is: {len(hands)}')

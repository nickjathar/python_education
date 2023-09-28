import random

# deck is the dictionary of a complete 52-card deck with no cards removed
deck = {(1, 1): '2c', (1, 2): '2d', (1, 3): '2h', (1, 4): '2s',
        (2, 1): '3c', (2, 2): '3d', (2, 3): '3h', (2, 4): '3s',
        (3, 1): '4c', (3, 2): '4d', (3, 3): '4h', (3, 4): '4s',
        (4, 1): '5c', (4, 2): '5d', (4, 3): '5h', (4, 4): '5s',
        (5, 1): '6c', (5, 2): '6d', (5, 3): '6h', (5, 4): '6s',
        (6, 1): '7c', (6, 2): '7d', (6, 3): '7h', (6, 4): '7s',
        (7, 1): '8c', (7, 2): '8d', (7, 3): '8h', (7, 4): '8s',
        (8, 1): '9c', (8, 2): '9d', (8, 3): '9h', (8, 4): '9s',
        (9, 1): 'Tc', (9, 2): 'Td', (9, 3): 'Th', (9, 4): 'Ts',
        (10, 1): 'Jc', (10, 2): 'Jd', (10, 3): 'Jh', (10, 4): 'Js',
        (11, 1): 'Qc', (11, 2): 'Qd', (11, 3): 'Qh', (11, 4): 'Qs',
        (12, 1): 'Kc', (12, 2): 'Kd', (12, 3): 'Kh', (12, 4): 'Ks',
        (13, 1): 'Ac', (13, 2): 'Ad', (13, 3): 'Ah', (13, 4): 'As'}

# if you specify a card in human readable card form (e.g. As, Kd, 2c, etc.),
# find_deck_key returns the dictionary key that is the tuple associated with that human readable card
def find_deck_key(deck, card):
    return list(deck.keys())[list(deck.values()).index(card)]
        
# deck_50 is a special deck that that has the hero's hole cards removed so that you can observe
# the distribution of outcomes after the flop in isolation (that is without anyone else having been dealt hole cards)
deck_50 = deck.copy()


deck_48 = deck.copy()



hero_card_keys = []
villan_card_keys = []

sf = 0
foak = 0
fh = 0
f = 0
s = 0
toak = 0
tp = 0
op = 0
hc = 0

hero_cards = ['Ac', 'Tc']
villan_cards = ['Ah', 'Qd']

for card in hero_cards:
    hero_card_keys.append(find_deck_key(deck, card))

for card in villan_cards:
    villan_card_keys.append(find_deck_key(deck, card))

for card in hero_cards:
    if card in villan_cards:
        print('Hero and Villian cards are not legitimate!')
        break


for card in hero_card_keys:
    del deck_50[card]
    del deck_48[card]

for card in villan_card_keys:
    del deck_48[card]

flops_50 = []

#while len(flops_50) < 19600:
while len(flops_50) < 100:
    this_flop = []
    this_flop.extend(hero_card_keys)
    deck_draw = deck_50.copy()
    while len(this_flop) < 5:
        card_in_deck50 = 1
        while card_in_deck50:
            card = (random.randint(1, 13), random.randint(1, 4))
            if card in deck_draw.keys():
                this_flop.append(card)
                del deck_draw[card]
                card_in_deck50 = 0

    this_flop = sorted(this_flop, reverse=True)

    if this_flop not in flops_50:
        flops_50.append(this_flop)

hands_50 = []

for hand in flops_50:
    # calculate rank and suit density of the hero hand
    hand_rank = []
    hand_suit = []
    
    for card in hand:
        hand_rank.append(card[0])
        hand_suit.append(card[1])

    hand_rank = sorted(hand_rank, reverse=True)
    hand_suit = sorted(hand_suit, reverse=True)

    if (hand_suit[0] == hand_suit[4]) and ((hand_rank[0] - hand_rank[4]) == 4):
        hand.append('Straight Flush')
        sf += 1
    elif (hand_rank[0] == hand_rank[3]) or (hand_rank[1] == hand_rank[4]):
        hand.append('Four of a Kind')
        foak += 1
    elif (hand_rank[0] == hand_rank[2]) and (hand_rank[3] == hand_rank[4]) or (hand_rank[0] == hand_rank[1]) and (hand_rank[2] == hand_rank[4]):
        hand.append('Full House')
        fh += 1
    elif (hand_suit[0] == hand_suit[4]):
        hand.append('Flush')
        f += 1
    elif (hand_rank[0] - hand_rank[4]) == 4:
        hand.append('Straight')
        s += 1
    elif (hand_rank[0] == hand_rank[2]) or (hand_rank[1] == hand_rank[3]) or (hand_rank[2] == hand_rank[4]):
        hand.append('Three of a Kind')
        toak += 1
    elif (hand_rank[0] == hand_rank[1]) and (hand_rank[2] == hand_rank[3]) or (hand_rank[1] == hand_rank[2]) and (hand_rank[3] == hand_rank[3]) or (hand_rank[0] == hand_rank[1]) and (hand_rank[3] == hand_rank[4]):
        hand.append('Two Pair')
        tp += 1
    elif (hand_rank[0] == hand_rank[1]) or (hand_rank[1] == hand_rank[2]) or (hand_rank[2] == hand_rank[3]) or (hand_rank[3] == hand_rank[4]):
        hand.append('One Pair')
        op += 1
    else:
        hand.append("High Card")
        hc += 1

    hands_50.append(hand)

print(' Total Hands:\t\t', sf + foak + fh + f + s + toak + tp + op + hc, '\n',
      'High Card:\t\t', hc, '\n',
      'One Pair:\t\t', op, '\n',
      'Two Pair:\t\t', tp, '\n',
      'Three of a Kind:\t', toak, '\n',
      'Straight:\t\t', s, '\n',
      'Flush:\t\t\t', f, '\n',
      'Full of House:\t\t', fh, '\n',
      'Four of a Kind:\t', foak, '\n',
      'Straight Flush:\t', sf, '\n')
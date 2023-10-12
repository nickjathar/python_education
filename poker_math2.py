import time
import random
import itertools
import numpy as np

# deck is the dictionary of a complete 52-card deck with no cards removed
deck = {(1, 1):  '2c', (1, 2):  '2d', (1, 3):  '2h', (1, 4):  '2s',
        (2, 1):  '3c', (2, 2):  '3d', (2, 3):  '3h', (2, 4):  '3s',
        (3, 1):  '4c', (3, 2):  '4d', (3, 3):  '4h', (3, 4):  '4s',
        (4, 1):  '5c', (4, 2):  '5d', (4, 3):  '5h', (4, 4):  '5s',
        (5, 1):  '6c', (5, 2):  '6d', (5, 3):  '6h', (5, 4):  '6s',
        (6, 1):  '7c', (6, 2):  '7d', (6, 3):  '7h', (6, 4):  '7s',
        (7, 1):  '8c', (7, 2):  '8d', (7, 3):  '8h', (7, 4):  '8s',
        (8, 1):  '9c', (8, 2):  '9d', (8, 3):  '9h', (8, 4):  '9s',
        (9, 1):  'Tc', (9, 2):  'Td', (9, 3):  'Th', (9, 4):  'Ts',
        (10, 1): 'Jc', (10, 2): 'Jd', (10, 3): 'Jh', (10, 4): 'Js',
        (11, 1): 'Qc', (11, 2): 'Qd', (11, 3): 'Qh', (11, 4): 'Qs',
        (12, 1): 'Kc', (12, 2): 'Kd', (12, 3): 'Kh', (12, 4): 'Ks',
        (13, 1): 'Ac', (13, 2): 'Ad', (13, 3): 'Ah', (13, 4): 'As'}

rh = {0: 0, 1: 0, 2: 0, 3: 0,  4:  0, 5:  0, 6:  0,
      7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0}

sh = {1: 0, 2: 0, 3: 0, 4: 0}

hand_rank = {1:  'Two',   2:  'Three', 3:  'Four', 4: 'Five', 5:  'Six',
             6:  'Seven', 7:  'Eight', 8:  'Nine', 9: 'Ten',  10: 'Jack',
             11: 'Queen', 12: 'King',  13: 'Ace'}

poker_hands = {'Straight Flush': 0, 'Four of a Kind': 0, 'Full House': 0,
               'Flush': 0, 'Straight': 0, 'Three of a Kind': 0,
               'Two Pair': 0, 'One Pair': 0, 'High Card': 0}

def is_wheel(hand):
    
    hand = sorted(hand, reverse=True)
    hand_ranks = []
    
    for card in hand:
        hand_ranks.append(card[0])

    if hand_ranks[0]==13 and hand_ranks[1]==4 and hand_ranks[2]==3 and hand_ranks[3]==2 and hand_ranks[4]==1:
        pop_card = hand.pop(0)
        hand.append((0, pop_card[1]))

    return hand

def what_is_hand(hand, rh, sh, hr):
    
    rhc = rh.copy()
    shc = sh.copy()

    hand = is_wheel(hand)

    urv = 0
    usv = 0
    maxrv = 0
    minrv = 13

    pair = 0
    trips = 0
    quads = 0

    # put rank density and suit density for the hand into rhc and shc respectively
    for rank, suit in hand:
        rhc[rank] = rhc[rank] + 1
        shc[suit] = shc[suit] + 1

    for rank, count in rhc.items():
        if count != 0:
            urv += 1
            if rank > maxrv:
                maxrv = rank

            if rank < minrv:
                minrv = rank

            if count == 2:
                pair += 1
            elif count == 3:
                trips += 1
    
    for suit, count in shc.items():
        if count != 0:
            usv += 1

    rangerv = maxrv - minrv

    if usv == 1:
        if rangerv == 4:
            return ('Straight Flush', hr[maxrv] + ' High')
        else:
            return ('Flush', hr[maxrv] + ' High')
        
    if (rangerv == 4) and (urv == 5):
        return ('Straight', hr[maxrv] + ' High')
    
    if urv == 2:
        if pair == 1:
            return ('Full House', '')
        else:
            return ('Four of a Kind', '')
        
    if urv == 3:
        if pair == 2:
            return ('Two Pair', '')
        else:
            return ('Three of a Kind', '')
    
    if urv == 4:
        return ('One Pair', '')
    else:
        return ('High Card', '')

for i in range(5000000):
    # draw two hole cards   
    hole1 = random.sample(list(deck.keys()), 2)

    deck_50 = deck.copy()

    for card in hole1:
        del deck_50[card]

    flop = random.sample(list(deck_50.keys()), 3)

    resolve_hand = what_is_hand(hole1 + flop, rh, sh, hand_rank)
    poker_hands[resolve_hand[0]] += 1
    
    if resolve_hand[0] == 'Straight' and resolve_hand[1] == 'Five High':
        print('Hole Cards:', hole1, 'with Flop', flop, 'is', resolve_hand)

#print(list((itertools.combinations(hole1+flop, 3))))
#print(len(list((itertools.combinations(hole1+flop, 3)))))
#print(poker_hands)

exit()

find_hand = ''
hand_iterations = 0

while find_hand != 'Straight Flush':
    # draw two hole cards   
    hole1 = random.sample(list(deck.keys()), 2)

    deck_50 = deck.copy()

    for card in hole1:
        del deck_50[card]

    flop = random.sample(list(deck_50.keys()), 3)

    find_hand = what_is_hand(hole1 + flop, rh, sh, hand_rank)
    hand_iterations += 1

print('Hole Cards:', hole1, 'with Flop', flop, 'is', what_is_hand(hole1 + flop, rh, sh, hand_rank))
print('It took', hand_iterations, 'to draw to this hand.')


# hole_cards = []
# completion_times = []

# for i in range(1000):
#     start = time.time()
#     hole_cards = []
#     draws = 0
#     while draws < 1327:
#         deal_hole_cards = random.sample(deck_keys, 2)
#         if deal_hole_cards not in hole_cards:
#             hole_cards.append(deal_hole_cards)
#             draws += 1
#     completion_times.append(time.time() - start)
# print(np.mean(completion_times))
# print(np.std(completion_times))

#rnum = random
#print(random.choices(range(3)))

# hero_cards    = ['Ac', 'Th']
# opp1_cards    = ['Ad', 'Qh']

# # QA check of hero and opp1 hole card consistency
# if len(list(filter(lambda i: i in list(deck.values()), hero_cards))) != 2:
#     print('One or both hero cards are not legitimate! Please choose appropriate hole cards for hero.')
#     exit()

# if len(list(filter(lambda i: i in list(deck.values()), opp1_cards))) != 2:
#     print('One or both opp1 cards are not legitimate! Please choose appropriate hole cards for opp1.')
#     exit()

# if len(list(filter(lambda i: i in opp1_cards, hero_cards))) != 0:
#     print('There is an overlap of cards between hero and opp1 hole cards. Please re-enter hole cards for both hero and opp1.')
#     exit()

# # create separte lists that are the tuples associated with the human readable cards from the user's hero and opp1 hole card inputs
# #hero_card_keys = list(lambda card: deck.keys()[list(deck.values()).index(card)])
# hero_card_keys = []
# opp1_card_keys = []

# for card in hero_cards:
#     hero_card_keys.append(list(deck.keys())[list(deck.values()).index(card)])

# for card in opp1_cards:
#     opp1_card_keys.append(list(deck.keys())[list(deck.values()).index(card)])

# # deck_50 is a special deck that that has the hero's hole cards removed so that you can observe
# # the distribution of outcomes after the flop in isolation (i.e. without anyone else having been dealt hole cards)
# deck_50 = deck.copy()

# for card in hero_card_keys:
#     del deck_50[card]

# hero_hands = []

# while len(hero_hands) < 100:
    


# exit()


# deck_48 = deck.copy()


# sf = 0
# foak = 0
# fh = 0
# f = 0
# s = 0
# toak = 0
# tp = 0
# op = 0
# hc = 0




# flops_50 = []

# #while len(flops_50) < 19600:
# while len(flops_50) < 100:
#     this_flop = []
#     this_flop.extend(hero_card_keys)
#     deck_draw = deck_50.copy()
#     while len(this_flop) < 5:
#         card_in_deck50 = 1
#         while card_in_deck50:
#             card = (random.randint(1, 13), random.randint(1, 4))
#             if card in deck_draw.keys():
#                 this_flop.append(card)
#                 del deck_draw[card]
#                 card_in_deck50 = 0

#     this_flop = sorted(this_flop, reverse=True)

#     if this_flop not in flops_50:
#         flops_50.append(this_flop)

# hands_50 = []

# for hand in flops_50:
#     # calculate rank and suit density of the hero hand
#     hand_rank = []
#     hand_suit = []
    
#     for card in hand:
#         hand_rank.append(card[0])
#         hand_suit.append(card[1])

#     hand_rank = sorted(hand_rank, reverse=True)
#     hand_suit = sorted(hand_suit, reverse=True)

#     if (hand_suit[0] == hand_suit[4]) and ((hand_rank[0] - hand_rank[4]) == 4):
#         hand.append('Straight Flush')
#         sf += 1
#     elif (hand_rank[0] == hand_rank[3]) or (hand_rank[1] == hand_rank[4]):
#         hand.append('Four of a Kind')
#         foak += 1
#     elif (hand_rank[0] == hand_rank[2]) and (hand_rank[3] == hand_rank[4]) or (hand_rank[0] == hand_rank[1]) and (hand_rank[2] == hand_rank[4]):
#         hand.append('Full House')
#         fh += 1
#     elif (hand_suit[0] == hand_suit[4]):
#         hand.append('Flush')
#         f += 1
#     elif (hand_rank[0] - hand_rank[4]) == 4:
#         hand.append('Straight')
#         s += 1
#     elif (hand_rank[0] == hand_rank[2]) or (hand_rank[1] == hand_rank[3]) or (hand_rank[2] == hand_rank[4]):
#         hand.append('Three of a Kind')
#         toak += 1
#     elif (hand_rank[0] == hand_rank[1]) and (hand_rank[2] == hand_rank[3]) or (hand_rank[1] == hand_rank[2]) and (hand_rank[3] == hand_rank[3]) or (hand_rank[0] == hand_rank[1]) and (hand_rank[3] == hand_rank[4]):
#         hand.append('Two Pair')
#         tp += 1
#     elif (hand_rank[0] == hand_rank[1]) or (hand_rank[1] == hand_rank[2]) or (hand_rank[2] == hand_rank[3]) or (hand_rank[3] == hand_rank[4]):
#         hand.append('One Pair')
#         op += 1
#     else:
#         hand.append("High Card")
#         hc += 1

#     hands_50.append(hand)

# print(' Total Hands:\t\t', sf + foak + fh + f + s + toak + tp + op + hc, '\n',
#       'High Card:\t\t', hc, '\n',
#       'One Pair:\t\t', op, '\n',
#       'Two Pair:\t\t', tp, '\n',
#       'Three of a Kind:\t', toak, '\n',
#       'Straight:\t\t', s, '\n',
#       'Flush:\t\t\t', f, '\n',
#       'Full of House:\t\t', fh, '\n',
#       'Four of a Kind:\t', foak, '\n',
#       'Straight Flush:\t', sf, '\n')
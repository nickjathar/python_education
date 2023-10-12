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

for i in range(1):
    # draw two hole cards for player 1
    hole1 = random.sample(list(deck.keys()), 2)

    # remove hole cards from full deck and draw three the remaining 50 cards
    deck_50 = deck.copy()

    for card in hole1:
        del deck_50[card]

    flop = random.sample(list(deck_50.keys()), 3)

    # assess what hand player 1 has after the flop
    p1_cards_postflop  = sorted(hole1 + flop, reverse=True)
    p1_hand_postflop = what_is_hand(p1_cards_postflop, rh, sh, hand_rank)

    if (p1_hand_postflop[0] == 'Straight Flush' or p1_hand_postflop[0] == 'Straight') and p1_hand_postflop[1] == 'Five High':
        p1_cards_postflop = sorted(p1_cards_postflop, reverse=True)
        pop_card = p1_cards_postflop.pop(0)
        p1_cards_postflop.append((0, pop_card[1]))

    if (p1_hand_postflop[0] == 'Straight Flush') and p1_hand_postflop[1] == 'Ace High': # or p1_hand_postflop[0] == 'Straight Flush') and p1_hand_postflop[1] == 'Five High':
        print('The', i+1, 'th hand dealt is', p1_cards_postflop, 'which is', p1_hand_postflop[0], p1_hand_postflop[1])

    # remove flop cards from 50 card deck and draw turn from remaining 47 cards
    deck_47 = deck_50.copy()

    for card in flop:
        del deck_47[card]

    turn = random.sample(list(deck_47.keys()), 1)
    p1_cards_on_turn = hole1 + flop + turn

    t = 1

    for hand in list(itertools.combinations(p1_cards_on_turn, 5)):
        hand = sorted(hand, reverse=True)
        hand_assessed = what_is_hand(hand, rh, sh, hand_rank)
        if (hand_assessed[0] == 'Straight Flush' or hand_assessed[0] == 'Straight') and hand_assessed[1] == 'Five High':
            hand = sorted(hand, reverse=True)
            pop_card = hand.pop(0)
            hand.append((0, pop_card[1]))
        print('The', t, 'th hand combination on the turn for player 1', hand, 'is', hand_assessed[0], hand_assessed[1])
        t += 1

    # remove turn card from 47 card deck and draw river from remaining 46 cards
    deck_46 = deck_47.copy()
    del deck_46[turn[0]]

    river = random.sample(list(deck_46.keys()), 1)
    p1_cards_on_river = hole1 + flop + turn + river

    r = 1
    print('\n')

    for hand in list(itertools.combinations(p1_cards_on_river, 5)):
        hand = sorted(hand, reverse=True)
        hand_assessed = what_is_hand(hand, rh, sh, hand_rank)
        if (hand_assessed[0] == 'Straight Flush' or hand_assessed[0] == 'Straight') and hand_assessed[1] == 'Five High':
            hand = sorted(hand, reverse=True)
            pop_card = hand.pop(0)
            hand.append((0, pop_card[1]))
        print('The', r, 'th hand combination on the river for player 1', hand, 'is', hand_assessed[0], hand_assessed[1])
        r += 1
#this is a test, let's see how things can go...

#euchure
import random
import collections

#make players a dictionary?

def makeEDeck():
    cards = []
    suits = ['diamond', 'spade', 'club', 'heart']
    cnum = [9, 10, 11, 12, 13, 1]

    for s, c in zip(suits, cnum):
        for c in cnum:
            cards.append((s,c))
    return cards

def shuffleCards(cards):
    return random.sample(cards, len(cards))
    print(cards)

deck = shuffleCards(makeEDeck())
#print(cards)
#print(shuffleCards(cards))

#values = str(range(1, 11)) + "Jack Queen King".split()
##values = "1 2 3 4 5 6 7 8 9 10 11 12 13".split()
##
##suits = "Diamonds Clubs Hearts Spades".split()
##suits = ['diamond', 'spade', 'club', 'heart']
##
##deck_of_cards = ["({0} ,{1})".format(v, s) for v in values for s in suits]
##
##print(deck_of_cards[1])

points = 0

##p1 = [deck[0:5], 0]
##p2 = [deck[5:10], 0]
##p3 = [deck[10:15], 0]
##p4 = [deck[15:20], 0]
##kiddy = deck[20:24]
##

''' slicing Guide:
players, hands/score, cards, suite/value
'''

#deal cards to each player/kiddy
def dealCards(deck):
    p1 = [deck[0:5], 0]
    p2 = [deck[5:10], 0]
    p3 = [deck[10:15], 0]
    p4 = [deck[15:20], 0]       
    kiddy = deck[20:24]

    return p1, p2, p3, p4, kiddy


p1, p2, p3, p4, kiddy = dealCards(shuffleCards(makeEDeck()))
players = [p1,p2,p3,p4]
##while t1Points < 10 or t2Points < 10:

for player in players:
    print(player)

dealer = player[0]
print("dealer: ", dealer)



def handValue(player, suite):
    vu = 0
    print('suite : ', suite)
    for crd in player[0]:
        print('crd: ', crd)
        if crd[0] == suite:
            vu += 1
    #need a better way to calculate hand worth
    return vu

#iterate through hand and see if have multiple cards of same suite
#this would be an intresting machLearn problem
def chooseSuite(player, suite):
    vu = 0
    vs = 0 #1
    vc = 0 #2
    vh = 0 #3
    vd = 0 #4
    print('suite : ', suite)
    for crd in player[0]:
        print('crd: ', crd)
        if 'spade' == crd[0]:
            vs += 1
        if 'club' == crd[0]:
            vc +=1
        if 'heart' == crd[0]:
            vh += 1
        if 'diamond' == crd[0]:
            vd += 1
    #they cant have 3 of the same in 2 suits...
    if vs > 2 and vs != suite:
        return 1
    elif vc > 2 and vc != suite:
        return 2
    elif vh > 2 and vh != suite:
        return 3
    elif vd > 2 and vd != suite:
        return 4
    else:
        return 0


suts = {1: 'spade', 2: 'club', 3: 'heart', 4: 'diamond'}

def decTrump1(players, kiddy):
    cardUp = kiddy[random.randint(0,3)]
    print("cardUp: ", cardUp)
    i = 0 
    for player in players: 
        #if the player simply has 2 or more of the same suite in hand
        thresh = 2
        if handValue(player, cardUp[0]) > thresh:
            
            return cardUp, i
            break
        else:
            i += 1
    #return "none"
    print("t2")
    decTrump2(players, cardUp)

def decTrump2(players, cardUp):
    i = 0
    for player in players:
        thresh = 3
        if chooseSuite(player, cardUp[0]) == 1:
            return 1, i
        elif chooseSuite(player, cardUp[0]) == 2:
            return 2, i
        elif chooseSuite(player, cardUp[0]) == 3:
            return 3, i
        elif chooseSuite(player, cardUp[0]) == 4:
            return 4, i
        else:
            i += 1
        
        

def updateOrder(players):
    p0 = players[0]
    players.remove(p0)
    players.append(p0)
    #print(players)

updateOrder(players)

def setUp(players, kiddy):
    cU, i = decTrump1(players, kiddy)
    updateOrder(players)
    print('i = ', i)
    print('cU =', cU)
    


def play(players, kiddy):
    cU, i = decTrump1(players, kiddy)

    try:
        decTrump1(players, kiddy)
        updateOrder(players)
        
    except decTrump(players, kiddy) == "none":
        print('well')
    else:
        decTrump2(players, kiddy)
        updateOrder(players)
        
    print('i = ', i)
    print('cU =', cU)

    

def sameCard(hand):
    slst = [] 
    for c in hand:
        slst.append(c[0])
    if 3 in collections.Counter(slst).values():
        return True
    return False


 def whichCard(hand):
    if hand[0][0] == hand[1][0] == hand[1][0]:
         return hand[0][0]
    elif 







    

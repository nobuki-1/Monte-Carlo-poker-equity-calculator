#POKER RULES:
#1. Royal flush; 8 (with an ace as its highest card)
#2. Straight flush; 8
#3. Four of a kind; 7 
#4. Full house; 6
#5. Flush; 5
#6. Straight; 4
#7. Three of a kind; 3
#8. Two pair; 2
#9. One pair; 1
#10. High card; 0

category_names = ["high card", "pair", "two pair", "three of a kind",
                  "straight", "flush", "full house", "four of a kind",
                  "straight flush"]


def tally_of_ranks(hand):
  rank_tally = [0]*13
  for card in hand:
    tally = card[0]
    rank_tally[tally] = rank_tally[tally] + 1
  return rank_tally

def tally_of_suits(hand):
  suit_tally = [0]*13
  for card in hand:
    tally = card[1]
    suit_tally[tally] = suit_tally[tally] + 1
  return suit_tally

#one pair, two pair, three of a kind, full house, four of a kind: all dealt with
#if 5 separate 1s, then could be royal flush, straight flush, straight, flush or high card

def grouped_by_rank(hand):
  rank_tally = tally_of_ranks(hand)
  groups = []
  for rank in range(0,13):
    count = rank_tally[rank]
    if count > 0: #then you would get useless info like i have 0 jacks for example
      groups.append((count, rank))
  groups.sort(reverse = True)
  return groups #output: [(3,12), (1,11), (1,2)] - 3 aces, 1 king, 1 2

def hand_based_on_rank(hand):
  groups = grouped_by_rank(hand)
  top = groups[0][0]       # the biggest count
  second = groups[1][0]    # the second biggest count

  if top == 4:
    return 7             # four of a kind
  if top == 3 and second >= 2:
    return 6             # full house
  if top == 3:
    return 3             # three of a kind
  if top == 2 and second == 2:
     return 2             # two pair
  if top == 2:
    return 1             # pair
  else:
    return 0               # high card

def flush_check(hand):
  suit_tally = tally_of_suits(hand)
  for suit in range(0,4):
    if suit_tally[suit] >= 5:
      suited_ranks = []
      for card in hand:
        if card[1] == suit:
          suited_ranks.append(card[0])
      suited_ranks.sort(reverse = True)
      return suited_ranks[:5]
  return [] #returns an empty list not 0 because the output of this function is a list not a number (like straight_check is)

def straight_check(hand):
  rank_tally = tally_of_ranks(hand)
  for start in range(8,-1,-1): #counts backwards from 8 to find the highest possible straight
    if (rank_tally[start] > 0 and rank_tally[start+1] > 0
      and rank_tally[start+2] > 0 and rank_tally[start+3] > 0
      and rank_tally[start+4] > 0):
        return start + 4 #returns the top rank of the straight
  if (rank_tally[12] > 0 and rank_tally[0] > 0 and rank_tally[1] > 0
      and rank_tally[2] > 0 and rank_tally[3] > 0):
        return 3 #this is the rank of the number 5
  return 0


def straight_flush_check(hand):
  rank_tally = tally_of_ranks(hand)
  suit_tally = tally_of_suits(hand)
  for suit in range(0,4):
    if suit_tally[suit] >= 5:
      suited_cards = []
      for card in hand:
        if card[1] == suit:
          suited_cards.append(card)
      top_card = straight_check(suited_cards)
      if top_card != 0:
        return top_card
  return 0

#no need for a royal flush check for the computer as its just the highest possible straight flush
# kicker - best card not included in the main result (e.g. if A,A,K,3,3,2,2 - then its a 2 pair but the grouped_by_rank will say the 2,2 is best but it should be the king)
# made_ranks - the cards included in the main result (e.g. the 2 pair in the result above)
def best_kicker(hand, made_ranks):
  rank_tally = tally_of_ranks(hand)
  for rank in range(12,-1,-1):
    if rank_tally[rank] > 0 and rank not in made_ranks:
      return rank

def tiebrakers(hand):
  groups = grouped_by_rank(hand)
  category = hand_based_on_rank(hand)
  ranks = []
  for count, rank in groups:
    ranks.append(rank)
  if category == 1:
    return ranks[:4] #if its a pair then you return the first 4 ranks (one of these is a pair)
  if category == 2:
    made_cards = [groups[0][1], groups[1][1]] #this labels the already confirmed cards as the the 2 sets of pairs
    return made_cards + [best_kicker(hand, made_cards)] #returns the 2 pairs and the highest remaining card
  if category == 3:
    return ranks[:3] #three of a kind, you return the trio and then the next 2 highest
  if category == 6:
    return ranks[:2] #full house, you return the trio then the pair
  if category == 7:
    made_cards = [groups[0][1]] #four of a kind, extracts the 4 cards
    return made_cards + [best_kicker(hand, made_cards)] #necessary as could have 4 of a kind then a pair of 2s and a king but grouped_by_rank would say 2 is better which is false
  return ranks[:5] #this is a high card



def evaluate(hand):

  straight_flush_top_score = straight_flush_check(hand)
  if straight_flush_top_score != 0:
    return(8, [straight_flush_top_score])

  scores = hand_based_on_rank(hand)
  if scores >= 6:
    return(scores, tiebrakers(hand))

  flush_ranks = flush_check(hand)
  if flush_ranks:
    return(5, flush_check(hand))

  straight_ranks = straight_check(hand)
  if straight_ranks != 0:
    return(4, [straight_ranks])

  return(scores, tiebrakers(hand))


        


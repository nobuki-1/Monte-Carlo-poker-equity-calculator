import random


#random.sample(list, k) -  k different random items from a list with no repeats
#random.seed(n) - fixes the starting point so repeatable results

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"] #all possible ranks 
suits = ["c", "h", "d", "s"] #possible suits: clubs, hearts, diamonds, spades

def text_to_card(text):
  return (ranks.index(text[0].upper()), suits.index(text[1].lower()))

def text_to_hand(text):
  text = text.replace(" ", "")
  hand = []
  for i in range(0, len(text), 2):
    piece = text[i:i+2]
    hand.append(text_to_card(piece))
  return hand

def card_to_text(card):
  return ranks[card[0]] + suits[card[1]]

def cards_to_text(cards):
  texts = []
  for card in cards:
    texts.append(card_to_text(card))
  return ", ".join(texts)

deck = [] #lists all 52 cards (as tuples)
for rank in range(0,13):
  for suit in range(0,4):
    deck.append((rank, suit))


def leftover_cards(text):
  remaining_deck = []
  known_cards = text_to_hand(text)
  for card in deck:
    if card not in known_cards:
      remaining_deck.append(card)
  return remaining_deck

  








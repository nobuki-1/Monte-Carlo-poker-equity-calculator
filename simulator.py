import random
import math
from evaluator import evaluate
from cards import text_to_hand, leftover_cards, cards_to_text

category_names = ["high card", "pair", "two pair", "three of a kind",
                  "straight", "flush", "full house", "four of a kind",
                  "straight flush"]

#THIS PAGE CAN TEST WHEN YOU KNOW OPPONENT'S HAND
print("When typing out hand, print in format Xy Xy (where X is the rank and y is the first letter of the suit)")
player_text = input("Type out your hand:")
opponent_text = ""
dealt_text = ""

player_cards = text_to_hand(player_text)
known_opponent_cards = text_to_hand(opponent_text)
unknown_opponent_cards = 2 - len(known_opponent_cards)
dealt = text_to_hand(dealt_text)

deck_left = leftover_cards(player_text + dealt_text + opponent_text)
missing = 5 - len(dealt) #these are the number of cards left to be dealt on the board

#EDIT TRIALS TO CHANGE NO. OF TRIALS.

wins = 0
ties = 0
losses = 0
trials = 10000 

for i in range(trials):
  drawn_cards = random.sample(deck_left, missing + unknown_opponent_cards) #draws 7 random cards - 5 on table, 2 for opponent
  full_board = dealt + drawn_cards[:missing]
  opponent_cards = known_opponent_cards + drawn_cards[missing:]
  player_score = evaluate(player_cards + full_board)
  opponent_score = evaluate(opponent_cards + full_board)
  if player_score > opponent_score:
    wins = wins + 1
  elif player_score == opponent_score:
    ties = ties + 1
  else:
    losses = losses + 1

output = (wins + 0.5 * ties)/trials

#print("Wins:", wins, "Ties:", ties, "Losses:", losses) REMOVE HASTAG FOR THIS TO RUN

#the formula for margin for error is 1.96 * sqrt(p(1-p)/N) where p is probability of win, N is number of trials

#Published equity: AA - 85.2%, KK - 82.4%, AKs - 67.0%, AKo - 65.3%: OTHER VALUES ARE IN README
published_percentage = float(input("Published equity percentage of your hand:"))
published = published_percentage/100

margin = 1.96 * math.sqrt(published * (1 - published) / trials)
error = output - published
print(f"Equity: {output:.2%}   Published: {published:.2%}")
print(f"Difference: {error * 100:.2f} points   Margin: ±{margin * 100:.2f} percentage points")

if abs(error) <= margin:
  print("PASS: within 95% region")
else:
  print("FAIL: outside 95% region")


#number of possible 2 card sets:
#78 (4C2 * 13) pairs, 312 (13C2 * 4) suited, 936 (13C2 * 4 * 3) unsuited - 13C2 comes from choosing 2 distinct ranks from 13
#only have to check 13 pairs (as 'ah as' is the same value as 'ad ac')
#only check 78 (312/4) suited as suit doesn't matter (9h 8h is same as 9d 8d)
#only check 78 (936/(4*3)) as 12 arrangements for same numbers but different suit
#only check 78 + 78 + 13 = 169

















#code below: 1 game and gives outcome based on your cards
'''
player_text = "Ah kh"
player_cards = text_to_hand(player_text)
drawn_cards = random.sample(deck_left, missing + 2) #draws 7 random cards - 5 on table, 2 for opponent


full_board = dealt + drawn_cards[:missing]
opponent_cards = drawn_cards[missing:]

player_score = evaluate(player_cards + full_board)
opponent_score = evaluate(opponent_cards + full_board)

print("Player:  ", cards_to_text(player_cards), "->", category_names[player_score[0]])
print("Opponent:", cards_to_text(opponent_cards), "->", category_names[opponent_score[0]])
print("Dealt cards:", cards_to_text(full_board))

if player_score > opponent_score:
  print("Player wins")
elif player_score == opponent_score:
  print("Draw")
else:
  print("Opponent wins")
'''
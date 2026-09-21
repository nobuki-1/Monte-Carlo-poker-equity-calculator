import random
from evaluator import evaluate
import matplotlib as plt

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"] #all possible ranks 
suits = ["c", "h", "d", "s"] #possible suits: clubs, hearts, diamonds, spades

#this function ignores the opponents hand
def equity(player_cards, trials = 1000):
  leftover_deck = []
  for card in deck:
    if card not in player_cards:
      leftover_deck.append(card)
  wins = 0
  ties = 0
  losses = 0
  for i in range(trials):
    drawn_cards = random.sample(leftover_deck, 7) #draws the flop, turn, river
    cards_on_board = drawn_cards[:5]
    opponent_cards = drawn_cards[5:]
    player_score = evaluate(player_cards + cards_on_board)
    opponent_score = evaluate(opponent_cards + cards_on_board)
    if player_score > opponent_score:
      wins = wins + 1
    elif player_score == opponent_score:
      ties = ties + 1
    else:
      losses = losses + 1
  output_equity = (wins + 0.5 * ties)/trials
  return output_equity


def table_of_hands(trials):
  results = [] #making a list of all 169 possible hands
  for high_card in range(12,-1,-1): #looks at the higher rank of the 2 cards in the hand
    for low_card in range(high_card, -1, -1): #looks at the lower rank of the cards, has to be less than the high_card to run
      if high_card == low_card: #you have a pair
        pair_hand = [(high_card, 0), (low_card, 1)] #the 0,1 are representative of all possible combos of suits
        score = equity(pair_hand, trials)
        hand_type = ranks[high_card] + ranks[low_card]
        results.append((score, hand_type))
      else: #so not a pair
        suited_hand = [(high_card, 0), (low_card, 0)]
        unsuited_hand = [(high_card, 0), (low_card, 1)]
        suited_score = equity(suited_hand, trials)
        unsuited_score = equity(unsuited_hand, trials)
        suited_hand_type = ranks[high_card] + ranks[low_card] + "s"
        unsuited_hand_type = ranks[high_card] + ranks[low_card] + "o"
        results.append((suited_score, suited_hand_type))
        results.append((unsuited_score, unsuited_hand_type))
  results.sort(reverse=True) #sorts in equity order
  return results


if __name__ == "__main__":
  table = table_of_hands(300)
  #print(len(table)) #prints 169
  print("s: suited, o: offsuited")
  print(f"{'Rank':<6}{'Hand':<6}{'Equity':^8}")
  print("-" * 22) #prints a table of results - these are the headings

  position = 1
  for eq, label in table:
    print(f"{position:<6}{label:<6}{eq:^8.2f}")
    position = position + 1


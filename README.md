# Monte-Carlo-poker-equity-calculator

This program estimates the equity (expected share of the pot) of a specific hand
against a random hand in a 2 player game of Texas Hold'em (a poker variant)

# What the program does

It has multiple options:
1. Given your hand, the program will randomly deal the remaining cards in the deck a
certain number of times (the number is your choice) and output your equity. It also has
the option to adapt so that if the opponent hand or the cards that are on the board have
been dealt, it will output an equity based on this fact too.
2. The program also outputs a table which includes all 169 types of hand and their
corresponding equities over a chosen number of trials.

An example output:
Ah As -> 84.94% ± 0.70% (Ah As corresponds to ace of hearts and ace of spades)

# How the program works

1. Firstly, it removes the already known cards from the deck. These are the cards in your
hand and any known opponent or board cards.
2. It randomly deals however remaining cards required and determines whether the result
is a win, a tie or a loss and records this data. This is found in the page named simulator.
3. The winner of the round is determined using a program (found in page called evaluator)
which compares each hand mainly by scoring each hand type with a score (for example, a straight
flush, which includes a royal flush, scores 8 points, which is the maximum)
4. Equity is then calculated using (wins + 0.5 * ties)/trials - ties are counted as half as
the pot is split in this case.
5. The formula for a 95% margin of error (if this simulation were repeated, 95% would contain
the true value) is used and is given by 1.96 * sqrt((p(1-p))/N) where p is the published equity
and N is the number of trials. Calculated equities are then compared to published values and
gauged whether they are consistent with the given margin.
6. To obtain the table of results of equity for each hand, a function loops and creates all
169 different hands (13 pairs, 78 suited cards, 78 offsuited cards) and tests each one.

# An example output with margin included

10000 trials per hand
| Hand | Equity | Published | Margin | Result |
|------|--------|-----------|--------|--------|
| AA   | 84.94% | 85.2%     | ±0.70  | Pass   |
| KK   | 82.42  | 82.40     | ±0.75  | Pass   |
| AKs  | 66.92  | 67.0      | ±0.92  | Pass   |
| AKo  | 65.29  | 65.30     | ±0.92  | Pass   |
<img width="475" height="179" alt="image" src="https://github.com/user-attachments/assets/e12a8d2c-9884-4671-adf0-492bf5869a7e" />
Above is the table used as published equities.
Source: Equilab

## Running it

Requires Python 3, no external libraries.

- `python simulator.py`: single matchup (follow the prompts; edit the trials at the top of the file)
- `python results.py`: the 169-hand table
- `python checkers.py`: the symmetry check
- `python test.py`: evaluator tests

# Testing
This checks the evaluator against specific examples - it tests every hand type, tests the wheel 
(A-2-3-4-5 straight) and for tiebrakers in the case of a 4 pair or a pair of 2 pairs. There are 25
tests and all 25 pass.

# Other

The equity of all 169 hand types, averaged with weights, should be 0.5 in a 2-player game, because 
each pot is shared between the two players (their shares sum to 1) and neither player has an advantage 
before the cards are dealt. Each hand type is weighted by how many real two-card hands it represents 
(pairs 6, suited 4, offsuit 12; 1,326 in total). The result was 0.4999 (10000 trials per hand), consistent 
with 0.5, which shows the simulation is unbiased..

The program also loops through 169 possible hands instead of 1326 hands (this is the actual number
of hands and is given by 52C2 = 1326) as suits are interchangeable and no suit outranks another - 
for example, the hand 9h 8d is equivalent to 9s 8h enabling the run time to be cut down by a large
amount.

# What each file does

Cards.py -> converts text input into tuples which the program understands, contains the full deck of cards
            and the list of all ranks and suits.
Evaluator.py -> contains the rules of Poker scoring and decided which hand wins.
Simulator.py -> contains the simulation for a single hand and provides the margin of error.
Results.py -> contains the table of results for all 169 hand types.
Checkers.py -> contains the check for the expected average score.
Test.py -> tests the program.

# Limitations

- This program only works for a 2 person game.
- The equity calculation ignores folding which is highly unrealistic.
- Only valid for the Texas Hold'em variant.
- The opponent is random so the equity overstates your chances against real opponents, who fold weak hands.
- Results are estimates, and the margin covers sampling noise only.














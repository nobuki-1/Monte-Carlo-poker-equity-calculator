#function of this is to find a weighted average checker,
#prove that, for 2 players playing poker, over time, equity will be 0.5 as total for each round is 1
from results import table_of_hands

table = table_of_hands(10000)

total = 0
for equity, label in table:
  if len(label) == 2: #i.e - in form KK/AA/99 so its a pair
    weight = 6 #as 6 different ways of obtaining a pair
  elif label[2] == 's':
    weight = 4 #as 4 different ways to obtain suited set as there are 4 suits
  elif label[2] == 'o':
    weight = 12 #as 4x3=12 ways to arrange 2 distinct suits from 4
  total = total + equity * weight

print(total)
print(f"The average weighted score is: {(total/1326):.4f}")
  
#1326 is total number of possible hands: 52C2 = 1326

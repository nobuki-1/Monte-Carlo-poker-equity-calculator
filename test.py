from evaluator import evaluate
from cards import text_to_hand


def score(text):
    return evaluate(text_to_hand(text))


# each category: the string on the right is what prints if the assertion fails
assert score("Ah Kd Qc 9s 4d 3h 2c") == (0, [12, 11, 10, 7, 2]), "high card"
assert score("Ah Ad Kc 9s 4d 3h 2c") == (1, [12, 11, 7, 2]), "pair"
assert score("Ah Ad Kh Kd Jc 5s 3h") == (2, [12, 11, 9]), "two pair"
assert score("Ah Ad Ac Ks Qd 7h 9c") == (3, [12, 11, 10]), "three of a kind"
assert score("5h 6d 7c 8s 9h Kd 2c")[0] == 4, "straight"
assert score("2h 5h 9h Jh Kh 3c 7d") == (5, [11, 9, 7, 3, 0]), "flush"
assert score("Ah Ad Ac Ks Kd 7h 9c") == (6, [12, 11]), "full house"
assert score("Ah Ad Ac As 2h 2d Kc") == (7, [12, 11]), "four of a kind"
assert score("5h 6h 7h 8h 9h Kd 2c") == (8, [7]), "straight flush"


assert score("Ah Ad Kh Kd 2c 2s Qh") == (2, [12, 11, 10]), "three pairs: queen kicker beats the third pair"
assert score("Ah Ad Ac Ks Kd Qh Qs") == (6, [12, 11]), "full house with two extra pairs uses the higher pair"
assert score("Ah Ad Ac Ks Kd Kh 2c") == (6, [12, 11]), "full house from two sets of trips"
assert score("Ah Kh Qh 9h 5h 2h 3c") == (5, [12, 11, 10, 7, 3]), "six-card flush keeps the best five"
assert score("5h 6h 7h 8h Kh 9c 2d") == (5, [11, 6, 5, 4, 3]), "flush + straight on different cards is only a flush"
assert score("Ah 2d 3c 4s 5h Kd 9c")[0] == 4, "the wheel is a straight"
assert score("Qh Kd Ac 2s 3h 7d 9c") == (0, [12, 11, 10, 7, 5]), "Q-K-A-2-3 is not a straight"
assert score("Ah 2h 3h 4h 5h Kd 9c")[0] == 8, "wheel straight flush"


assert score("Ah 2d 3c 4s 5h Kd 9c") < score("2h 3d 4c 5s 6h Kd 9c"), "wheel loses to a 6-high straight"
assert score("Ah 2d 3c 4s 5h 6d 9c") > score("Ah 2d 3c 4s 5h Kd 9c"), "6-high beats the wheel when both are present"
assert score("5h 6d 7c 8s 9h Td Jc") > score("5h 6d 7c 8s 9h Kd 2c"), "jack-high straight beats nine-high"
assert score("Ah Kh Qh Jh Th 2c 3d") > score("Kh Qh Jh Th 9h 2c 3d"), "royal beats king-high straight flush"
assert score("Ah Ad Kc 9s 4d 3h 2c") > score("Ac As Qc 9d 4h 3s 2d"), "pair of aces: king kicker beats queen"
assert score("Ah Ad Kh Kd 2c 2s Qh") > score("Ac As Kc Ks Jd 5h 3s"), "two pair: queen kicker beats jack"
assert score("Ah Kh Qh 9h 5h 2c 3d") > score("Ah Kh Qh 9h 4h 2c 3d"), "flush: the fifth card decides"


assert score("Ah Kd Qc 9s 4d 3h 2c") == score("Ac Kh Qd 9h 4s 3c 2d"), "different suits, same ranks: a tie"

print("All tests passed")
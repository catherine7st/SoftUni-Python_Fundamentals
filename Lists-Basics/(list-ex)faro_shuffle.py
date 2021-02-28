# cards = input().split()
# shuffles = int(input())
#
# before_sh = deck
# after_sh = []
#
# for i in range(shuffles):
#     after_sh = []
#     for j in range(len(deck)//2):
#         after_sh.append(before_sh[j])
#         after_sh.append(before_sh[j + len(deck) // 2])
#     before_sh = after_sh
#
# print(after_sh)
#
#
import copy

cards = input().split()
shuffles = int(input())

top_card = cards[0]
bottom_card = cards[-1]
half = len(cards) // 2

shuffle_cards = []

for shuffle in range(shuffles):
    left_cards = []
    right_cards = []

    for i in range(1, half):
        left_cards.append(cards[i])

    for i in range(half, len(cards) - 1):
        right_cards.append(cards[i])

    for i in range(len(left_cards)):
        shuffle_cards.append(right_cards[i])
        shuffle_cards.append(left_cards[i])

    cards = shuffle_cards.copy()
    cards.append(bottom_card)
    cards.insert(0, top_card)
    shuffle_cards = []

print(cards)

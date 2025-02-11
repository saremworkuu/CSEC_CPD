n = int(input())
cards = list(map(int, input().split()))

sereja_score = 0
dima_score = 0

turn = 0

while cards:
    if cards[0] > cards[-1]:
        chosen_card = cards.pop(0)
    else:
        chosen_card = cards.pop(-1)

    if turn == 0:
        sereja_score += chosen_card
    else:
        dima_score += chosen_card

    turn = 1 - turn

print(sereja_score, dima_score)

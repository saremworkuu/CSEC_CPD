def calculate_calories(calories, game_sequence):
    total = 0
    for c in game_sequence:
        total += calories[int(c) - 1]
    print(total)

a, b, c, d = map(int, input().split())
s = input()

calculate_calories([a, b, c, d], s)

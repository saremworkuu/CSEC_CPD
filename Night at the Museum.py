def minimum_rotations(name):
    current = 'a'
    total_moves = 0
    
    for letter in name:
        clockwise = abs(ord(letter) - ord(current))
        counterclockwise = 26 - clockwise
        total_moves += min(clockwise, counterclockwise)
        current = letter
    
    print(total_moves)

name = input().strip()
minimum_rotations(name)

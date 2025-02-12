def birds_on_wires(n, birds, m, shots):
    for x, y in shots:
        x -= 1
        left_birds = y - 1
        right_birds = birds[x] - y

        if x > 0:
            birds[x - 1] += left_birds
        if x < n - 1:
            birds[x + 1] += right_birds

        birds[x] = 0

    return birds

n = int(input().strip())  
birds = list(map(int, input().split()))
m = int(input().strip())  
shots = [tuple(map(int, input().split())) for _ in range(m)]

result = birds_on_wires(n, birds, m, shots)
for count in result:
    print(count)

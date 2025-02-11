n = int(input())
events = list(map(int, input().split()))

u_c = 0
a_o = 0

for event in events:
    if event == -1:
        if a_o > 0:
            a_o -= 1
        else:
            u_c += 1
    else:
        a_o += event

print(u_c)

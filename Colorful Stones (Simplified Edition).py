def f_p(s, t):
    p = 1  
    for move in t:
        if s[p - 1] == move:
            p += 1
    print(p)

s = input().strip()
t = input().strip()
f_p(s, t)

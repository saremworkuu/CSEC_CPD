def m_s(k, r):
    for i in range(1, 11):
        total_cost = k * i
        if total_cost % 10 == 0 or total_cost % 10 == r:
            print(i)
            return

k, r = map(int, input().split())
m_s(k, r)

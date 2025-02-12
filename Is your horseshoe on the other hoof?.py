def min_horseshoes_to_buy(s1, s2, s3, s4):
    return 4 - len(set([s1, s2, s3, s4]))

s1, s2, s3, s4 = map(int, input().split())
print(min_horseshoes_to_buy(s1, s2, s3, s4))

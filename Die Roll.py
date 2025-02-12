from math import gcd

def winning_p(y, w):
    highest = max(y, w)
    favorable_outcomes = 6 - highest + 1
    gcd_value = gcd(favorable_outcomes, 6)
    return f"{favorable_outcomes // gcd_value}/{6 // gcd_value}"

y, w = map(int, input().split())
print(winning_p(y, w)

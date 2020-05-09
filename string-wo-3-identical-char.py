# https://leetcode.com/discuss/interview-question/398037/
from itertools import groupby

def stringWithout3Identical(S):
    ans = ''
    for c, g in groupby(S):
        print(list(g))
        L = len(list(g))
        ans += c * min(L, 2)
    return ans

S = 'eedaaad'
print(stringWithout3Identical(S))

S = 'xxxtxxx'
print(stringWithout3Identical(S))

S = 'uuuuxaaaaxuuu'
print(stringWithout3Identical(S))

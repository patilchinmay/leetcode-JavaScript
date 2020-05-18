# https://leetcode.com/discuss/interview-question/398026/
from itertools import groupby

def solution(s):
    ans = 0

    for c, g in groupby(s):
        group = list(g)
        # print(c, group, len(group))
        if len(group) <= 2:
            # print("Do Nothing")
            continue
        else:
            # print("Increse ANS", len(group)//3)
            ans += len(group)//3

    return ans

if __name__ == "__main__":
    print("baaab", solution("baaab"))
    print("baaaab", solution("baaaab"))
    print("baaaaab", solution("baaaaab"))
    print("baaaaaab", solution("baaaaaab"))
    print("baaaaaaaaaab", solution("baaaaaaaaaab"))

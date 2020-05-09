from itertools import groupby

def longestWithout3(S):
    loc, ans = '', ''
    for c, g in groupby(S):
        glen = len(list(g))
        print(c, list(g))
        ans = max([ans, loc + c * min(glen, 2)], key=len)
        if glen > 2:
            loc = c*2
        else:
            loc += c*glen
    return ans

if __name__ == "__main__":
    assert longestWithout3("aabbaaaaabb") == "aabbaa"
    # assert longestWithout3("aabbaaaaabbaabbaabbaabbab") == "aabbaabbaabbaabbab"
    # assert longestWithout3("aabbaabbaabbaa") == "aabbaabbaabbaa"
    # assert longestWithout3("aaabb") == "aabb"

    print("all tests passed")
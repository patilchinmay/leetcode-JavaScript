# https://leetcode.com/discuss/interview-question/398035/
import collections

def solution(s):
    counter = collections.Counter(s).most_common()
    print(counter)
    ans = 0

    count_set = set()

    for char, count in counter:
        last_added = 0
        if count in count_set:
            print("Exist in set", char , count)
            if count == 1:
                ans += count
            elif last_added <= count:
                ans += count
            else:
                ans += 1
        else:
            print("Not in set", "Adding ",char)
            count_set.add(count)
            last_added = count

    print(count_set)
    return ans

if __name__ == "__main__":
    print("eeeeffff", solution("eeeeffff"))
    print("aabbffddeaee", solution("aabbffddeaee"))
    print("llll", solution("llll"))
    print("example", solution("example"))

# https://leetcode.com/discuss/interview-question/344677

ropes = [1, 2, 5, 10, 35, 89]

ropes.sort(reverse=True)
ans = []

while(len(ropes)>1):
    a = ropes.pop()
    b = ropes.pop()
    print(a,b)
    print('Added', a+b)
    ropes.append(a+b)
    ans.append(a+b)
    print(ropes)
    ropes.sort(reverse=True)

print(sum(ans))

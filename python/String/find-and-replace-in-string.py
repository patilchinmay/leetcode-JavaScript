# https://leetcode.com/problems/find-and-replace-in-string/submissions/

class Solution:
    def findReplaceString(self, S: str, indexes: [int], sources: [str], targets: 
		[str]) -> str:
        
        if len(indexes) == 0:
            return S
        
        ans = []
        
        i = 0
        
        while i < len(S):
            # print("i = ",i)
            if i not in indexes:
                # print(i, "not in indexes")
                ans += S[i]
            else:
                index = indexes.index(i)
                # print(i, "IS in indexes at index = ", index)
                
                # print("\tFinding ", sources[index])
                
                position = S.find(sources[index], i, i+len(sources[index]))
                # print("\tPostion = ", position)
                
                if position == -1:
                    ans += [S[i]]
                else:
                    ans += list(targets[index])
                    i = i + len(sources[index]) - 1
            i+=1    
            # print(ans)
            
        return "".join(ans)

# "abcdddd"
# [0, 2, 5]
# ["ab", "c", "d"]
# ["eee", "ffff", "zz"]
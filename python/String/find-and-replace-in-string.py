# https://leetcode.com/problems/find-and-replace-in-string/submissions/

class Solution:
    def findReplaceString(self, S: str, indexes: [int], sources: [str], targets: 
		[str]) -> str:
        
		# Corner case
        if len(indexes) == 0:
            return S
        
		# List are mutable and faster to operate with compared to strings
        ans = []
        
        i = 0
        
        while i < len(S):
            # print("i = ",i)
            if i not in indexes:
                # print(i, "not in indexes")
                ans += S[i]
            else:
				# Find at which index is 'i' present in indexes so that value can be used to get the relevant sources and targets values.
                index = indexes.index(i)
                # print(i, "IS in indexes at index = ", index)
                
                # print("\tFinding ", sources[index])

                # Equivalent to => S[i:].startswith(sources[index])
				# Find if the string has sources[index] at postion i thorugh i+len(sources[index])
                position = S.find(sources[index], i, i+len(sources[index]))
                # print("\tPostion = ", position)
                
                if position == -1:
					# sources[index] was not found at the required position
                    ans += [S[i]]
                else:
					# # sources[index] was found at the required position. Add targets[index] to answer
                    ans += list(targets[index])
                    i = i + len(sources[index]) - 1 # subtracting 1 from correct value as we will add that 1 at the end of the loop (on next line) anyway.
            i+=1    
            # print(ans)
            
        return "".join(ans)

# "abcdddd"
# [0, 2, 5]
# ["ab", "c", "d"]
# ["eee", "ffff", "zz"]
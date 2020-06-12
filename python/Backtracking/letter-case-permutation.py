# https://leetcode.com/problems/letter-case-permutation/submissions/
# Create a horizontal tree of traversing this problem to understand better.

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        answer = []
        # Split the string into list. split() doesn't work
        string_arr = list(S)
        
        self.backtrack(0, answer, string_arr)

        return answer
    
    def backtrack(self, index, answer, S):
        # define return conditions
        if index == len(S):
            answer.append(''.join(S.copy()))
            return
        
        # Process the node
        if ((S[index]>='a' and S[index]<='z') or (S[index]>='A' and S[index]<='Z')):
            # Uppercase
            S[index] = S[index].upper()
            # Call next position
            self.backtrack(index+1, answer, S)
            
            # Lowercase
            S[index] = S[index].lower()
            # Call next position
            self.backtrack(index+1, answer, S)
            
        else:
            # Anything other than english alphabet
            self.backtrack(index+1, answer, S)
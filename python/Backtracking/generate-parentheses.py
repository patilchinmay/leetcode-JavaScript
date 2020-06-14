# https://leetcode.com/problems/generate-parentheses/submissions/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return [""]
        
        # Available options to generate from at the beginning
        open_p = ['('] * n
        close_p = [')'] * n
        
        answer = []
        path = []
        
        self.backtrack(0, n, path, open_p, close_p, answer)
        
        return answer
    
    def backtrack(self, index, n, path, open_p, close_p, answer):
        # print(index, "path=", path, "\t",open_p, "\t",close_p)

        # More closing parenthesis than opening parenthesis
        if  path.count(')') > path.count('('):
            return
        
        # Return condition
        if index == n*2:
            answer.append("".join(path.copy())) # Add to the answer
            return

        # Process the node (path) in 2 possible ways

        # append opening parenthesis
        if open_p:
            path.append(open_p.pop())
            self.backtrack(index+1, n, path, open_p, close_p, answer)
            open_p.append(path.pop()) #Backtrack

        # append closing parenthesis
        if close_p:
            path.append(close_p.pop())
            self.backtrack(index+1, n, path, open_p, close_p, answer)
            close_p.append(path.pop()) #Backtrack
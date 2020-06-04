# https://leetcode.com/problems/simplify-path/submissions/
class Solution:
    def simplifyPath(self, path: str) -> str:
        path_arr = path.split("/") # Remove /
        path = [x for x in path_arr if x] #  Remove / and empty chars

        ans = []

        for i in range(len(path)):
            if path[i] == '..':
                if ans:
                    ans.pop() # Remove the item (go back in dir) only if there is something to remove.
            elif path[i] != '.':
                ans.append(path[i])

        return "/"+"/".join(ans)

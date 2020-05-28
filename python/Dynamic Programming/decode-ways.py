# https://leetcode.com/problems/decode-ways/submissions/
# https://leetcode.com/problems/decode-ways/discuss/650945/Python-DP-O(1)-space-clear-explanation

class Solution:
    def numDecodings(self, s: str) -> int:
        
        if not s or s[0] == "0":
            return 0
        
        dp = [1] + [0] * len(s)
        dp[1] = 1
        
        for i in range(2, len(s)+1):
            # print("START i = ", i, " char = ", s[i-1], " dp = ", dp) 

            if 1 <= int(s[i-1]) <= 9:
                dp[i] = dp[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
                
            # print("END i = ", i, " char = ", int(s[i-2:i]), " dp = ", dp) 
        # print(dp) 
        return dp[-1]

# "001"
# "110"
# "100"
# "100001"
# "000"
# "10101"
# "1010"
# ""
# "0"
# "1"
# "99"
# "226"
# "2626"
# "262622"
# "12222"
# "122221"
# "122229"
# https://leetcode.com/problems/camelcase-matching/submissions/

import re

class Solution:
    def camelMatch(self, queries: [str], pattern: str) -> [bool]:
                
        # Splitting the pattern
        pattern = list(pattern)
        
        # Generating the REGEX pattern
        regex_pattern = r"^[a-z]*"+"[a-z]*".join(pattern)+"[a-z]*$"
        # print(regex_pattern)
        
        ans = [ (re.search(regex_pattern, query) != None) for query in queries]
        
        return ans
    
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# "FB"
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# "FoBa"
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# "FoBaT"
# ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"]
# "aFoBaT"
# ["CompetitiveProgramming","CounterPick","ControlPanel"]
# "CooP"
# ["aksvbjLiknuTzqon","ksvjLimflkpnTzqn","mmkasvjLiknTxzqn","ksvjLiurknTzzqbn","ksvsjLctikgnTzqn","knzsvzjLiknTszqn"]
# "ksvjLiknTzqn"
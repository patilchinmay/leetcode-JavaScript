# https://leetcode.com/problems/restore-ip-addresses/submissions/

class Solution:
    def restoreIpAddresses(self, s: str) -> [str]:
        if len(s) < 4:
            return []
        
        s = list(s)
        
        answer = set()
        
        self.backtrack(s, 0, [], answer)
        
        return answer
    
    def backtrack(self, s, index, current_path, answer):
        # print(index, current_path)
        
        # Define boundaries and conditions
        if len(current_path) == 4: # make sure we stop at 4th octet of IP adr
            ans = ".".join(current_path.copy())
            if len(ans) == (len(s)+3): # Input and answer match in length. 3 is added to account for 3 '.' that join the current_path
                answer.add(ans)
            return
        
        # Don't process if index is higher than len(s)
        if index >= len(s):
            return
        
        for i in range(1,4):
            ip_part_string = "".join(s[index:index+i])
            # Skip blank strings
            if ip_part_string:
                # Make sure the IP is in valid range
                if 0 <= int(ip_part_string) <= 255: 
                    # Handle the case of 0 being in the beginning of ip_part_string e.g. int('010') => 10. Example input => "10101010"
                    if len(ip_part_string) == len(str(int(ip_part_string))):
                        current_path.append(ip_part_string)
                        self.backtrack(s, index+i, current_path, answer)
                        del current_path[-1] # Backtrack
    
# "25525511135"
# "1111"
# "2552552550"
# "10101010"
# "256256256256"
# "00010"
# "19216801"
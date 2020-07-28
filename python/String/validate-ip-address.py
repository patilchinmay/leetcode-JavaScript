# https://leetcode.com/problems/validate-ip-address/submissions/

class Solution:
    def validIPAddress(self, IP: str) -> str:
    
        if ':' in IP and self.validateIPv6(IP):
            return "IPv6"
        
        if '.' in IP and self.validateIPv4(IP):
            return "IPv4"
        
        return "Neither"
    
    def validateIPv6(self, IP):
        ip_arr  = IP.split(':')

        if len(ip_arr) != 8:
            return False

        for i in range(8):
            if len(ip_arr[i]) > 4:
                return False

            try:
                ip_arr[i] = hex(int(ip_arr[i], 16))[2:]
            except:
                return False

        return True
    
    def validateIPv4(self, IP):            
        ip_arr  = IP.split('.')

        if len(ip_arr) != 4:
            return False

        for i in range(4):
            try:
                ip_part = int(ip_arr[i])
                
                if not (0 <= ip_part <= 255):
                    return False
                
                if len(  str( ip_part ) ) != len(ip_arr[i]):
                    return False
            except:
                return False

        return True

'''
"2001:0db8:85a3:0000:0000:8a2e:0370:7334"
"2001:0db8:85a3:0:0:8A2E:0370:7334"
"2001:0db8:85a3::8A2E:0370:7334"
"02001:0db8:85a3:0000:0000:8a2e:0370:7334"
"172.16.254.1"
"256.256.256.256"
"10.10.10.10"
"0.0.0.0"
"abcde"
"abc:.def.ghi.jkl"
"abc.:def.ghi.jkl"
"..."
":::"
'''
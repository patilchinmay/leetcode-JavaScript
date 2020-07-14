# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/submissions/

class Solution:
    def maxVowels(self, s, k: int) -> int:
        
        str = s[:k]
            
        temp = str.count('a') + str.count('e') + str.count('i') + str.count('o') + str.count('u')
        
        max = temp
        
        vowels  = ['a', 'e', 'i', 'o', 'u']
        
        for i in range(0, len(s)-k):
            
            if s[i] in vowels:
                temp -=  1
            
            if s[i+k] in vowels:
                temp += 1
                
            if temp > max:
                max = temp
            
            # print(i, s[i], s[i+k-1], max)
            
        return max

# "abciiidef"
# 3
# "aeiou"
# 2
# "leetcode"
# 3
# "rhythms"
# 4
# "tryhard"
# 4
# "yudmscfyiojonpapzrbycjajwkqtcnokmchwkyjnznvrouwghhjlcycbglkmziqspglugfzfqvzceyedxrimlrnucbkqfeaxkpopuoeclkpiuvwqmtfcrxrtnvertmneiunwlysctapotabvzpbermtyemyxodpiwyahawfynkzglgoiehbdmwuhiqbgnsbjeijjevrishtlzsdmvqehvtxphhatgycsfdmxpbgmgcpacqbvmzcxzvricqixgmivbmwhisqlmoazgdoawtwjvzidakeshfpwwafzjbaskzaurxhkwffztjuqwdowknqtdhusogrlwqbjqlyapmuyfmgpaefpzbbvhfwpcymzpphxhrdhkgtkiszdaytyhrpzmsdodllzfiquzunlejxealjxrqrjoqslznbhhmdkfmgojojknejttnghbxjjqxvkeigdlnfvrxmvlyriknmgrnghqnxlxaylsxiwvvmmqycktrayzpgmcgmfmjmpbfrnejemjbryeirbzccxwlrirdnwsdlxirifjjpugkrnycimynrbmugxrrroeetnfxxkymuxwemlorrwsimyqfosynbgeqdkjxoowwotnitijybspywlufxlpidqejxtddixqqwhhvkvvxdtbkvqyuygyevoosicrhsulsyovwtnlgoafcrdbczsvvisqvjeheipqsohicbsyggscsocrzpyzwgwdmxjcfpforlayoxxgjlmnayetbzsqtiihvoxvpsmmmlamlxleidvlwqvisjsbzentrryvhmquthyyvbpiylefhfargeqwlrdimrbvqtkxmikehxqmolduojvctnhkbopnypuosnwugzavinnoebsbmedplgkqvnnaszftgwbqqsvwfcxvhyupxjssmyjmiobgnjxziapamuagiuycuycyxvljxgchczqqulrryaeljzlvdteadjqmbfvoxrtxchgefmsztxwmignzgq...
# 57373
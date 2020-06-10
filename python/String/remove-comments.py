# https://leetcode.com/problems/remove-comments/submissions/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        import re
        
        source = '\n'.join(source)
        
        # print(source)
        
        single_line = r"\/\/.*"
        multiline_closed = r"(?s:\/\*.*?\*\/)"
        multiline_not_closed = r"\/\*.*"    
        
        # // abc
        # first regex will match above

        # /* abc
        # abc
        # abc */
        # second regex will match above

        # if there is a comment where sinlge line comment is enclosed in the multiline comment and it is on last line, third regex will match that
        
        # order matters
        regex = '|'.join([single_line, multiline_closed, multiline_not_closed])
        
        Filtered = re.sub( regex, "", source)
        
        # print(Filtered)
        
        return [ item for item in Filtered.split('\n') if item != ""]
# https://leetcode.com/problems/letter-tile-possibilities/submissions/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Using set so that duplicates will not be counted even if input has repeating letters.
        # Use list if it is confirmed that input will have distinct letters.
        answer = set()
    
        # Initially available_items == tiles (as we have not started, so all possibilities are available) and current_path is empty
        current_path = []
        available_items = list(tiles) # Using as list so it is easy to manipulate
    
        self.backtrack(0, answer, current_path, available_items, tiles )
        
        return(len(answer))
        
    def backtrack(self, index, answer, current_path, available_items, tiles):
        # define returning condition for recursion (dfs)
        if index == len(tiles):
            return
      
        # Initially available_items == tiles (as we have not started, so all possibilities are available) and current_path is empty
        for i in range(len(available_items)):
            '''
            Remove the i'th item from available items
            Add that item to current path
            
            e.g. If a string given in input is "ABC"
            At index = 0 (before processing next line, the vars will be)
              i=0 current_path = [], available_items = [A, B, C]
              i=1 current_path = [], available_items = [A, B, C]
              i=2 current_path = [], available_items = [A, B, C]
            
            At index = 0 (after processing next line, the vars will be)
              i=0 current_path = [A], available_items = [B, C]
              i=1 current_path = [B], available_items = [A, C]
              i=2 current_path = [C], available_items = [A, B]
            
            At index = 1 (w.r.t. i=0 from above) (after processing next line, the vars will be)
              i=0 current_path = [A, B], available_items = [C]
              i=1 current_path = [A, C], available_items = [B]
            
            At index = 2 (w.r.t. i=0 from above) (after processing next line, the vars will be)
              i=0 current_path = [A, B, C], available_items = []
            
            So on.... 
            recursive calls will make sure to traverse the tree via DFS and collect all the possibilities
            '''
            current_path.append(available_items.pop(i))
            
            answer.add("".join(current_path))
            
            self.backtrack( index+1, answer, current_path, available_items, tiles )
      
            # Reverse the processing that we did earlier a.k.a. backtrack
            available_items.insert(i, current_path.pop())
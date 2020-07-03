# https://leetcode.com/submissions/detail/361407999/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: ['Employee'], id: int) -> int:
        if not employees:
            return 0
        
        employees_dict = { employee.id: (employee.importance, employee.subordinates) for employee in employees }
            
        result = 0
        
        queue = [ employees_dict[id] ]
        
        while queue:
            
            imp, subs = queue.pop(0)
            
            result+=imp
            
            if subs:
                for sub in subs:
                    queue.append( employees_dict[sub] )
        
        return result
# https://leetcode.com/problems/employee-importance/submissions/

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
        
        result = 0
        queue = [ self.findEmployeeWithID(id, employees) ]
        
        while queue:
            
            _, imp, subs = queue.pop(0)
            
            result+=imp
            
            if subs:
                for sub in subs:
                    queue.append( self.findEmployeeWithID(sub, employees) )
        
        return result
        
    def findEmployeeWithID(self, id, employees):
        for employee in employees:
            if id == employee.id:
                return (employee.id, employee.importance, employee.subordinates)